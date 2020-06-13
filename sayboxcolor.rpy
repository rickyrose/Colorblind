init - 4 python:
    style . default . font =  "fonts / blogger.otf" 
    # features from 7dots.rpy
    window_center ()
    images_auto ()

init:
    # this variable is responsible for the background of the text box (saybox) 
    $ frame =  "steam" 
    # create two stretching pictures for the saybox background 
    image frmF = Frame ( "frame future" , 100 , 100 )
    image frmS = Frame ( "frame steam" , 160 , 160 )
     # create a picture that changes if the variables are changed 
    image frm = ConditionSwitch ( "frame == 'future'" , "frmF" , "frame == 'steam'" , "frmS" )

init - 1 python:
     # assign to the box our changing background 
    style . window . background =  "frm"

    # OPTIONAL BEAUTIES: 
    # font sizes 
    font_size ( 36 , 48 , 48 , 64 )
     # alignment width 
    style . default . justify =  True 
    # indent for text 
    style . window . xpadding =  120 
    style . window . ypadding =  90 
    style . window . yminimum =  320 
    style . window .xmargin =  140 
    # padding for 
    style menu buttons . mm_button . xpadding =  72 
    style . gm_nav_button . xpadding =  36

label start:
    scene bg jail2
    show sen normal
    "The default design."

    $ frame =  "future"  # change the background of the box
    show bg pab2 behind sen
    with dissolve
     "Another design. \ n If you save, after loading it, the background of the text window will not be reset to the original, as it would if you just changed the window style with the command {b} {i} style.window.background = ' saybox '{/ i} {/ b}. "

    "Because now the background depends on the variable frame, and it is saved and loaded with all the other data. And style.window.background is set at startup."

    $ frame =  "steam"  # change the background of the saybox
    show bg jail2 behind sen
    with dissolve
     "Again the default design." 
    return
