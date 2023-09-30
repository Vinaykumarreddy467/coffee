from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

# MySQL Configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'MIKEALSON',
    'database': 'COFFEE',
}

@app.route('/')
def index():
    # Connect to MySQL database
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()

    # Execute a query to fetch data
    query = "SELECT * FROM coffee"
    cursor.execute(query)

    # Fetch all the data
    data = cursor.fetchall()

    # Close the database connection
    cursor.close()
    connection.close()

    # Render the template with the data
    return render_template('disc-method.html', data=data)

if __name__ == '__main__':
    app.run(debug=True,port=5001)
