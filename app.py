from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        number = request.form['number']
        with open('data.txt', 'a') as f:
            f.write(number + '\n')
        return f'Thank you for submitting {number}!'
    else:
        return '''
            <form method="post">
              <label for="number">Number:</label>
              <input type="number" name="number" id="number" min="1" max="100" required>
              <br><br>
              <button type="submit">Submit</button>
            </form>
        '''

if __name__ == '__main__':
    app.run(debug=True)
