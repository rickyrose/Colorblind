# you need to upload the rpy_save.rpy file to the project’s game folder 
# it is responsible for saving any data (in the form of a python code) 
# the level of this block must be lower than the level of the saved

init python:
    # for example, we will create some class for objects on the screen 
    # it can have any structure, parameters, functions 
    # classes can have several 
    class  TUnit :
         # the input parameter names must coincide with the class parameter names! 
        def  __init__ ( self , id , sprite = None , x = 0 , y = 0 , flip = False ):
             # unique identifier of the 
            self object . id =  id 
            # its image (objects may look the same) 
            if not sprite:
                sprite =  id 
            self . sprite = sprite
             # coordinates of the 
            self object . x = x
             self . y = y
             # mirroring 
            self . flip = flip

        # the function returns the horizontal zoom of the object 
        def  xzoom ( self ):
             if  self . flip:
                 return  - 1.0 
            return  1.0

    # a list of all objects on the screen 
    units = []

    # if the flag is set, then the editor mode, not the game 
    edit_mode =  False

    # selected unit 
    current_unit =  None

    # list of available sprites 
    sprites_list = [ "guy" , "kolonna" , "lenin" , "bg" ]

    # last selected sprite 
    last_sprite = sprites_list [ 0 ]

    # the function returns an object with the desired id 
    def  get_unit ( id ):
         # 
        iterates over all units in search of the desired for i in units:
             if i . id ==  id :
                 return i
         return  None

    # function for dragging an object with the mouse 
    def  draggetxy (drags, drop):
         global units, current_unit

        # reset the old coordinates of the object 
        drags [ 0 ] . oldposition =  None 
        # get access to the desired 
        i = get_unit (drags [ 0 ] . drag_name)
         # if it exists, then 
        if i:
             # change the coordinates of the object to the current 
            i . x, i . y = drags [ 0 ] . x, drags [ 0 ] . y
             # select the current object 
            current_unit =i
             # redraw the 
            renpy screen . restart_interaction ()
    
    
    #save the 
    level and close the program, # so that at the next start, renpai compiles # the saved python code into a file of the * .rpyc 
    def  save_quit () type:
         # save the 
        generated test_data_init 
        # 
        block with level 1 (init 1 python: to the file TEST_DATA_SAVE.rpy ) # separated by commas, indicate the names of all variables, 
        # objects, lists, tuples, etc., 
        # the current state of which you need to remember 
        # in this case, only a list of objects on the screen 
        # and a list of available sprites 
        rpy_save ( "TEST_DATA_SAVE" , "test_data_init" , 1 , "units" ,"sprites_list" )
         # close the 
        Quit program (confirm = False ) ()
     # create an action for the editor button 
    SaveQuit = renpy . curry (save_quit)

    # create a new unique id 
    def  new_id ():
        i =  0 
        name =  to None 
        # iterate id numbers until you reach even non-existent 
        The while  not name:
             the if get_unit ( "id"  +  of str (i)):
                i + =  1 
            else :
                name =  "id"  +  str (i)
         return name

    # adding a new object to the screen 
    def  add_unit ():
         global units, current_unit
        current_unit = TUnit ( "id" , last_sprite)
        current_unit . id = new_id ()
         # add the created object to the 
        units list . append (current_unit)
        renpy . restart_interaction ()
    AddUnit = renpy . curry (add_unit)

    # removing an object from the screen 
    def  del_unit ():
         global units, current_unit
         if current_unit:
            units . remove (current_unit)
            current_unit =  None 
            renpy . restart_interaction ()
    DelUnit = renpy . curry (del_unit)

    # change object layer 
    def  up_unit ():
         global units, current_unit
         if current_unit:
            oldindex = units . index (current_unit)
            newindex = oldindex +  1 
            if newindex > =  len (units):
                newindex =  0 
            units . insert (newindex, units . pop (oldindex))
            renpy . restart_interaction ()
    UpUnit = renpy . curry (up_unit)

    # mirroring an object 
    def  flip_unit ():
         global units, current_unit
         if current_unit:
            current_unit . flip =  not current_unit . flip
            renpy . restart_interaction ()
    FlipUnit = renpy . curry (flip_unit)

    # changing the image of the 
    def  object spr_unit ():
         global units, current_unit, last_sprite
         if current_unit:
            index = sprites_list . index (current_unit . sprite) +  1 
            if index > =  len (sprites_list):
                index =  0 
            current_unit . sprite = sprites_list [index]
            last_sprite = sprites_list [index]
            renpy . restart_interaction ()
    SprUnit = renpy . curry (spr_unit)

# editor screen (aka game screen)
screen game:
    modal edit_mode

    # in game mode, we simply display objects on the screen 
    if  not edit_mode:
         for i in units:
            add i . sprite pos (i . x, i . y)
     # in editor mode allows moving and changing the 
    else :
         object for i in units:
            drag:
                # name of the object for the coordinate change function 
                drag_name i . id
                 # coordinates of the object 
                pos ( int (i . x), int (i . y))
                 # the object itself
                button:
                    
                    #button without background and indentation 
                    background None xpadding 0 ypadding 0 
                    xmargin 0 ymargin 0 
                    # image of the object 
                    add i . sprite xzoom i . xzoom ()
                     # so that you can drag and drop, turn off actions
                    action []
                    # to drag only for drawing 
                    focus_mask True 
                    # what to do when dragging (function above)
                dragged draggetxy
                
                #selecting an item with a click rather than dragging clicked SetVariable ( "current_unit" , i)

    if edit_mode:
         # editor menu
        frame:
            background "# 0128" 
            align ( 1.0 , 1.0 )
            vbox:
                textbutton _ ( "Add Object" ) action AddUnit ()
                textbutton _ ( "Change sprite" ) action [SensitiveIf (current_unit), SprUnit ()]
                textbutton _ ( "Change Layer" ) action [SensitiveIf (current_unit), UpUnit ()]
                textbutton _ ( "Mirror Object" ) action [SensitiveIf (current_unit), FlipUnit ()]
                textbutton _ ( "Delete Object" ) action [SensitiveIf (current_unit), DelUnit ()]
                textbutton _ ( "Exit" ) action Return ()
                textbutton _ ( Save and Exit) action SaveQuit ()

        # sprite options 
        if current_unit:
            frame:
                background "# 0128" 
                align ( 0.0 , 1.0 )
                vbox:
                    text "id:"  +  str (current_unit . id)
                    text "sprite:"  +  str (current_unit . sprite)
                    text "x, y:"  +  str (current_unit . x) +  ","  +  str (current_unit . y)
                    text "flip:"  +  str (current_unit . flip)
                    text "order:"  +  str (units . index (current_unit))

# select mode
label start:
    $ quick_menu =  False
    menu:
        "Editor Mode" :
            call edit_mode
        "Game Mode" :
            call game_mode
    $ quick_menu =  True 
    return

# show the screen in game mode
label game_mode:
    # if there are saves, then start loading from them 
    if  "test_data_init"  in  globals () . keys ():
         $ test_data_init ()

    $ edit_mode =  False
    show screen game

    "Showing the result ..." 
    return

# show the screen in editor mode
label edit_mode:
    # if there are saves, then start loading from them 
    if  "test_data_init"  in  globals () . keys ():
         $ test_data_init ()

    $ edit_mode =  True 
    $ current_unit =  None 
    $ last_sprite = sprites_list [ 0 ]
    call screen game
    return
