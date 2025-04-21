import pymysql
import creds 
from flask import Flask, render_template, request
import boto3
app = Flask(__name__)

#Creates connection to MySQL
def get_conn():
    conn = pymysql.connect(
        host= creds.host,
        user= creds.user, 
        password = creds.password,
        db=creds.db,
        )
    return conn
 
#Function that executes SQL queries 
def execute_query(query, args=()):
    cur = get_conn().cursor()
    cur.execute(query, args)
    rows = cur.fetchall()
    cur.close()
    return rows


#Function to generate HTML table 
def display_html(rows):
    html = ""
    html += """<table><tr><th>Country</th><th>Cities</th><th>Population</th></tr>"""

    for r in rows:
        html += "<tr><td>" + str(r[0]) + "</td><td>" + str(r[1]) + "</td><td>" + str(r[2]) + "</td></tr>"
    html += "</table></body>"
    return html

#Displays top 10 cities for a given country entered by user based on population
@app.route("/countryquery/<country>")
def viewdb(country):
    rows = execute_query("""SELECT country.name, city.name, city.population
                FROM city JOIN country on city.countrycode = country.code
                WHERE country.name = %s 
                ORDER BY city.population DESC 
                Limit 10
                """, (str(country))
                )
    return display_html(rows)


#Route to create the textbox form
@app.route("/countryquerytextbox", methods = ['GET'])
def country_form():
  return render_template('textbox.html', fieldname = "Country")

#DynamoDB setup
TABLE_NAME = "Vacation"

#Insert City inyo DynamoDB 
#Return SQL Query result for country entered by user 
#POST to recieve form submission 
dynamodb = boto3.resource('dynamodb', region_name="us-east-1")
table = dynamodb.Table(TABLE_NAME)
@app.route("/countryquerytextbox", methods = ['POST'])
def country_form_post():
  text = request.form['text']
  newcity = request.form['city']
  cost_value = 1000
  #puts new city into DynamoDB table
  table.put_item(
      Item = { 
          'City' : newcity,
          'Cost' : cost_value
      }
      
  ) 
  #returns HTML diplays top 10 cities
  return viewdb(text)

#Starts Flask server 
if __name__ == '__main__': 
    app.run(host = '0.0.0.0', port=8080, debug=True)