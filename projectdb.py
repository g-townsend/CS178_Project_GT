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
        html += "<tr><td>" + str(r[0]) + "</td><td>" + str(r[1]) + "</td><td>" + str(r[2]) + "</td></tr>"
    html += "</table></body>"
    return html


@app.route("/languagequery/<language>")
def viewdb(language):
    rows = execute_query("""SELECT city.name, city.population, country.name
                FROM city JOIN country on city.countrycode = country.code JOIN country using (countrycode)
                WHERE language = %s and percentage > 80
                """, (str(language))
                )
    return display_html(rows)

from flask import request

from flask import render_template
@app.route("/languagequerytextbox", methods = ['GET'])
def langauge_form():
  return render_template('textbox.html', fieldname = "language")


@app.route("/languagequerytextbox", methods = ['POST'])
def language_form_post():
  text = request.form['text']
  return viewdb(text)

if __name__ == '__main__': 
    app.run(host = '0.0.0.0', port=8080, debug=True)
