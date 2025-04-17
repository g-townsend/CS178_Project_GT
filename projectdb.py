import pymysql
import creds 
from flask import Flask
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
    html += """<table><tr><th>City</th><th>Population</th><th>Country</th></tr>"""

    for r in rows:
        html += "<tr><td>" + str(r[0]) + "</td><td>" + str(r[1]) + "</td><td>" + str(r[2]) + "</td><td>"+ str(r[3]) + "</td></tr>"
    html += "</table></body>"
    return html


@app.route("/countryquery/<country>")
def viewdb(country):
    rows = execute_query("""SELECT country.name, country.population, country.capital. city.name
                FROM city JOIN country on city.countrycode = country.code
                WHERE country.name = %s 
                """, (str(country))
                )
    return display_html(rows)

from flask import request

from flask import render_template
@app.route("/countryquerytextbox", methods = ['GET'])
def country_form():
  return render_template('textbox.html', fieldname = "Country")


@app.route("/countryquerytextbox", methods = ['POST'])
def country_form_post():
  text = request.form['text']
  return viewdb(text)

if __name__ == '__main__': 
    app.run(host = '0.0.0.0', port=8080, debug=True)
