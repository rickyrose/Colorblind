# drop sms.rpy and 7dots.rpy into the game folder of your project and write sms 
# tags for sms: 
# "{# l = Hello!}" - for sms from the left interlocutor 
# "{# r = And hello to you! } "- for SMS from the right interlocutor 
#" {# c = Losyas left the conversation.} "- for system SMS in the center 
#" {#on} "or $ sms_on () - show a window with SMS 
#" {#off} " or $ sms_off () - hide the window with SMS 
# "{#cls}" or $ sms_cls () - clear the window with SMS 
# there can be several different tags in one line and plain text 
# "<<smile>>" - like this add pictures 
# message history can be viewed,leafing through the screen with the mouse or the wheel 
# the smooth disappearance / appearance of the text box with SMS accounting is also implemented

init python:
    # sms sounds 
    sms_c =  "sms_c" 
    sms_l =  "sms_l" 
    sms_r =  "sms_r"

    # duration of vibration (if the device supports it) 
    sms_vibrate =  . 5

    # position of the window with SMS 
    sms_xalign, sms_yalign =  . 75 , . 25

    # window size with SMS (cell screen) 
    sms_width, sms_height =  450 , 600

    # sizes of one SMS 
    sms_w, sms_h =  int (sms_width *  . 75 ), int (config . screen_height *  . 05 )

    # header sizes with the name of the interlocutor 
    sms_caption_height =  100 
    sms_caption_width = sms_width

    # interlocutor name 
    sms_name =  "Unknown"

    # indentation for sms bubbles 
    sms_xpadding =  32 
    sms_ypadding =  16 
    # external 
    sms_border =  16

    # to store the text of all SMS 
    sms_all = []

    # tags for SMS - in the center, left, right 
    sms_tags = [ "c" , "l" , "r" ]

    # all tags for sms, including window control 
    sms_all_tags = sms_tags + [ "on" , "off" , "cls" ]

    # get text and sms style from a string like "r = Hello!" 
    def  get_sms_text_style (txt):
        smsstyle, smstext = get_key_val (txt)
         if smsstyle in sms_tags:
             return  "sms_"  + smsstyle, smstext
         return  None , txt

    # remove sms text from the text box and drop sms on the screen 
    def  sms (text):
         global sms_all, sms_last_what
         # get tags as strings 
        tags = get_tags_str (text)
         # sort through lines with 
        for i in tags tags:
             # parse a string into parts separated sign = equals = 
            key, val = get_key_val (i)
             # clear the sms window 
            if key ==  "cls" :
                sms_cls ()
            # show sms window 
            if key ==  "on" :
                sms_on ()
            # hide sms window 
            if key ==  "off" :
                sms_off ()
            # new message in the sms window 
            if key in sms_tags:
                 if val is  None :
                    val =  "" 
                # change the emoticons on the pictures 
                val = val . replace ( "<<" , "{image =" )
                val = val . replace ( ">>" , "}" )
                 # add 
                sms_all sms to the screen . append (key +  "="  + val)
                renpy . restart_interaction ()
                 # message sound 
                sms_sound =  "sms_"  + key
                 if sms_sound:
                    splay (sms_sound)
                    if sms_vibrate >  0 :
                        renpy . vibrate (sms_vibrate)
     # from a function in action 
    SMS = renpy . curry (sms)

    # show sms screen 
    def  sms_on (effect = dissolve):
        renpy . show_screen ( 'sms_screen' , _layer = "master" )
        renpy . transition (effect)

    # hide sms screen 
    def  sms_off (effect = dissolve):
        renpy . hide_screen ( 'sms_screen' , layer = "master" )
        renpy . transition (effect)

    # clear sms screen 
    def  sms_cls (effect = dissolve):
         global sms_all
        sms_all = []
        sms_on (effect = effect)

    # to store the last text visible in the textbox 
    sms_last_what =  None

    # scroll down 
    yadjValue =  float ( "inf" )
    yadj = ui . adjustment ()

init:
    # transparency 
    transform transparent (alpha =. 0 ):
        alpha alpha

    # style for SMS frame 
    style sms_frame is frame:
         # blank screen image 
        background "smsbg" 
        yfill True
        xminimum sms_width xmaximum sms_width
        yminimum sms_height ymaximum sms_height
        xmargin 0 ymargin 0 
        xpadding 0 ypadding 0

    # style sms system centered 
    style sms_c is button:
        background "# 0000" 
        xalign . 5 
        xmargin sms_border ymargin sms_border /  2  
        xpadding 0 ypadding sms_ypadding

    # color of system messages 
    $ style . sms_c_text . color =  "# 0008"

    # sms 
    style on the left style sms_l is sms_c:
        xpadding sms_xpadding ypadding sms_ypadding
        xmaximum sms_w yminimum sms_h
        xalign . 0 
        background Frame ( "smsleft" , 16 , 16 )

    # sms 
    style on the right style sms_r is sms_l:
        xalign 1.0 
        background Frame ( "smsright" , 16 , 16 )

    # style of the window with the name of the interlocutor 
    style sms_caption is button:
        background Frame ( "smstop" , 0 , 0 )
        xfill True The
        xminimum sms_caption_width
        yminimum sms_caption_height

    # style of the window with the name of the interlocutor 
    style sms_bottom is button:
        background Frame ( "smsbottom" , 0 , 0 )
        xminimum sms_caption_width
        yminimum sms_caption_height /  2

    # style of the text with the name of the interlocutor 
    style sms_caption_text is button_text:
        color "#fff" 
        font "fonts / robotoblack.ttf" 
        align ( . 4 , . 75 )

    # effect for appearance / disappearance of the text box 
    transform inout (t =. 25 ):
        on show:
            alpha . 0 
            linear t alpha 1.0
        on hide:
            alpha 1.0 
            linear t alpha . 0

    # manifest 
    transform inin (t =. 25 ):
        alpha . 0 
        linear t alpha 1.0

    # dissolve 
    transform outout (t =. 25 ):
        alpha 1.0 
        linear t alpha . 0

# screen with sms
screen sms_screen:
    python:
        yadj . value = yadjValue
    vbox:
        align (sms_xalign, sms_yalign)
        frame:
            style "sms_frame"
            vbox:
                # Interlocutor name 
                textbutton sms_name style "sms_caption" the align ( . 5 , . 0 )
                 # container for bubbles with messages
                frame:
                    xmargin 0 ymargin 0 
                    xpadding 0 ypadding 0 
                    background None
                    viewport:
                        id  "sms_vp" 
                        xinitial 1.0 
                        yfill False 
                        mousewheel True 
                        draggable False 
                        side_xfill True
                        transclude
                        yadjustment yadj
                        vbox:
                            xfill True 
                            yanchor 1.0 
                            yalign 1.0 
                            for i in sms_all:
                                 # message bubbles 
                                $ sms_style, sms_text = get_sms_text_style (i)
                                textbutton sms_text:
                                    if sms_style:
                                        style sms_style
                                    action []
        textbutton "" style "sms_bottom" action [] yalign 1.0

# rewrite the screen say
screen say (who, what):
    # SMS tag processing 
    on "show" action SMS (what)
    on "hide" action SetVariable ( "sms_last_what" , del_tags (what))

    style_prefix "say"

    window:
        # so that an empty window does not loom 
        if  not del_tags (what):
             # but 
            if sms_last_what fades smoothly :
                at outout ()
            else :
                 # at start was generally invisible
                at transparent ()
        else :
             if  not sms_last_what:
                 # appeared smoothly if visible text appeared
                at inin ()
            else :
                 # so that the text box appears and disappears smoothly in other cases
                at inout ()

        id  "window"

        if who is  not  None :

            window:
                id  "namebox" 
                style "namebox" 
                text who id  "who"

        text what id  "what"

    ## If there is a side image ("head"), shows it on top of the text. 
    ## By the standard, it is not shown on the option for mobile devices - there is not enough 
    ## space. 
    if  not renpy . variant ( "small" ):
        add SideImage () xalign 0.0 yalign 1.0
