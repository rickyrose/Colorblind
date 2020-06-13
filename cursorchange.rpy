init python:
     # function for changing the cursor 
    # cursors must be in the images folder 
    # cur0 - name for the system cursor 
    def  cursor (name =  "cur0" , x = 0 , y = 0 ):
         if name ! =  "cur0" :
            persistent . cur = name
            persistent . cx =  0 
            persistent . cy =  0 
            config . mouse = { 'default' : [( 'images /'  + name +  '.png' , x, y)]}
         else :
            config . mouse =  None 
    # turn the function into action, 
    # so that you can bind, for example, to button presses: 
    # action Cursor ("cur0", 2, 4) 
    Cursor = renpy . curry (cursor)
     # show / hide the cursors menu 
    cur_choo =  False 
    # at the first start we set the default cursor 
    if persistent . cur is  None :
        persistent . cur =  "cur0" 
        persistent . cx =  0 
        persistent . cy =  0 
    # at each start, put the last cursor selected 
    cursor (persistent . cur, persistent . cx, persistent . cy)

screen cursor_chooser:
    vbox:
        align ( 1.0 , 0.0 )
         # button to show / hide the cursor list 
        imagebutton auto "cur_ % s .png" focus_mask True action SetVariable ( "cur_choo" , not cur_choo) xalign 1.0 
        # buttons for changing the cursor to the finger 
        if cur_choo:
            textbutton _ ( "{image = cur0.png}" ) action Cursor ( "cur0" )
            textbutton _ ( "{image = cur1.png}" ) action Cursor ( "cur1" , 2 , 2 )
            textbutton _ ( "{image = cur2.png}" ) action Cursor ( "cur2" )
            textbutton _ ( "{image = cur3.png}" ) action Cursor ( "cur3" )
            textbutton _ ( "{image = cur4.png}" ) action Cursor ( "cur4" , 3 )
            textbutton _ ( "{image = cur5.png}" ) action Cursor ( "cur5" , 3 )
            textbutton _ ( "{image = cur6.png}" ) action Cursor ( "cur6" )

label start:
    # show cursor selection screen
    show screen cursor_chooser
    "Click on the button in the corner and select the cursor." 
    "The next time you start, the cursor is saved." 
    return

