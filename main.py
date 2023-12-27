
#? imports for Language Processing

import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('tagsets')
nltk.download('averaged_perceptron_tagger')

# ~ ------------------------------------------------------- ~
# ~ ------------------------------------------------------- ~

#? word validation (will need imports, following resource links)

def validate_word(word, valid_tags):
    return word in valid_tags

def validate_sentence(sentence):
    tagged = nltk.pos_tag(word_tokenize(sentence))

    print(f"tagged here: {tagged}")

    valid_noun = validate_word(tagged[0][1], noun_tags)
    print(f"noun tagged here: {valid_noun}")

    valid_adjective = validate_word(tagged[5][1], adj_tags)
    print(f"adjective tagged here: {valid_adjective}")

    valid_verb = validate_word(tagged[1][1], verb_tags)
    print(f"verb tagged here: {valid_verb}")
    
    return valid_noun, valid_adjective, valid_verb

#? The tags are shown by the ntlk, on the documentation it can be found when using a function

noun_tags = ["NN", "NNP", "NNPS", "NNS"]
adj_tags = ["JJ", "JJR", "JJS"]
verb_tags = ["VB", "VBD", "VBG", "VBN", "VBP", "VBZ"]

#? each While loop will keep running until the user puts in the right Part of Speech

# while True:
#     noun = input("Enter a noun: ")
#     if validate_word(noun, noun_tags):
#         print("Valid noun entered:", noun)
#         break
#     else:
#         print("Not a valid noun. Please enter a noun.")

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



#? Here is where we input the stories that we want users to randomly receive with their own words selected 


# stories = [

#         f'{noun} is where the {adjective} Elden Ring player {verb} across the field',

#         f'{noun} would have {verb} that this anime called Naruto was the {adjective} ever', 

#         f'Psychologically, from the {noun}\'s point of view... {verb} is the {adjective} achievement!'
#     ]

#? Here we choose a random story from the list



# randomStory = random.choice(stories)

#? Here we display the random story to the user

# print(f"Here is a random story: {randomStory}")

































#? use an array : How to generate random stories?


#? Do we need a Front end ( HTML & CSS ) for this or do we keep this at just a terminal?