from flask import Flask, request, render_template, redirect, flash
import mysql.connector

app = Flask(__name__)
app.config['SECRET_KEY'] = 'pmtgames'

#define a route to the index.html file
@app.route('/', methods=["POST", "GET"])
def index():
    if request.method == "POST":
        guess = request.form["guess"]

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

        flash(f"Your guess is {guess}!!", category="success")
        print(f"Your guess is {guess}")

    return render_template('index.html')


# @app.route('/submit_guess', methods=['POST'])
# def submit_guess():
#     if request.methods == 'POST':
#         guess = request.form['guess']

#     # Connect to the MySQL database
#     cnx = mysql.connector.connect(user='sqluser', password='password',
#                                   host='localhost', database='guesses')
#     cursor = cnx.cursor()

#     # Insert the guess into the database
#     query = "INSERT INTO guesses (guess) VALUES (%s)"
#     cursor.execute(query, (guess,))
#     cnx.commit()

#     # Close the database connection
#     cursor.close()
#     cnx.close()

#     print("Your guess has been recorded")
    
#     # redirect the user back to index.html
#     return redirect('/')

if __name__ == '__main__':
    app.run(debug=True, port=5500)

