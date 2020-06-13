init python:
     # the first time you start the game, an empty list of "discoveries" 
    if persistent is created . pages is  None :
        persistent . pages = []
     # number of the current page 
    page =  0 
# screen for displaying open pages
screen scrPages:
    # frame for page
    frame:
        the align ( . 5 , . 2 ) # location 
        # size 
        xminimum 500 xmaximum 500 
        yminimum 400 ymaximum 400 
        background Used "# 0028"  # background
        vbox:
            spacing 16 
            # container with page control buttons
            hbox:
                xfill True The 
                # button that flips through pages backwards (with verification on the border) 
                # SensitiveIf makes the button active when the condition 
                textbutton _ ( "« " ) the align ( . 0 , . 0 ) the action [SensitiveIf (page >  0 ), the SetVariable ( " page " , page -  1 )]
                text of str (page +  1 ) +  "from"  +  of str ( len is (persistent . pages)), the align ( . 5 , . 0 )
                 # button that flipping back pages (checked at the border) 
                textbutton _ ( "» " ), the align ( 1.0 , . 0 ) action [SensitiveIf (page <  len (persistent . pages) -  1 ), SetVariable ( "page" , page +  1)]
             # if the current page is available, then print it 
            if page > =  0  and page <  len (persistent . pages):
                 $ title, txt, img = persistent . pages [page]
                 # horizontal container so the picture is on the left
                hbox:
                    vbox:
                        # picture 
                        xminimum 200 xmaximum 200 
                        # if it is, then output 
                        if img:
                            img align add ( . 5 , . 2 )
                     # vertical container for the text
                    vbox:
                        xfill True yalign . 1 
                        # distance between objects in the 
                        spacing container 16 
                        # page 
                        title text title xalign . 5 
                        # page 
                        text text txt xfill True
 
label start:
    "First, we’ll show a screen with pages. It’s blank when you first start it."
    show screen scrPages
    "Add one page." 
    $ persistent . pages . append (( "Page 1" , "Page text. Just any text to set an example." , "image1" ))
     "Now add a couple more pages." 
    $ persistent . pages . append (( "Page 2" , "The text of the second page. And again, just any text to show an example." , "image2" ))
     $ persistent . pages . append (( "Page 3" ,"The text of the second page. And again, just any text in order to set an example. Only this time without a picture." , "" ))
     "Now you can look through them."
    hide screen scrPages
    "The session is over. Thank you all."
    menu:
        "Clear page list?" 
        Yes :
             # this line clears the data in the 
            $ persistent page list . pages = []
             # most likely the button 
            # textbutton _ ("Clear") action SetField (persistent, "pages", []) 
        "No" will be used for this :
             pass 
    return
