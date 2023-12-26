from flask import Flask, render_template, request

from main import validate_word, noun_tags, adj_tags, verb_tags
# from main import 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])

def process():

    while True:
        noun = request.form['user_input']
        if validate_word(noun, noun_tags):
            valid_message = f"Valid noun entered: {noun}"
            return render_template('index.html', valid_message=valid_message)
        else:
            return "Not a valid noun. Please enter a noun."

# while True:
#     verb = input("Enter a verb: ")
#     if validate_word(verb, verb_tags):
#         print("Valid verb entered:", verb)
#         break
#     else:
#         print("Not a valid verb. Please enter a verb.")

# while True:
#     adjective = input("Enter an adjective: ")
#     if validate_word(adjective, adj_tags):
#         print("Valid adjective entered:", adjective)
#         break
#     else:
#         print("Not a valid adjective. Please enter an adjective.")
    
if __name__ == '__main__':
    app.run(debug=True)     
