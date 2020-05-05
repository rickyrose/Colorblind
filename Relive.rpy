screen relive_menu:
    zorder 10
    tag mini_menu
#Allows user to relive minigame not fully implimented 
#Do Not Use until Finished

    if relive_menu_tutor_complete == 0:
        pass
    else:
        modal True

    vbox:
        imagebutton auto "buttons/closer_button_cell_%s.png" focus_mask True action [SetVariable("phone_button_on", 0), Hide("relive_menu")]

    vbox:
        xpos 784
        ypos 80
        image "bg/cell_phone_display.png"

    frame:
        xpos 816
        ypos 140
        text "{size=18}Total Events: [complete_rel_e!t]/[max_rel_e]{/size}"

    if relive_menu_tutor_complete == 0:
        frame:
            xpos 816
            ypos 190
            textbutton "{size=28}Maze{/size}" action NullAction()

    if m_ex_active == 1:
            vbox:
                xpos 909
                ypos 180
                image "bg/exclaim_icon.png"
                
                
           vbox:
            xpos 931
            ypos 691
            imagebutton auto "buttons/cell_phone_off_button_%s.png" focus_mask True action NullAction()
            
    else:
        frame:
            xpos 816
            ypos 190
            textbutton "{size=28}Maze{/size}" action [Hide("relive_menu"), Show("relive_m_menu")]
            
   if m_ex_active == 1:
            vbox:
                xpos 909
                ypos 180
                image "bg/exclaim_icon.png"
                
                
                
                
    vbox:
            xpos 931
            ypos 691
            imagebutton auto "buttons/cell_phone_off_button_%s.png" focus_mask True action [Hide("relive_menu"), Show("cell_phone_menu")]
            
            
            
            
    screen relive_m_menu:
    zorder 3
    tag mini_menu
    modal True

    vbox:
        imagebutton auto "buttons/closer_button_cell_%s.png" focus_mask True action [SetVariable("phone_button_on", 0), SetVariable("m_ex_active", 0), Hide("relive_m_menu")]

    vbox:
        xpos 784
        ypos 80
        image "bg/cell_phone_display.png"

    frame:
        xpos 816
        ypos 140
        text "{size=18}Maze Events: [m_rel_e_found!t]/[m_rel_e_max]{/size}"

    frame:
        xpos 816
        ypos 190
        has vbox

        side ("c r"):
            area (1,0,280,470)
            viewport id "relive_m_scroll":
                draggable True mousewheel True

                vbox:
                    if lab_escape == 1:
                        textbutton "{size=20}Replay the Maze{/size}" action [SetVariable("phone_button_on", 0), SetVariable("m_ex_active", 0), Jump("Meg_Barge_Rep")]

 
            vbar value YScrollValue("relive_m_scroll")
    null height 20

    vbox:
        xpos 931
        ypos 691
        imagebutton auto "buttons/cell_phone_off_button_%s.png" focus_mask True action [SetVariable("m_ex_active", 0), Hide("relive_m_menu"), Show("relive_menu")]






scene ep1_01_wake
    with fade
    $ m_ex_active = 0
    g 
    scene ep1_02_uh
    m 
    scene ep1_03_wow
    with dissolve
    g 
    scene ep1_03_ugh
    dc 
    g 
    scene ep1_04_can
    g 
    dc 
    scene ep1_05_you
    with dissolve
    n 

    jump Going_Back_Af_Replay
