#This is a hidden object mini-game # save this code to the game.rpy file in the root of the game

# Called something like this:

# $ InitGame ("bg_room", 5.0, True, (735, 300), "figure1", (640, 226), "figure2", (288, 38), "figure3", (115, 260), "figure4 ") 
# $ StartGame ()

# where bg_room is the name of the background file without specifying the extension .jpg 
# 5.0 - the number of seconds to search 
# if <= 0, the timer is off, you can take only one item, it will be saved in oRes 
# (735, 300), "figure1" - coordinates and file name of the item 
# without the extension .png 
# items can be any number 
# all backgrounds and pictures of the items must be in the images folder 
# in oRes - true or false (laid out in the allotted time or not) - or the name of the item 
# number of items found in oLen variable 
# total number of items in maxLen variable

# $ GameAsBG () # shows a screen with pictures as a background, not clickable

# in the sounds folder, the sound should be “click.mp3” 
# or, if it is not, then you need to comment out the line: 
# renpy.play ("sounds / click.mp3", channel = "sound")

init python:
    # a window in the center of the screen 
    import  os 
    os . environ [ 'SDL_VIDEO_CENTERED' ] =  '1' 
    # automatic declaration of 
    config sprites . automatic_images_minimum_components =  1 
    config . automatic_images = [ '' , '_' , '/' ]
    config . automatic_images_strip = [ "images" ]
    oXY = []
    oN = []
    oLen =  0 
    maxLen =  0 
    oBg =  "" 
    oLast =  - 1 
    oTime =  0.0 
    oMaxTime =  5.0 
    needTimer =  False 
    oActive =  False 
    oRes =  False

    # Initializing the game, placing items on the screen 
    def  InitGame (bg, time, * args):
         global oBg, oXY, oN, oLen, maxLen, oLast, oTime, oMaxTime, oActive, needTimer, oRes
        oXY = []
        oN = []
        oLen =  0 
        oBg = bg
        oLast =  - 1 
        oTime = time
        oMaxTime = time
        maxLen =  0 
        oActive =  True 
        oRes =  False 
        if oTime >  0.0 :
            needTimer =  True 
        for xy, obj_name in  zip (args [ 0 :: 2 ], args [ 1 :: 2 ]):
            oXY . append (xy)
            oN . append (obj_name)
            maxLen + =  1

    # Launching the game 
    def  StartGame ():
         global oActive
        oActive =  True 
        need =  True 
        while need:
            renpy . call_screen ( "game" , _layer = "master" )
            need = oRes ==  False 
            if needTimer and (oTime <=  . 0 ):
                need =  False

    # Show the game screen as an inactive background 
    # Items already found will not be displayed 
    def  GameAsBG ():
         global oActive
        oActive =  False 
        renpy . show_screen ( "game" , _layer = "master" )

    # The click handler on the subject 
    def  o_click (i):
         global oLen, oRes
         if i > =  0 :
             if oN [i]:
                temp = oN [i]
                oN [i] =  "" 
                oLen + =  1 
                renpy . play ( "sounds / click.mp3" , channel = "sound" )
                renpy . restart_interaction ()
                 if needTimer:
                     if oLen > = maxLen:
                        oRes =  True 
                else :
                    oRes = temp
    oClick = renpy . curry (o_click)

# Actually the game screen, run from the StartGame () function
screen game:
    modal True 
    if oActive and needTimer:
        timer 0.01 repeat True action [SetVariable ( "oTime" , oTime -. 01 ), If (oTime <=  . 0 , true = [Return ()])]
    add oBg
    for i in  range ( 0 , len (oN)):
         if oN [i]:
            imagebutton:
                focus_mask True
                pos (oXY [i])
                idle oN [i]
                hover oN [i]
                # you can duplicate pictures of objects, 
                # naming them "images / object_name_hover.png" 
                # and highlighting them in a graphical editor 
                # and replacing the line above with the line below 
                # then when you hover, they will be highlighted 
                # hover oN [i] + "hover" 
                if oActive:
                    action [oClick (i), Return ()]
                else :
                    action []
    if oActive and needTimer:
         # if oTime> .1: 
            # text "[oTime]" align (.1, .1) size 48 
        # else: 
            # text "0.0" align (.1, .1) size 48
        bar value StaticValue (oTime, oMaxTime):
            align ( . 5 , . 001 )
            xmaximum 400 
            ymaximum 20 
            left_bar Frame ( "slider_left.png" , 10 , 10 )
            right_bar Frame ( "slider_right.png" , 10 , 10 )
            thumb None 
            thumb_shadow None
