from flask import Flask
from flaskext.mysql import MySQL
from flask import jsonify
app = Flask(__name__)


mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'

app.config['MYSQL_DATABASE_DB'] = 'flaskapi'
mysql.init_app(app)
conn = mysql.connect()
cursor = conn.cursor()


@app.route("/books")
def getAllBooks():
    query = cursor.execute("SELECT * FROM books")
    #head_rows = cursor.fetchmany(size=2)
    #return "Hello World!" + str(query)
    return jsonify(cursor.fetchall())

@app.route('/books/<id>', methods=['GET'])
def getOneBook(id):
    #myArray = []
    bookID = id
    bookFound = ""
    #bookTotal = cursor.execute("SELECT * FROM books")
    query = cursor.execute("SELECT * FROM books WHERE id=" + bookID)
    allBooks = jsonify(cursor.fetchone())

    return allBooks


    #query = cursor.execute("SELECT * FROM books")
    #head_rows = cursor.fetchmany(size=2)
    #return "Hello World!" + str(query)
    #return jsonify(myArray)
    #return jsonify(bookFound)
@app.route('/books/<id>', methods=['DELETE'])
def deleteBook(id):
    bookID = id
    query = cursor.execute("DELETE FROM books WHERE id=" + bookID)
    #Create an return message if delete was sucessfull

if __name__ == "__main__":
    app.run()
