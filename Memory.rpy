Player must turn cards to find pairs (or triplets, quadruplets).
##### The game screen
screen memo_scr:    
    
    ##### Timer
    timer 1.0 action If (memo_timer > 1, SetVariable("memo_timer", memo_timer - 1), Jump("memo_game_lose") ) repeat True
    
    text str(memo_timer) xalign 0.5 yalign 0.05
    
    
    ##### Cards
    #
    # To use images, just comment out lines that show text and uncomment lines that show images
    grid 3 4:
        for card in cards_list:
            button:
                background None

                if card["c_chosen"]:        # shows the face of the card
                    text card["c_value"]    # will show text
                    #add card["c_value"]    # will show image

                else:                       # shows the back of the card
                    text "X"                # will show text
                    #add "C"                # will show image

                action If ( (card["c_chosen"] or not can_click), None, [SetDict(cards_list[card["c_number"]], "c_chosen", True), Return(card["c_number"]) ] )
 

    

init:
    python:
        def cards_shuffle(x):
            renpy.random.shuffle(x)
            return x

    ##### Images
    image A = "img_1.png"         # different card images
    image B = "img_2.png"
    image C = "back.png"          # back of the card

    

    
label memoria_game:
    
    #####
    #
    # At first, let's set the cards to play (the amount should match the grid size - in this example 12)
    $ values_list = ["A", "A", "A", "A", "A", "A", "B",  "B", "B", "B", "B", "B"]
    
    # Then - shuffle them
    $ values_list = cards_shuffle(values_list)
    
    # And make the cards_list that describes all the cards
    $ cards_list = []
    python:
        for i in range (0, len(values_list) ):
            cards_list.append ( {"c_number":i, "c_value": values_list[i], "c_chosen":False} )   

    # Before start the game, let's set the timer
    $ memo_timer = 50.0
    
    # Shows the game screen
    show screen memo_scr
    
    # The game loop
    label memo_game_loop:
        $ can_click = True
        $ turned_cards_numbers = []
        $ turned_cards_values = []
        
        # Let's set the amount of cards that should be opened each turn (all of them should match to win)
        $ turns_left = 3
        
        label turns_loop:
            if turns_left > 0:
                $ result = ui.interact()
                $ memo_timer = memo_timer
                $ turned_cards_numbers.append (cards_list[result]["c_number"])
                $ turned_cards_values.append (cards_list[result]["c_value"])
                $ turns_left -= 1
                jump turns_loop
        
        # To prevent further clicking befor chosen cards will be processed
        $ can_click = False
        # If not all the opened cards are matched, will turn them face down after pause
        if turned_cards_values.count(turned_cards_values[0]) != len(turned_cards_values):
            $ renpy.pause (1.0, hard = True)
            python:
                for i in range (0, len(turned_cards_numbers) ):
                    cards_list[turned_cards_numbers[i]]["c_chosen"] = False
        
        # If cards are matched, will check if player has opened all the cards
        else:
            $ renpy.pause (1.0, hard = True)
            python: 
                
                # Let's remove opened cards from game field
                # But if you prefere to let them stay - just comment out next 2 lines
                for i in range (0, len(turned_cards_numbers) ):
                    cards_list[turned_cards_numbers[i]]["c_value"] = Null()
                    
                    
                for j in cards_list:
                    if j["c_chosen"] == False:
                        renpy.jump ("memo_game_loop")
                renpy.jump ("memo_game_win")
                
                

        jump memo_game_loop

label memo_game_lose:
    hide screen memo_scr
    $ renpy.pause (0.1, hard = True)
    $ renpy.pause (0.1, hard = True)
    "You lose! Try again."
    jump memoria_game

label memo_game_win:
    hide screen memo_scr
    $ renpy.pause (0.1, hard = True)
    $ renpy.pause (0.1, hard = True)
    "You win!"
    return
