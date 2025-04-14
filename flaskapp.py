from flask import Flask
app = Flask(__name__)
@app.route ('/')
def hello (): 
    return '<h1>Hello from Flask!</h1>'

@app.route('/about')
def about(): 
    return '<h2>An about page!</h2>'

@app.route('/numvowels/<var>')
def numvowels(var): 
    A = var.count('A')
    a = var.count ('a')
    E = var.count('E')
    e = var.count ('e')
    I= var.count('I')
    i = var.count ('i')
    O = var.count('O')
    o= var.count ('o')
    U = var.count('U')
    u = var.count('u')
    results = A + E + I + O + U + a + e + i + o + u
    return str(results)
import pymysql
import creds 



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
    html += """<table><tr><th>ArtistID</th><th>Artist</th><th>Track Title</th><th>Price</th><th>Milliseconds</th></tr>"""

    for r in rows:
        html += "<tr><td>" + str(r[0]) + "</td><td>" + str(r[1]) + "</td><td>" + str(r[2]) + "</td><td>" + str(r[3]) + "</td><td>" + str(r[4]) + "</td></tr>"
    html += "</table></body>"
    return html


@app.route("/viewdb")
def viewdb():
    rows = execute_query("""SELECT ArtistId, Artist.Name, Track.Name, UnitPrice, Milliseconds
                FROM Artist JOIN Album using (ArtistID) JOIN Track using (AlbumID)
                ORDER BY Track.Name 
                Limit 500""")
    return display_html(rows)

@app.route("/pricequery/<price>")
def viewprices(price):
    rows = execute_query("""select ArtistId, Artist.Name, Track.Name, UnitPrice, Milliseconds
            from Artist JOIN Album using (ArtistID) JOIN Track using (AlbumID)
            where UnitPrice = %s order by Track.Name 
            Limit 500""", (str(price)))
    return display_html(rows) 

@app.route("/timequery/<time>")
def viewtime(time): 
    rows = execute_query ("""select ArtistId, Artist.Name, Track.Name, UnitPrice, Milliseconds
    from Artist JOIN Album using (ArtistID) JOIN Track using (AlbumID)
    WHERE Milliseconds > %s order by Track.Name 
    Limit 500 """, (str(time)))
    return display_html(rows)
from flask import request

from flask import render_template
@app.route("/timequerytextbox", methods = ['GET'])
def price_form():
  return render_template('textbox.html', fieldname = "Milliseconds")


@app.route("/timequerytextbox", methods = ['POST'])
def time_form_post():
  text = request.form['text']
  return viewtime(text)


if __name__ == '__main__': 
    app.run(host = '0.0.0.0', port=8080, debug=True)
