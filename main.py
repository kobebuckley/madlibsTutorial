# note. alias python=python3 

# imports
import random
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
from nltk.tokenize import word_tokenize

#! user input: How to ask the user for words?


    #? do we need to check that user enters a proper noun, verb, or adjective? And if so we tell them? 
        # ! This would use NLP 

        # first we install NLP (might need to install pip first!)

# using the quote provided from docs to test 

sagan_quote = """
... If you wish to make an apple pie from scratch,
... you must first inventing the universe."""

words_in_sagan_quote = word_tokenize(sagan_quote)
test = nltk.pos_tag(words_in_sagan_quote)

print(test)

        #? After we get a confirmation on what type of word this is, how do we then do certain actions based on that information

# test 

# userInput = input("Enter something here: ")
# print(userInput)

# noun
noun = input("Enter a noun: ")

# verbs
verb = input("Enter a verb: ")

# adjectives
adjective = input("Enter an adjective: ")

# Printing out sentences 

#? how to insert dynamic variables into string

chosen = f"The words you have chosen are {noun}, {verb}, and {adjective}."

print(chosen)


#! Making a list of stories to randomly choose

    #? How do we make a list of stories / strings?

stories = [

        f'{noun} is where the {adjective} Elden Ring player {verb} across the field',

        f'{noun} would have {verb} that this anime called Naruto was the {adjective} ever', 

        f'Psychologically, from the {noun}\'s point of view... {verb} is the {adjective} achievement!'
    ]

        #? How do we randomize these stories? 

randomStory = random.choice(stories)

print(f"Here is a random story: {randomStory}")

































#? use an array : How to generate random stories?


#? Do we need a Front end ( HTML & CSS ) for this or do we keep this at just a terminal?