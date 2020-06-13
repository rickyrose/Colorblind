init python:
     import  string

    # variables (do not touch manually) 
    qte_word =  "" 
    next_k =  "" 
    qteTime =  . 0 
    qteMaxTime =  5.0 
    abc =  list (string . Ascii_lowercase)

    # initialization of the game when the screen starts 
    # parameters are passed when the game screen is called 
    # if the word is empty, then a random length is generated length 
    # time is the time allotted for the game in seconds 
    def  qte_init (word = "" , time = 5.0 , length = 5 ):
         global qte_word, next_k, qteMaxTime, qteTime
        qteMaxTime = time
        qteTime = time
        qte_word = word . lower ()
         if word:
            next_k = qte_word [ 0 ]
         else :
             for i in  range ( 0 , length):
                qte_word = qte_word + renpy . random . choice (abc)
                next_k = qte_word [ 0 ]
        renpy . restart_interaction ()
     # pressing the next necessary button, go to the next 
    def  next_key ():
         global qte_word, next_k
        qte_word = qte_word [ 1 :]
        next_k =  "" 
        if qte_word:
            next_k = qte_word [ 0 ]
        renpy . restart_interaction ()
    NextKey = renpy . curry (next_key)
    qteInit = renpy . curry (qte_init)

# game 
screen itself screen scr_qte (word = "" , time = 5.0 , length = 5 ):
     # initialization 
    on 'show' action qteInit (word, time, length)
    modal True 
    if qte_word:
         # reduce the time allotted for the game and check if it doesn’t work out - lose 
        timer 0.01 repeat True action [SetVariable ( "qteTime" , qteTime -  . 01 ), If (qteTime <=  . 0 , true = Return ( False ))]
         # display which button to press 
        text next_k . upper () the align ( . 5 , . 5 ) size 96 
        # if you need something to click, then interrogates the keyboard
        if  len (next_k) ==  1 :
            key next_k action NextKey ()
    else :
         # all buttons pressed - 
        timer wins . 1 action Return ( True )
     # timeline 
    bar StaticValue value (qteTime, qteMaxTime) align ( . 5 , . 1 ) xmaximum 600

