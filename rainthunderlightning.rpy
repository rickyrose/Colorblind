init python:
     # can be
     done with the standard Animation function, # but asked with this: 
    def  Ani (img_name, frames, delay =. 1 , loop = True , reverse = True , effect = None , start = 1 , ext = "png" , ** properties):
        args = []
         for i in  range (start, start + frames):
            args . append (renpy . display . im . image (img_name +  str (i) +  "."  + ext))
             if reverse or loop or (i < start + frames -  1 ):
                args . append (delay)
                args . append (effect)
         if reverse: # reverse animation if needed 
            for i in  range (start + frames -  2 , start, - 1 ):
                args . append (renpy . display . im . image (img_name +  str (i) +  "."  + ext))
                 if loop or (i > start +  1 ):
                    args . append (delay)
                    args . append (effect)
         return anim . TransitionAnimation ( * args, ** properties)
     # time of appearance / decay of sounds 
    fade_time =  1.0 
    # register channels so that sounds do not interrupt each other 
    channels = [ "rain" , "thunder1" , "thunder2" , "thunder3" ]
     for i in channels:
        renpy . music . register_channel (i, "sfx" , True )
     # play sounds on our channels 
    # or on the sound channel if the desired channel is not registered 
    def  splay (name, channel = None , loop = False , fadein = fade_time, fadeout = fade_time):
         if  not channel in channels:
            channel =  None 
        if channel is  None :
             if name in channels:
                channel = name
             else :
                channel =  "sound" 
        fn =  "sounds /"  + name +  ".ogg" 
        renpy . music . play (fn, channel = channel, loop = loop, fadeout = fadeout, fadein = fadein)
     # gradually stop the sounds or one sound if the input is not a 
    def  sstop list (channel = channels, fadeout = fade_time):
         if  isinstance (channel, list ):
             for i in channel:
                renpy . music . stop (i, fadeout = fadeout)
         else :
            renpy . music . stop (channel, fadeout = fadeout)
     # new lightning position 
    xa = renpy . random . random ()
     def  newxa ():
         global xa
        xa = renpy . random . random ()
        renpy . restart_interaction ()
     # function -> action 
    SPlay = renpy . curry (splay)
    SStop = renpy . curry (sstop)
    NewXA = renpy . curry (newxa)
    p = Character ( "Pig" , color = "# ffcc77" , window_left_padding = 200 , show_side_image = Image ( "pig.png" , align = ( 0.0 , 1.0 )))

# screen for rain and thunder
screen Rain:
    # turn on and turn off the rain with the 
    on 'show' action SPlay ( "rain" , loop = True )
     screen # you can only stop the rain SStop ("rain"), 
    # then the thunder that has started will rattle and subside 
    on 'hide' action SStop ( )
     # pseudo-random peals 
    timer 4.5 repeat True action SPlay ( "thunder1" )
    timer 6.5 repeat True action SPlay ( "thunder2" )
    timer 15.0 repeat True action SPlay ( "thunder3" )
     # picture with lightning 
    timer . 1 repeat True action NewXA ()
    add "light" :
        xalign xa
    # rain 
    add "rain" :
        alpha . fifteen

init:
    # Blank picture 
    image none = Null in ( 1 , 1 )
     # animation rain 
    image rain = Ani ( "rain" , 5 , . 1 , reverse = False The )
     # lightning animation 
    image lightning = Ani ( "lightning" , 3 , . 025 )
     # flickering lightning
    image light:
        yalign 0 yanchor 0 
        # empty 
        "none" 
        4.5 
        xzoom 1.0 
        "lightning" 
        . 1 
        "none" 
        . 1 
        "lightning" 
        . 1 
        "none" 
        1.5 
        # Mirror 
        Image xzoom - 1.0 
        "lightning" 
        . 1 
        "none" 
        . 05 
        "lightning" 
        . 1
        repeat
# the game starts here
label start:
    scene bg with  None
    show screen Rain
    with dissolve
    p "It seems like rain is going to ..."
    pause
    hide screen Rain
    with dissolve
    p "It seems to be over." 
    return
