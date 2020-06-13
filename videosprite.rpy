init python:
     # game window in the center of the screen 
    import  os 
    os . environ [ 'SDL_VIDEO_CENTERED' ] =  '1' 
    # automatic declaration of images 
    config . automatic_images_minimum_components =  1 
    config . automatic_images = [ '' , '_' , '/' ]
    config . automatic_images_strip = [ 'images' ]

# The game starts here.
label start:
    scene bg tvset
    # blank picture instead of video 
    show expression Null ( 1 , 1 ) as video
     # video file name without extension 
    $ chan =  None
label chan_select:
    # channel selection (video file name)
    menu:
        "What are we going to watch?" 
        "Series" :
             $ chan =  "sitcom" 
        "Comedy" :
             $ chan =  "comedy" 
        "Sport" :
             $ chan =  "sport" 
        "Nothing" :
             $ chan =  None 
    # if the channel / file name is not empty 
    if chan:
         # then display the video in the right place 
        show expression Movie (play = chan + ".mp4" , pos = ( 444 ,= ( 0 , 0 ), size = ( 320 , 240 )) as video
        pause
        # and go choose the channel again
        jump chan_select
    else :
         # otherwise hide the video
        hide video
    "Better do business." 
    return
