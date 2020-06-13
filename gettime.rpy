init python:
     import  datetime 
    # start time of the current game session = time of the last 
    persistent check . game_last_time = datetime . datetime . now ()
     # total time in seconds in the game 
    if persistent . gametime is  None :
        persistent . gametime =  0 
    # function to display the current total time in the game 
    def  show_gametime (st, at):
         # how much has passed since the last check 
        t = datetime . datetime . now ()
        dt = t - persistent . game_last_time
         # remember the current time as the time of the last 
        persistent check . game_last_time = t
         # sum the time in the game with the time since the last 
        persistent check . gametime + = dt . total_seconds () # in seconds 
        # translate seconds into hours, minutes, seconds 
        minutes, seconds =  divmod ( int (persistent . gametime), 60 )
        hours, minutes =  divmod (minutes, 60 )
         # translate text into image 
        # with formatting (adding zeros if the number is not double-digit) 
        img = Text ( " % 0 * d : % 0 * d : % 0 * d "  % ( 2 , hours, 2 , minutes, 2 , seconds))
         # output image eventually 
        return statement img, . 1
init:
    # bind the function to a dynamic image, 
    # so that the counter ticks without updating the screens 
    image gametime = DynamicDisplayable (show_gametime)

screen scr_game_time:
    # The same line can be added to the main menu: 
    the add "gametime" the align ( . 95 , . 05 )

# to reset the time in the game: 
# $ persistent.gametime = 0 
# or attach to the button: 
# textbutton _ ("Reset time") action SetField (persistent, "gametime", 0)

# The game starts here.
label start:
    show screen scr_game_time
    "The text of the game." 
    return
