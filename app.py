import random
from flask import Flask, render_template, request
from main import validate_sentence

app = Flask(__name__)

@app.route('/')

def index():
    return render_template('index.html')

# Route to handle the form submission for word validation
@app.route('/story-val', methods=['POST'])

def validate_words():

    noun = request.form['noun_input']
    adjective = request.form['adj_input']
    verb = request.form['verb_input']

    #? This is a placeholder sentence to ensure that the user words are given correct Parts of Speech tags.
    sentence = f"{noun} {verb} to the really {adjective} store"

    validation_sentence = validate_sentence(sentence)

    valid_noun = validation_sentence[0]
    valid_adjective = validation_sentence[1]
    valid_verb = validation_sentence[2]

    stories = [
        f"Jujutsu Kaisen follows {noun} {adjective} students {verb} curses and their powers.",
        f"Dr. Stone portrays a world where {noun} {verb} to rebuild civilization after a {adjective} event.",
        f"Jujutsu Kaisen introduces a {adjective} {noun} who {verb} to control cursed energy.",
        f"{verb} Shippuden delves into the {adjective} {noun} of a young ninja's growth.",
        f"A {adjective} cat psychic {noun} who {verb} evil spirits in Mob Psycho the anime style.",
        f"Envision the {adjective} cat-and-mouse game between a detective and a {noun} who {verb} death through Death Note the anime style"]

    randomStory = random.choice(stories)

    error_messages = []

    if not valid_noun:
        error_messages.append("Not a valid noun. Please try again.")
    if not valid_adjective:
        error_messages.append("Not a valid adjective. Please try again.")
    if not valid_verb:
        error_messages.append("Not a valid verb. Please try again.")

    if error_messages:
        return render_template('index.html', error_messages=error_messages)
    else:
       return render_template('index.html', valid_noun=valid_noun, valid_verb=valid_verb, valid_adjective=valid_adjective,
                            noun=noun, verb=verb, adjective=adjective, randomStory=randomStory)
if __name__ == '__main__':
    app.run(debug=True)     
