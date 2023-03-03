from flask import Flask, request
import mysql.connector

app = Flask(__name__)

@app.route('/submit_guess', methods=['POST'])
def submit_guess():
    guess = request.form['guess']

    # Connect to the MySQL database
    cnx = mysql.connector.connect(user='sqluser', password='password',
                                  host='localhost', database='guesses')
    cursor = cnx.cursor()

    # Insert the guess into the database
    query = "INSERT INTO guesses (guess) VALUES (%s)"
    cursor.execute(query, (guess,))
    cnx.commit()

    # Close the database connection
    cursor.close()
    cnx.close()

    return "Your guess has been recorded!"

if __name__ == '__main__':
    app.run(debug=True)

