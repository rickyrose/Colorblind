init - 3 python:
     # game window in the center of the screen 
    import  os 
    os . environ [ 'SDL_VIDEO_CENTERED' ] =  '1' 
    # automatic declaration of images 
    config . automatic_images_minimum_components =  1 
    config . automatic_images = [ '' , '_' , '/' ]
    config . automatic_images_strip = [ 'images' ]

init python:
    # First, let's draw up the main textbox: 
    # font of the game 
    style . default . font =  "anime.ttf" 
    # beautiful plump buttons in the game 
    style . button . ypadding =  8 
    style . button . xpadding =  16 
    # color of the text in the textbox 
    style . say_thought . color =  "# 000" 
    # padding for the textbox 
    hpad =  40 
    vpad =  64 
    # background of the main window 
    style. window . background = Frame ( "frame" , hpad, vpad)
     # minimum size of the textbox 
    style . window . yminimum =  200

    # and now the additional dialogs themselves: 
    # indentation of the text inside the textbox 
    style . window . left_padding = hpad
    style . window . right_padding = hpad
    style . window . top_padding = vpad
    style . window . bottom_padding = vpad
     # list for text in windows 
    whats = [ "" ]
     # indents for stretching dialog frames 
    hpad2 =  50 
    vpad2 =  28 
    # number of additional windows 
    # i.e. the number of delimiters "|" 
    whats_count =  0 
    # dialog text separator 
    divider =  "|"

    # we cut the text by the number of dialog boxes 
    def  SplitF (txt):
         global whats, whats_count
         if txt:
            whats = txt . split (divider)
         else :
            whats = [ "" ]
        whats_count =  len (whats) -  1 
    # turn into action 
    Split = renpy . curry (SplitF)

# standard screen with textbox, but with the addition of 
a line parser # and distribution of pieces of text in the windows
screen say:
    # Defaults for side_image and two_window 
    default side_image =  None 
    default two_window =  False 
    # read data from the text box 
    on "show" action Split (what)
     # Decide whether we need a two-window or one-window option. 
    if  not two_window:
         # One-window option.
        window:
            id  "window" 
            if  not whats [ 0 ]:
                background none
            vbox:
                style "say_vbox" 
                if who:
                    text who id  "who" 
                text whats [ 0 ] id  "what"  # display the first window 
    else :
         # Variant with two windows.
        vbox:
            style "say_two_window_vbox" 
            if who:
                window:
                    style "say_who_window"
                    text who:
                        id  "who"
            window:
                id  "window" 
                if  not whats [ 0 ]:
                    background none
                vbox:
                    style "say_vbox" 
                    text whats [ 0 ] id  "what"  # print the first window

    # If there is an image, display it above the text. 
    if side_image:
        add side_image
    else :
        add SideImage () xalign 0.0 yalign 1.0

    # display data in additional dialog boxes 
    if whats_count >  0 :
        hbox:
            for i in  range ( 1 , whats_count +  1 ):
                 if whats [i]:
                     # text in windows
                    frame:
                        text _ (whats [i]) xalign . 5 color "# 000" 
                        # screen width / number of dividers = window width 
                        xminimum (config . Screen_width / whats_count)
                        xmaximum (config . screen_width / whats_count)
                         # padding for text from frame edges
                        left_padding vpad2
                        right_padding vpad2
                        top_padding vpad2
                        bottom_padding vpad2
                        # background of windows 
                        background Frame ( "bubble" , hpad2, vpad2)
                 else :
                     # no text, empty dialog, no background
                    frame:
                        text _ ( "" )
                        xminimum (config . screen_width / whats_count)
                        background none

    # Use quick menu.
    use quick_menu

label start:
    scene bg street
    "The text in the main window." 
    show girl1 at left with moveinleft
     "Text in the main window. | Dialog 1 (full width)" 
    show girl2 with dissolve
     "Text in the main window. || Dialog 2 \ n Line 2 |" 
    show girl3 at right with moveinright
     "Text in the main window. ||| Dialog 3" 
    "Text in the main window. | Dialog 1 | Dialog 2 \ n Line 2 | Dialog 3"
    hide girl1
    hide girl3
    with dissolve
     "|| Without the main text. |" 
    return
