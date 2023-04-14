#import the relevant stuff.
from flask import render_template, request, Flask, g
import sqlite3

#app setup
app = Flask(__name__)

def get_db() :
    #connect to the database
    g.db = sqlite3.connect('instance/database.db')

    #this tells the session how to extract rows from the database. sqlite3.Row  will return rows that behave like dictionaries.
    g.db.row_factory = sqlite3.Row

    #Create the main table if it doesn't exist.
    g.db.execute('CREATE TABLE IF NOT EXISTS names(name TEXT)')

    return g.db

#Tell flask to close the db when the app has finished running
@app.teardown_appcontext
def close_db(exception):
    db = g.pop('db', None)

    if db is not None:
        db.close()

@app.route('/', methods=('GET', 'POST'))
def index():
    
    db = get_db()

    if request.method == 'POST':
        db.execute('INSERT INTO names VALUES (?)', (request.form['name'],))
        
        #write changes to db.
        db.commit()

    #get all names from the database and pass them to the template.
    names = db.execute('SELECT * FROM names').fetchall() 

    return render_template('index.html', names=names)

if __name__ == '__main__':
    index()
