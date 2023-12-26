from flask import Flask, render_template, request

from main import validate_word, noun_tags, adj_tags, verb_tags
# from main import 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
# Route to handle the form submission for word validation

@app.route('/validation', methods=['POST'])
def validate_words():
    noun = request.form['noun_input']
    verb = request.form['verb_input']
    adjective = request.form['adj_input']

    valid_noun = validate_word(noun, noun_tags)
    valid_verb = validate_word(verb, verb_tags)
    valid_adjective = validate_word(adjective, adj_tags)

    print(valid_adjective, valid_verb, valid_noun)
    return render_template('index.html', valid_noun=valid_noun, valid_verb=valid_verb, valid_adjective=valid_adjective,
                           noun=noun, verb=verb, adjective=adjective)

if __name__ == '__main__':
    app.run(debug=True)     
