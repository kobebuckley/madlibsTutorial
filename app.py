import random
from flask import Flask, render_template, request
from main import validate_sentence
from openai import OpenAI # pip install openai

app = Flask(__name__)

@app.route('/')

def index():
    return render_template('index.html')

# Route to handle the form submission for word validation
@app.route('/story-val', methods=['POST'])

def validate_words():

    # all input, including space, can mess up the validation
    # changing case, as it affects what the POS states a word as (such as lowercase adj properly, instead of as a noun when capitalized)
    noun = request.form['noun_input']
    adjective = request.form['adj_input']
    verb = request.form['verb_input']

    noun = noun.capitalize()
    adjective = adjective.lower()
    verb = verb.lower()

    #? This is a placeholder sentence to ensure that the user words are given correct Parts of Speech tags.
    sentence = f"{noun} {verb} to the really {adjective} store"

    validation_sentence = validate_sentence(sentence)
    print(f"Here is the validate sentence: {validate_sentence}")

    valid_noun = validation_sentence[0]
    valid_adjective = validation_sentence[1]
    valid_verb = validation_sentence[2]

    stories = [
        # f"anime art style, darkcore aesthetic, a nameless {noun} is {verb} alone in a {adjective} room and pondering life, he must confront his own demons in order to save the world, grim, dark, peculiar",
        f"In the stylish world of 'Cowboy Bebop,' a brooding {noun} Spike Spiegel {verb} {adjective} alone in a dimly lit room, reflecting on his past, haunted by ghosts, battling inner turmoil.",
        f"Within the haunting ambiance of 'Death Note,' a {adjective} Light Yagami {verb} silently in a {adjective} chamber, plotting fateful moves, wrestling with the abyss, chasing forbidden power."
        # f"Embracing the whimsy of 'My Neighbor Totoro,' a curious Totoro playfully frolics in a cozy forest, lost in thought, cherishing serene moments, seeking solace in simplicity, and {noun} is {verb} within a {adjective} time."
        # f"In the enchanting world of 'Sailor Moon,' a determined Usagi Tsukino gazes into the moonlit night alone, contemplating destiny, summoning courage, embracing the cosmic order."
        # f"Amidst the cyberpunk vibe of 'Ghost in the Shell,' a contemplative Major Motoko Kusanagi stands stoically in a futuristic room, pondering existence, questioning reality, lost in a sea of data."
        # f"Immersed in the captivating 'Attack on Titan' universe, a conflicted Eren Yeager paces in a grim chamber, battling inner turmoil, haunted by past traumas, driven by vengeance."
        # f"Within the vibrant world of 'Naruto,' a determined Naruto Uzumaki stands resiliently in a sunlit room, dreaming of becoming Hokage, facing trials, seeking validation and acceptance."
        # f"In the mystical aura of 'Spirited Away,' a curious Chihiro lingers in a mysterious chamber, embracing the surreal, confronting spirits, seeking to break the curse, hoping for salvation."
        # f"Amidst the medieval setting of 'Berserk,' a tormented Guts sits solemnly in a dark chamber, burdened by destiny, battling demons, seeking retribution in a cruel world."
        # f"In the whimsical world of 'One Piece,' a determined Monkey D. Luffy stands boldly in a vibrant room, dreaming of becoming Pirate King, confronting challenges, chasing freedom and adventure."
       
       
        # f"Dr. Stone portrays a world where {noun} {verb} to rebuild civilization after a {adjective} event in an anime stlye.",
        # f"Jujutsu Kaisen follows {noun} {adjective} students {verb} curses and their powers in an anime stlye.",
        # f"Jujutsu Kaisen introduces a {adjective} {noun} who {verb} to control cursed energy in an anime stlye.",
        # f"Jujutsu Kaisen introduces a {adjective} {noun} who {verb} to control cursed energy in Attack on Titan the anime stlye.",
        # f"{verb} Shippuden delves into the {adjective} {noun} of a young ninja's growth in an anime stlye.",
        # f"A {adjective} cat psychic {noun} who {verb} evil spirits in the anime style of Mob Psycho.",
        # f"Envision the {adjective} cat-and-mouse game between a detective and a {noun} who {verb} death through Death Note in an anime stlye"
        ]

    randomStory = random.choice(stories)

    error_messages = []

    if not valid_noun:
        error_messages.append("Not a valid noun. Please try again.")
    if not valid_adjective:
        error_messages.append("Not a valid adjective. Please try again.")
    if not valid_verb:
        error_messages.append("Not a valid verb. Please try again.")

    # needs api key to function, also will need dot env to hide the key 
    # client = OpenAI() 

    # response = client.images.generate(
    # model="dall-e-3",
    # prompt=randomStory,
    # size="1024x1024",
    # quality="standard",
    # style="vivid",
    # n=1,
    # )

    # image_url = response.data[0].url
    image_url = '/static/placeholder1.png'  # Adjust the path accordingly


    # Prompt is revised by Dalle 3, maybe can aim to make the revised prompt as close to original as possible
    
    # print(response.data)

    if error_messages:
        return render_template('index.html', error_messages=error_messages)
    else:
       return render_template('index.html', valid_noun=valid_noun, valid_verb=valid_verb, valid_adjective=valid_adjective,
                            noun=noun, verb=verb, adjective=adjective, randomStory=randomStory, image_url=image_url)
                            
if __name__ == '__main__':
    app.run(debug=True)     
