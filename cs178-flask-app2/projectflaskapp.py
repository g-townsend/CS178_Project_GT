import pymysql
import creds 
from flask import Flask, render_template

import boto3
app = Flask(__name__)

def get_conn():
    conn = pymysql.connect(
        host= creds.host,
        user= creds.user, 
        password = creds.password,
        db=creds.db,
        )
    return conn
 
def execute_query(query, args=()):
    cur = get_conn().cursor()
    cur.execute(query, args)
    rows = cur.fetchall()
    cur.close()
    return rows


#display the sqlite query in a html table
def display_html(rows):
    html = ""
    html += """<table><tr><th>Country</th><th>Cities</th><th>Population</th></tr>"""

    for r in rows:
        html += "<tr><td>" + str(r[0]) + "</td><td>" + str(r[1]) + "</td><td>" + str(r[2]) + "</td></tr>"
    html += "</table></body>"
    return html


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

from flask import request

@app.route("/countryquerytextbox", methods = ['GET'])
def country_form():
  return render_template('textbox.html', fieldname = "Country")

import boto3
TABLE_NAME = "Vacation"

dynamodb = boto3.resource('dynamodb', region_name="us-east-1")
table = dynamodb.Table(TABLE_NAME)
@app.route("/countryquerytextbox", methods = ['POST'])
def country_form_post():
  text = request.form['text']
  newcity = request.form['city']
  cost_value = 1000
  table.put_item(
      Item = { 
          'City' : newcity,
          'Cost' : cost_value
      }
      
  ) 

  return viewdb(text)

if __name__ == '__main__': 
    app.run(host = '0.0.0.0', port=8080, debug=True)