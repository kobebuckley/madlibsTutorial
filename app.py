from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    user_input = request.form['user_input']  # Fetching user input from the form
    # Process the user input here (perform operations, calculations, etc.)
    print(f"Received user input: {user_input}")
    # You can return a response or redirect as per your application's logic
    return "Data received!"

if __name__ == '__main__':
    app.run(debug=True)
