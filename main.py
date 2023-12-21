# note. alias python=python3 

# imports
import random
import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt')
nltk.download('tagsets')
nltk.download('averaged_perceptron_tagger')


# noun
noun = input("Enter a noun: ")

# verbs
verb = input("Enter a verb: ")

# adjectives
adjective = input("Enter an adjective: ")

# Printing out sentences 

#? how to insert dynamic variables into string

# chosenWords = f"The words you have chosen are {noun}, {verb}, and {adjective}."

chosenWords = [[noun], [verb], [adjective]]


print(chosenWords)

#! user input: How to ask the user for words?


    #? do we need to check that user enters a proper noun, verb, or adjective? And if so we tell them? 
        # ! This would use NLP 

        # first we install NLP (might need to install pip first!)


# words_in_chosenWords = word_tokenize(chosenWords)

nounTag = nltk.pos_tag(chosenWords[0])
print(f"noun tagged here: {nounTag}")

# chosenNoun = word_tokenize(noun)

chosenVerb = nltk.pos_tag(verb)
chosenAdjective = nltk.pos_tag(adjective)

# print(chosenNoun)
#! nltk.help.upenn_tagset()

        #? After we get a confirmation on what type of word this is, how do we then do certain actions based on that information
if (nounTag[0][1] == "NN"):
    print("NN")
else:
    print("Hmm thats not a noun!!!")
    while (nounTag[0][1] != "NN"):
        chosenWords[0] = input(f"Enter a REAL noun: {chosenWords[0]}")
    





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