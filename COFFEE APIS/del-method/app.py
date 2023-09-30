from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# Define MySQL connection parameters
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="MIKEALSON",
    database="COFFEE"
)

@app.route('/')
def index():
    return render_template('delete_data.html')

@app.route('/delete', methods=['POST'])
def delete_data():
    # Get data from the form
    data_to_delete = request.form['data_to_delete']

    # Create a cursor object to execute queries
    cursor = db.cursor()

    # Execute the DELETE query
    cursor.execute("DELETE FROM COFFEE WHERE item = %s", (data_to_delete,))

    # Commit the changes
    db.commit()

    # Close the cursor
    cursor.close()

    return "Data deleted successfully!"

if __name__ == '__main__':
    app.run(debug=True,port=5004)
