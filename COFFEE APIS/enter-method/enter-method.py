from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# Configure MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="MIKEALSON",
    database="coffee"
)

@app.route('/')
def index():
    return render_template('entry-method.html')

@app.route('/submit', methods=['POST'])
def submit():
    item = request.form['item']
    SNO = request.form['SNO']
    price = request.form['price']

    cursor = db.cursor()
    cursor.execute("INSERT INTO COFFEE (SNO,ITEM, PRICE) VALUES (%s,%s, %s)", (SNO , item, price))
    db.commit()

    return 'Item added successfully!'

if __name__ == '__main__':
    app.run(debug=True, port =5002)
