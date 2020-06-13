# to call a location with a button on the screen screen, 
# you need to call it in a new context. 
# that is, it opens like a different game. 
# and all the old screens are hiding.

# here only when saving the game, only the place is remembered 
# where the first call was called from, as if all return had already worked 
# so it’s better to disable the save option 
#total: the method works only for all kinds of menus, 
# but not for branching the plot
init python:
    # stack for storing the state of screens until calling call 
    screens = []
     # action on the ESC button 
    gamemenu = config . game_menu_action
     # add another list of screens 
    def  s_push (item):
         global screens
        screens . append (item)
     # retrieve the last list of screens 
    def  s_pop ():
         global screens
         if  len (screens) >  0 :
             return screens . pop ()
         return []
     # starting amount of money to test 
    money =  10 
    # flag for calling a location in a new context 
    is_call =  False 
    # you cannot execute a regular call label from the screen 
    # create its analogue 
    class  MyCall (Action):
         def __init__ ( self , label, * args, ** kwargs):
             self . label = label
             self . args = args
             self . kwargs = kwargs
         def  __call__ ( self ):
             global screens, is_call
             # disable ESC 
            config . game_menu_action = NullAction ()
             # remember 
            s_push (renpy .current_screen () . screen_name)
             # enable the flag to call the new context (to hide the button) 
            is_call =  True 
            # call the location in the new 
            renpy context . call_in_new_context ( self . label, * self . args, ** self . kwargs)
     # function to restore screens in a new context 
    def  show_screens ():
         for i in screens [ - 1 :]:
            renpy . show_screen (i)
     # function to return from a location in a new context 
    def  myreturn ():
         global is_call
         # hide screens 
        for i in s_pop ():
            renpy . hide_screen (i)
         # clear the flag of the new location so that the button for calling it appears again 
        is_call =  len (screens) >  0 
        if  not is_call:
            config . game_menu_action = gamemenu
         # save game 
        renpy data . retain_after_load ()
        Return () ()
    # so that you can bind to the digger, for example 
    MyReturn = renpy . curry (myreturn)

# screen from which you can make a call
screen test:
    text _ ( of str (money) +  "money" ), the align ( . 05 , . 05 )
     # button to show only if you're not call her pressing 
    the if  not is_call:
         # button that performs an analog call label 
        textbutton _ ( "Chit" ) the align ( . 95 , . 05 ) the action MYCALL ( "menu1" )
     the else :
         # call the call from the tag, which has already caused by a call 
        textbutton _ ( "Hint" ) the align ( . 95 ,. 05 ) action MyCall ( "hnt" )

label start:
    show expression "images / bg.jpg"
    show screen test
    "You created a new Ren'Py game." 
    "Add a plot, images and music and send it to the world!" 
    return

# another location from which you can return to the same place in the game 
# if you wish, you can pass parameters when called 
# then you can call it like this: ... action MyCall ("menu1", plus = 100) 
label menu1 (plus = 10 ) :
     # display all screens hidden when calling the location in a new context 
    $ show_screens ()
     # actually some actions 
    $ loop1 =  True 
    # loop until the 3rd button 
    while loop1 is pressed:
        menu:
            "+ [plus]" :
                 $ money + = plus
             "- [plus]" :
                 $ money - = plus
             "Return" :
                 $ loop1 =  False 
    # go back to where we came from, restoring the previous state of affairs 
    # instead of return 
    $ MyReturn () ()
     return

label hnt:
    scene black
    centered "Hint: this is a nested call call from another call." 
    $ MyReturn () ()
     return
