init python:
     # functions from 7dots.rpy file
    images_auto ()
    window_center ()
    money =  100 
    # stroke 
    style . default . outlines = [( 2 , "# 0008" , 0 , 0 ), ( 1 , "# 0008" , 0 , 0 )]

    # action for entering and checking cheats 
    def  call_input ():
        code =  input ( "Enter code:" )
         if code ==  "1234" :
             global money
            money + =  100 
            message ( "You conjured 100 money." )
         elif code is  None :
            message ( "You pressed cancel." )
         else :
            message ( "Password is incorrect." )
    CallInput = renpy . curry (call_input)

# this screen is waiting for the tab button to be pressed 
screen cheat:
    key "K_TAB" the action CallInput ()
     # indicator denyuzhek 
    frame the align ( . 95 , . 05 ) background Used "# 0008" :
        text "$ [money]" color "# dd4" size 48

# The game starts here.
label start:
    scene bg
    show neko with dissolve
     # show a screen that catches the cheat button
    show screen cheat
    "Press TAB to enter the cheat code. And enter" 1234. " 
    "The game is over." 
    return

