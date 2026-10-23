
import random

templates = [
    {
        "text":  "A :adjective ghost is :adverb behind you!",
        "author": "rtoal"
    },
    {
        "text": "The :color :noun is :verb at you!",
        "author": "rbettis"
    },
    { 
        "text": "The mysterious :noun lies :preposition ground!",
        "author": "rbettis"
    },
    {
        "text": "Behold the :adverb :adjective of :noun!",
        "author": "rbettis"
    },
    {
        "text": "Hike to the :noun where the :color :flower is.",
        "author": "rbettis"
    },
    {
        "text": "The brave :noun :verb the :adjective :adverb.",
        "author": "rbettis"
    },
    {
        "text": "Long ago, :noun :verb the world, discovering :place.",
        "author": "rbettis"
    },
    {
        "text": "The :adverb :adjective :noun :verb his :animal.",
        "author": "rbettis"
    },
    {
        "text": "He :verb his :noun :adverb.",
        "author": "rbettis"
    },
    {
        "text": "The :noun struck the :place with :adjective :weapon",
        "author": "rbettis"
    }
    
    
]

yes_answers = {"yes", "si", "oui", "yup", "bet", "yep", "y"}





while True:
     provided_words = {}
     current_template = random.choice(templates)
     words = (current_template["text"]).split()
 
 
   
     for word in words:
        if word.startswith(":"):
            response=input(f"Provide word that fits description {word}").strip().lower()
            while not (1 <= len(response) <= 30):
                response=input("Try Again.")

            provided_words[word] = response

     user_sentence = current_template["text"]

     for word in provided_words:
         user_sentence = user_sentence.replace(word, provided_words[word]).strip().lower()

     print(user_sentence)
     print()
     print(f"Sentence Template by {current_template['author']}")
     print()
     print()
     response=input("Would you like to play again?").strip().lower()
     if response==("no"):
         print("Thanks for playing!")
         break
     elif response in yes_answers:
         continue
   







  

  
  


