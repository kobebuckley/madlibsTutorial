
# imports
import random
import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('tagsets')
nltk.download('averaged_perceptron_tagger')

# ~ ------------------------------------------------------- ~
# ~ ------------------------------------------------------- ~

def validate_word(word, valid_tags):
    chosen_words = [[word]]
    word_tag = nltk.pos_tag(chosen_words[0])

    if any(tag[1] in valid_tags for tag in word_tag):
        return True
    else:
        return False

noun_tags = ["NN", "NNP", "NNPS", "NNS"]
verb_tags = ["VB", "VBD", "VBG", "VBN", "VBP", "VBZ"]
adj_tags = ["JJ", "JJR", "JJS"]

while True:
    noun = input("Enter a noun: ")
    if validate_word(noun, noun_tags):
        print("Valid noun entered:", noun)
        break
    else:
        print("Not a valid noun. Please enter a noun.")

while True:
    verb = input("Enter a verb: ")
    if validate_word(verb, verb_tags):
        print("Valid verb entered:", verb)
        break
    else:
        print("Not a valid verb. Please enter a verb.")

while True:
    adjective = input("Enter an adjective: ")
    if validate_word(adjective, adj_tags):
        print("Valid adjective entered:", adjective)
        break
    else:
        print("Not a valid adjective. Please enter an adjective.")


stories = [

        f'{noun} is where the {adjective} Elden Ring player {verb} across the field',

        f'{noun} would have {verb} that this anime called Naruto was the {adjective} ever', 

        f'Psychologically, from the {noun}\'s point of view... {verb} is the {adjective} achievement!'
    ]

randomStory = random.choice(stories)

print(f"Here is a random story: {randomStory}")

































#? use an array : How to generate random stories?


#? Do we need a Front end ( HTML & CSS ) for this or do we keep this at just a terminal?