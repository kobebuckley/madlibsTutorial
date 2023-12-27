import random
from flask import Flask, render_template, request

from main import validate_word, noun_tags, adj_tags, verb_tags

app = Flask(__name__)

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
    
    stories = [

        f'{noun} is where the {adjective} Elden Ring player {verb} across the field',

        f'{noun} would {verb} that this anime called Naruto was the {adjective} ever', 

        f'Psychologically as an anime enjoyer, {noun}\'s point of view... {verb} is the {adjective} achievement!'
    ]

    randomStory = random.choice(stories)

    return render_template('index.html', valid_noun=valid_noun, valid_verb=valid_verb, valid_adjective=valid_adjective,
                           noun=noun, verb=verb, adjective=adjective, randomStory=randomStory )


if __name__ == '__main__':
    app.run(debug=True)     
