

#? imports for Language Processing

import random
import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('tagsets')
nltk.download('averaged_perceptron_tagger')

# ~ ------------------------------------------------------- ~
# ~ ------------------------------------------------------- ~

#? word validation (will need imports, following resource links)

def validate_word(word, valid_tags):
    chosen_words = [[word]]
    word_tag = nltk.pos_tag(chosen_words[0])

    if any(tag[1] in valid_tags for tag in word_tag):
        return True
    else:
        return False
    
    
#? The tags are shown by the ntlk, on the documentation it can be found when using a function

noun_tags = ["NN", "NNP", "NNPS", "NNS"]
verb_tags = ["VB", "VBD", "VBG", "VBN", "VBP", "VBZ"]
adj_tags = ["JJ", "JJR", "JJS"]




#? each While loop will keep running until the user puts in the right Part of Speech

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



#? Here is where we input the stories that we want users to randomly receive with their own words selected 

stories = [

        f'{noun} is where the {adjective} Elden Ring player {verb} across the field',

        f'{noun} would have {verb} that this anime called Naruto was the {adjective} ever', 

        f'Psychologically, from the {noun}\'s point of view... {verb} is the {adjective} achievement!'
    ]

#? Here wwe choose a random story from the list



randomStory = random.choice(stories)

#? Here we display the random story to the user

print(f"Here is a random story: {randomStory}")

#test































#? use an array : How to generate random stories?


#? Do we need a Front end ( HTML & CSS ) for this or do we keep this at just a terminal?