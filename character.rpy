# the module contains a character constructor, 
# which iterates over all the characters from the list, 
# fastens their heads from the list of emotions 
# and creates the character itself 
# in the images folder there should be a side folder 
# in it subfolders with the names of the characters to store their emotions 
# and also in the images folder should contain body files with character names, 
# but without goals

# to use the module you just need to fill out the list 
# chars with tuples from the name of the sprite, the name of the character and the color of the name 
# ("dane", _ (u "Dane Thorson"), "#fff")

init python:
    # automatic image declaration 
    config . automatic_images_minimum_components =  1 
    config . automatic_images = [ '' , '_' , '/' ]
    config . automatic_images_strip = [ "images" ]

    # list of heroes to be constructed 
    # alias for sprites and screen name 
    chars = [( "dane" , _ ( u "Dane Thorson" ), "#fff" ), ( "vera" , _ ( u "Faith" ) , "#cdf" )]

    # list of available emotions 
    zemo = [ "ok" , "angry" , "smile" ]

    # default sprite sizes 
    default_width =  600 
    default_height =  1080

    # default indentation to the head 
    # in case the head images are smaller than on the sprite 
    default_xoffset =  0 
    default_yoffset =  0

    # all that is not worth changing further :)

    # character constructor 
    def  make_character (name, width = default_width, height = default_height, xoffset = default_xoffset, yoffset = default_yoffset):
         #
         iterate over emotions for emo in zemo:
             # sprite name for emotion 
            face =  "side"  + name +  ""  + emo
             # body / base + emotion 
            args = [(width, height), ( 0 , 0 ), name, (xoffset, yoffset), face]
            # we collect 
            renpy in a sprite . image (name +  ""  + emo, LiveComposite ( * args, align = ( . 5 , 1.0 )))

    # Collect all the characters 
    for nick, name, color in chars:
         # collect large sprites of headless bodies and heads with emotion 
        the if nick ==  "vera" :
             # sprite exception 
            make_character (nick, 950 , 1080 , 250 )
         the else :
             # standard sprites
            make_character (nick)
        # head for empty emotion from ok.png 
        renpy . copy_images ( "side"  + nick +  "ok" , "side"  + nick)
         # give the character a name and a talking head 
        # you can add the color of the name and other character attributes 
        globals () [nick] = Character (name, image = nick, who_color = color)

init:
    transform ax (x =. 5 ):
        xalign x

# The game starts here:
label start:
    scene bg caffee
    show dane ok
    with dissolve

    dane "Hi, I'm Dane Thorson. This is an example of how to make talking heads in Ren'Py."

    dane angry "Now I have to get angry."

    dane smile "Now - smile."

    show dane smile at ax ( . 25 )
    show vera ok at ax ( . 75 )
     with moveinright
    vera "And I am Vera. I wish you all the best."

    vera smile "I'm here as an exception. Like a big sprite from which heads were cut out at some distance from the edge."

    return
