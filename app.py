import random
from flask import Flask, render_template, request

from main import validate_word, noun_tags, adj_tags, verb_tags

app = Flask(__name__)


# stories = [
#     'Cosplayer is where the {adjective} Elden Ring {noun} {verb} across the field.',
#     'Otaku would {verb} that this {noun} called Naruto was the {adjective} ever.',
#     'Psychologically as an anime enjoyer, {noun} fan\'s point of view... {verb} is the {adjective} achievement!',
# ]

stories = [
    "Jujutsu Kaisen follows {noun} {adjective} students {verb} curses and their powers.",
    "Dr. Stone portrays a world where {noun} {verb} to rebuild civilization after a {adjective} event.",
    "Jujutsu Kaisen introduces a {adjective} {noun} who {verb} to control cursed energy.",
    "{verb} Shippuden delves into the {adjective} {noun} of a young ninja's growth.",
    "A {adjective} cat psychic {noun} who {verb} evil spirits in Mob Psycho the anime style.",
    "Envision the {adjective} cat-and-mouse game between a detective and a {noun} who {verb} death through Death Note the anime style"
]


@app.route('/')
def index():
    return render_template('index.html')

# Route to handle the form submission for word validation
@app.route('/validation', methods=['POST'])

def validate_words():
    noun = request.form['noun_input']
    adjective = request.form['adj_input']
    verb = request.form['verb_input']

    nounContext= f"{noun} went to the really big store"
    adjectiveContext = f"Tom went to the really {adjective} store"
    verbContext = f"Tom {verb} to the really big store"
    
    # print(f"Here is the nounContext: {nounContext.split()[0]}")
    # print(f"Here is the adjectiveContext: {adjectiveContext.split()[5]}")
    # print(f"Here is the verbContext: {verbContext.split()[1]}")

    valid_noun = validate_word(nounContext.split()[0], noun_tags)
    valid_adjective = validate_word(adjectiveContext.split()[5], adj_tags)
    valid_verb = validate_word(verbContext.split()[1], verb_tags)
    
    # print(valid_noun)
    # print(valid_adjective)
    # print(valid_verb)
    
    # stories = [

    #     f'{noun} is where the {adjective} Elden Ring player {verb} across the field',

    #     f'{noun} would {verb} that this anime called Naruto was the {adjective} ever', 

    #     f'Psychologically as an anime enjoyer, {noun}\'s point of view... {verb} is the {adjective} achievement!'
    # ]

    randomStory = random.choice(stories)

    return render_template('index.html', valid_noun=valid_noun, valid_verb=valid_verb, valid_adjective=valid_adjective,
                           noun=noun, verb=verb, adjective=adjective, randomStory=randomStory )


if __name__ == '__main__':
    app.run(debug=True)     
