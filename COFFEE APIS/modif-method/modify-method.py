from flask import Flask, render_template, request
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="MIKEALSON",
    database="COFFEE"
)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('modify_data.html')

@app.route('/modify', methods=['POST'])
def modify_data():
    item = request.form['item']
    price = request.form['price']

    # Modify the data in the database based on item and price
    cursor = db.cursor()
    cursor.execute("UPDATE coffee SET price = %s WHERE item = %s", (price, item))
    db.commit()
    cursor.close()

    return "Data Modified Successfully"

if __name__ == '__main__':
    app.run(debug=True,port = 5003 )
