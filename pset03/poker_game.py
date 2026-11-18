import cards




while True:
    number_of_players = 0
    number_of_players=input("Please enter a number of players between 2-10").strip().lower()
    if number_of_players in ("bye", "exit"):
      break
    else:
        try:
         number_of_hands=int(number_of_players)
         if number_of_hands > 10 or number_of_hands < 2:
          print("Number is too high or too low")
         elif 2 <= number_of_hands <= 10:
           hands=cards.deal(number_of_hands, 5)
           for hand in hands: 
              classification = cards.poker_classification(hand)
              cards_strings=[]
              for card in hand:
                 cards_strings.append(str(card))
         
              cards_text = " ".join(cards_strings)
              print (""f"{cards_text} is a {classification}")


             
        except ValueError:
         print("Please re-enter a valid number of players between 2-10")
        continue
     
    


  
    