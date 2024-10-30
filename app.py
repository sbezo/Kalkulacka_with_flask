from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        try:
            # Retrieve numbers from form input, add them, and store in 'result'
            num1 = float(request.form['num1'])
            num2 = float(request.form['num2'])
            result = num1 + num2
        except ValueError:
            result = "Invalid input"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)