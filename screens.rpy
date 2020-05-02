#########################################
#
# This file is in the public domain. Feel free to modify it and use it anyway you want.
#
#########################################
################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)

init:
    transform trans30:
        alpha 0.3
    image main_menu_cg="gui/test_background.jpg"
    image main_menu_cg_foggy=LiveComposite((1280,720), (0,0), Solid("#fff"), (0,0), At("gui/test_background.jpg", trans30))

## ■██▓▒░ MAIN MENU ░▒▓█████████████████████████████████████■
## Screen that's used to display the main menu, when Ren'Py first starts
## http://www.renpy.org/doc/html/screen_special.html#main-menu
screen main_menu:
    tag menu # This ensures that any other menu screen is replaced.
    # Add a background image for the main menu:
    add "main_menu_cg"
    add "gui/main_menu_ground.png"
    add "gui/main_menu_title.png"
    $ x = 995
    $ y=110
    imagebutton auto "gui/MainStart-%s.png" xpos x ypos y focus_mask None action Start() hovered [ Play ("test_one", "sfx/click.wav"), Show("gui_tooltip", my_picture="tooltip_main_menu_start") ] unhovered [Hide("gui_tooltip")] at main_eff1
    $ y+=90
    imagebutton auto "gui/MainLoadStart-%s.png" xpos x ypos y focus_mask None action ShowMenu('load') hovered [ Play ("test_two", "sfx/click.wav"), Show("gui_tooltip", my_picture="tooltip_game_menu_load") ] unhovered [Hide("gui_tooltip")] at main_eff2
    $ y+=90
    imagebutton auto "gui/MainOptionsStart-%s.png" xpos x ypos y focus_mask None action ShowMenu('preferences') hovered [ Play ("test_three", "sfx/click.wav"), Show("gui_tooltip", my_picture="tooltip_game_menu_config") ] unhovered [Hide("gui_tooltip")] at main_eff3
    $ y+=90
    # if persistent.extra_unlocked: # We only show the extras, if they have been unlocked. Because we are using a variable (y) for ypos, we don't need to worry about positioning the rest of the button(s).
    imagebutton auto "gui/MainExtrasStart-%s.png" xpos x ypos y focus_mask None action ShowMenu('extras_blank') hovered [ Play ("test_four", "sfx/click.wav"), Show("gui_tooltip", my_picture="tooltip_main_menu_extras") ] unhovered [Hide("gui_tooltip")] at main_eff4
    $ y+=90
    imagebutton auto "gui/MainHelpStart-%s.png" xpos x ypos y focus_mask None action ShowMenu('help') hovered [ Play ("test_five", "sfx/click.wav"), Show("gui_tooltip", my_picture="tooltip_main_menu_help") ] unhovered [Hide("gui_tooltip")] at main_eff4
    $ y+=90
    imagebutton auto "gui/MainQuitStart-%s.png" xpos x ypos y focus_mask None action Quit(confirm=False) hovered [ Play ("test_six", "sfx/click.wav"), Show("gui_tooltip", my_picture="tooltip_game_menu_quit") ] unhovered [Hide("gui_tooltip")] at main_eff5

# The code below defines the ATL transform effects for each button on the main menu. These effects are triggered when the buttons are shown.
# ATL transform properties: http://www.renpy.org/wiki/renpy/doc/reference/Animation_and_Transformation_Language#Transform_Properties
init -2:
    transform main_eff1:
        zoom 0.5
        easein 0.4 zoom 1.0
    transform main_eff2:
        zoom 0.5
        easein 0.8 zoom 1.0
    transform main_eff3:
        zoom 0.5
        easein 1.2 zoom 1.0
    transform main_eff4:
        zoom 0.5
        easein 1.6 zoom 1.0
    transform main_eff5:
        zoom 0.5
        easein 2.0 zoom 1.0
    transform main_eff6:
        zoom 0.5
        easein 2.4 zoom 1.0

style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text



## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xalign gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width

## ■██▓▒░ NAVIGATION ░▒▓████████████████████████████████████■
## This screen is responsible for the game menu/navigation. It's included in other screens to display the game menu navigation.
## http://www.renpy.org/doc/html/screen_special.html#navigation
screen navigation:
    add "main_menu_cg_foggy"
    add "gui/main_menu_ground.png"
    add "gui/game_menu_ground.png"
    imagebutton auto "gui/OptionsSaveGame-%s.png" xpos 980 ypos 129 focus_mask True action ShowMenu('save') hovered [ Play ("test_one", "sfx/click.wav"), Show("gui_tooltip", my_picture="tooltip_game_menu_save") ] unhovered [Hide("gui_tooltip")] at nav_eff
    imagebutton auto "gui/OptionsLoadGame-%s.png" xpos 980 ypos 214 focus_mask True action ShowMenu('load') hovered [ Play ("test_two", "sfx/click.wav"), Show("gui_tooltip", my_picture="tooltip_game_menu_load") ] unhovered [Hide("gui_tooltip")] at nav_eff
    imagebutton auto "gui/OptionsOptions-%s.png" xpos 980 ypos 297 focus_mask True action ShowMenu('preferences') hovered [ Play ("test_three", "sfx/click.wav"), Show("gui_tooltip", my_picture="tooltip_game_menu_config") ] unhovered [Hide("gui_tooltip")] at nav_eff
    imagebutton auto "gui/OptionsMainMenu-%s.png" xpos 980 ypos 381 focus_mask True action MainMenu() hovered [ Play ("test_one", "sfx/click.wav"), Show("gui_tooltip", my_picture="tooltip_game_menu_main") ] unhovered [Hide("gui_tooltip")] at nav_eff
    imagebutton auto "gui/OptionsReturn-%s.png" xpos 980 ypos 465 focus_mask True action Return() hovered [ Play ("test_two", "sfx/click.wav"), Show("gui_tooltip", my_picture="tooltip_game_menu_return") ] unhovered [Hide("gui_tooltip")] at nav_eff
    imagebutton auto "gui/OptionsQuitGame-%s.png" xpos 980 ypos 549 focus_mask True action Quit() hovered [ Play ("test_three", "sfx/click.wav"), Show("gui_tooltip", my_picture="tooltip_game_menu_quit") ] unhovered [Hide("gui_tooltip")] at nav_eff

# The code below defines the ATL transform effects for the buttons on the game menu. These effects are triggered when we hover the mouse over them (hover and selected_hover). Effects that are triggered by idle and selected_idle events (when we stop hovering the mouse over them) ensure that the buttons are moved back to the initial state.

init -2:
    transform nav_eff:
        on idle:
            easein 0.5 xpos 980
        on selected_idle:
            easein 0.5 xpos 980
        on hover:
            easein 0.3 xpos 1000
            easein 0.3 xpos 960
        on selected_hover:
            easein 0.3 xpos 1000
            easein 0.3 xpos 960

## ■██▓▒░ PREFERENCES ░▒▓███████████████████████████████████■
## Screen that allows the user to change the preferences.
## http://www.renpy.org/doc/html/screen_special.html#prefereces
screen preferences:
    tag menu # This ensures that any other menu screen is replaced.
    use navigation # We include the navigation screen (game menu)
    add "gui/config_ground.png" # We add the image that is shown in the background of the preferences screen.
    # Display windowed/full screen:
    imagebutton auto "gui/config_display_window_%s.png" xpos 405 ypos 210 focus_mask True action Preference('display', 'window') at config_eff hovered [ Play ("test_one", "sfx/click.wav"), Show("gui_tooltip", my_picture="tooltip_config_windowed") ] unhovered [Hide("gui_tooltip")]
    imagebutton auto "gui/config_display_fullscreen_%s.png" xpos 525 ypos 210 focus_mask True action Preference('display', 'fullscreen') at config_eff hovered [ Play ("test_two", "sfx/click.wav"), Show("gui_tooltip", my_picture="tooltip_config_fullscreen") ] unhovered [Hide("gui_tooltip")]
    # Transitions on/off:
    imagebutton auto "gui/config_transitions_none_%s.png" xpos 690 ypos 210 focus_mask True action Preference('transitions', 'none') at config_eff hovered [ Play ("test_four", "sfx/click.wav"), Show("gui_tooltip", my_picture="tooltip_config_enable_transition") ] unhovered [Hide("gui_tooltip")]
    imagebutton auto "gui/config_transitions_all_%s.png" xpos 810 ypos 210 focus_mask True action Preference('transitions', 'all') at config_eff hovered [ Play ("test_four", "sfx/click.wav"), Show("gui_tooltip", my_picture="tooltip_config_enable_transition") ] unhovered [Hide("gui_tooltip")]
    # Stop/continue skipping after choices
    imagebutton auto "gui/config_afterchoices_stop_%s.png" xpos 405 ypos 460 focus_mask True action Preference('after choices', 'stop') at config_eff hovered [ Play ("test_one", "sfx/click.wav"), Show("gui_tooltip", my_picture="tooltip_config_stop_skip") ] unhovered [Hide("gui_tooltip")]
    imagebutton auto "gui/config_afterchoices_skip_%s.png" xpos 525 ypos 460 focus_mask True action Preference('after choices', 'skip') at config_eff hovered [ Play ("test_two", "sfx/click.wav"), Show("gui_tooltip", my_picture="tooltip_config_go_skip") ] unhovered [Hide("gui_tooltip")]
    # Skip all/seen text
    imagebutton auto "gui/config_skip_seen_%s.png" xpos 690 ypos 460 focus_mask True action Preference('skip', 'seen') at config_eff hovered [ Play ("test_one", "sfx/click.wav"), Show("gui_tooltip", my_picture="tooltip_config_seen") ] unhovered [Hide("gui_tooltip")]
    imagebutton auto "gui/config_skip_all_%s.png" xpos 810 ypos 460 focus_mask True action Preference('skip', 'all') at config_eff hovered [ Play ("test_two", "sfx/click.wav"), Show("gui_tooltip", my_picture="tooltip_config_all") ] unhovered [Hide("gui_tooltip")]
    # bar sliders for volume control, text speed and auto-forward time
    frame xpos 60 ypos 228:
        style_group "pref"
        has vbox
        bar value Preference("music volume")
    frame xpos 60 ypos 350:
        style_group "pref"
        has vbox
        bar value Preference("sound volume")
    frame xpos 60 ypos 475:
        style_group "pref"
        has vbox
        bar value Preference("text speed")
    frame xpos 60 ypos 595:
        style_group "pref"
        has vbox
        bar value Preference("auto-forward time")

init -2 python:
    # Styling for the bar sliders:
    # Aleema's Customizing Menus tutorial: http://lemmasoft.renai.us/forums/viewtopic.php?f=51&t=9812
    # Bar style properties documentation: http://www.renpy.org/doc/html/style.html#bar-style-properties
    style.pref_frame.background = None
    style.pref_slider.left_bar = "gui/config_bar_full.png"
    style.pref_slider.right_bar = "gui/config_bar_empty.png"
    style.pref_slider.thumb = None
    style.pref_slider.xmaximum = 290
    style.pref_slider.ymaximum = 44
    style.pref_slider.left_gutter = 0
    style.pref_slider.right_gutter = 0


init -2:
    transform config_eff:
        on idle:
            easein 0.5 rotate 0
        on selected_idle:
            easein 0.5 rotate 0
        on hover:
            easein 0.3 rotate 5
            easein 0.3 rotate -5
            repeat
        on selected_hover:
            easein 0.3 rotate 5
            easein 0.3 rotate -5
            repeat

python:
    class TrackCursor(renpy.Displayable):
        def __init__(self, child):
            super(TrackCursor, self).init()

            self.child = renpy.displayable(child)

            self.x = None
            self.y = None

        def render(self, width, height, st, at):
            rv = renpy.Render(width, height)

            if self.x is not None:
                cr = renpy.render(self.child, width, height, st, at)
                cw, ch = cr.get_size()
                rv.blit(cr, (self.x - cw / 2, self.y - ch / 2))

            return rv

        def event(self, ev, x, y, st):
            if (x != self.x) or (y != self.y):
                self.x = x
                self.y = y
                renpy.redraw(self, 0)

## ■██▓▒░ SAVE / LOAD SLOT ░▒▓██████████████████████████████■
## This represents a load/save slot. You should customize this to ensure that the placement of the thumbnail and the slot text are as desired. Positions (x1, y1, x2 and y2) are relative to the x, y parameters, that are passed when the screen is called. To set the screenshot thumbnail size see options.rpy.
init -2 python: #we initialize x and y, so the load_save_slot screen below works at startup
    x=0
    y=0
screen load_save_slot:
    $ file_text = "% s\n  %s" % (FileTime(number, empty="Empty Slot."), FileSaveName(number))
    $x1=x+430
    $y1=y+15
    add FileScreenshot(number) xpos x1 ypos y1
    $x2=x+30
    $y2=y+15
    text file_text xpos x2 ypos y2 size 24 outlines [(2, "05b1e6", 0, 0)]

## ■██▓▒░ SAVE SCREEN ░▒▓███████████████████████████████████■
screen save:
    tag menu # This ensures that any other menu screen is replaced.
    use navigation # We include the navigation/game menu screen
    #add "gui/file_picker_ground.jpg" # We add the file picker background image. This image is the same for save and load screens.
    add "gui/title_save.png" # We add the save title image on top of the background
    use file_picker # We include the file_picker screen

## ■██▓▒░ LOAD SCREEN ░▒▓███████████████████████████████████■
screen load:
    use navigation # We include the navigation/game menu screen
    tag menu # This ensures that any other menu screen is replaced.
    #add "gui/file_picker_ground.jpg"
    add "gui/title_load.png"
    use file_picker

## ■██▓▒░ SAVE / LOAD FILE PICKER ░▒▓███████████████████████■
## Since saving and loading are so similar, we combine them into a single screen, file_picker. We then use the file_picker screen from simple load and save screens.
screen file_picker:
    # Buttons for selecting the save/load page:
    imagebutton auto "gui/filepage1_%s.png" xpos 66 ypos 135 focus_mask True action FilePage(1) hover_sound "sfx/click.wav"
    imagebutton auto "gui/filepage2_%s.png" xpos 66 ypos 310 focus_mask True action FilePage(2) hover_sound "sfx/click.wav"
    imagebutton auto "gui/filepage3_%s.png" xpos 66 ypos 485 focus_mask True action FilePage(3) hover_sound "sfx/click.wav"
    $ y=135 # ypos for the first save slot
    for i in range(0, 3): # This repeats the block below 3 times (counts from 0 to 2), for the 3 save slots. We could also copy/paste the block below 3 times, but we are too lazy to do that.
        imagebutton auto "gui/fileslot_%s.png" xpos 255 ypos y focus_mask True action FileAction(i)
        use load_save_slot(number=i, x=255, y=y) # This calls the load_save_slot screen defined above. We pass variable i as the slot number and x, y coordinates.
        $ y+=175 # We increase the y variable so every next save slot is moved 124px lower.

## ■██▓▒░ YES/NO PROMPT ░▒▓█████████████████████████████████■
## Screen that asks the user a yes or no question. You'll need to edit this to change the position and style of the text.
## http://www.renpy.org/doc/html/screen_special.html#yesno-prompt

screen yesno_prompt:
    on "show" action Play("sound", "sfx/alert.wav")
    modal True # A modal screen prevents the user from interacting with displayables below it, except for the default keymap.

    add "gui/yesno_ground.png"
    imagebutton auto "gui/yesno_yes_%s.png" xpos 430 ypos 450 action yes_action hover_sound "sfx/click.wav"
    imagebutton auto "gui/yesno_no_%s.png" xpos 710 ypos 450 action no_action hover_sound "sfx/click.wav"

    window background None xminimum 690 yminimum 380 xalign 0.5 yalign 0.5: # xmargin 340 ymargin 210:
        text _(message) outlines [(2, "#0613c2", 0, 0)] color "#fff" size 30:
            xalign 0.5 yalign 0.5

    # if message == layout.ARE_YOU_SURE:
        # add "gui/yesno_are_you_sure.png"
    # elif message == layout.DELETE_SAVE:
        # add "gui/yesno_delete_save.png"
    # elif message == layout.OVERWRITE_SAVE:
        # add "gui/yesno_overwrite_save.png"
    # elif message == layout.LOADING:
        # add "gui/yesno_loading.png"
    # elif message == layout.QUIT:
        # add "gui/yesno_quit.png"
    # elif message == layout.MAIN_MENU:
        # add "gui/yesno_main_menu.png"

## ■██▓▒░ CUSTOM MOUSE POINTER ░▒▓██████████████████████████■
##This block is responsible for the custom mouse pointer
# init python:
    # config.mouse = { }
    # config.mouse["default"] = [
         # ("gui/mouse_pointer.png", 8.8, 0.0),
    # ]
# Configuration variables: http://www.renpy.org/doc/html/config.html
# Custom mouse pointer is commented out, to disable it for the time being, because of an issue in all recent versions of Ren'Py.

## ■██▓▒░ TOOLTIP ░▒▓███████████████████████████████████████■
screen gui_tooltip (my_picture="", my_tt_xpos=58, my_tt_ypos=687):
    add my_picture xpos my_tt_xpos ypos my_tt_ypos

## ■██▓▒░ CUSTOM SOUND CHANNEL ░▒▓██████████████████████████■
# This is the block where we declare the individual sound channels. This enables us to play several sound FX's without overlapping
init python:
    renpy.music.register_channel("test_one", "sfx", False)
    renpy.music.register_channel("test_two", "sfx", False)
    renpy.music.register_channel("test_three", "sfx", False)
    renpy.music.register_channel("test_four", "sfx", False)
    renpy.music.register_channel("test_five", "sfx", False)
    renpy.music.register_channel("test_six", "sfx", False)

## ■██▓▒░ THE TEXTBOX ░▒▓███████████████████████████████████■
# Screen that's used to display adv-mode dialogue.
# http://www.renpy.org/doc/html/screen_special.html#say

##############################################################################
## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        if who is not None:
            window:
                id "namebox"
                style "namebox"
                text who id "who"
        text what id "what"
    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height
    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos


## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xalign gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid". When
## this screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen navigation():

    vbox:
        style_prefix "navigation"

        xpos 0.05
        yalign 0.4


        spacing gui.navigation_spacing

        if main_menu:

            textbutton _("Start") action Start() text_color "#dbb200" text_hover_color "#ffffff" text_size 35 text_outlines [ (3, "#000", 0, 0) ]

        else:

            # textbutton _("History") action ShowMenu("history")

            textbutton _("Save") action ShowMenu("save") text_size 35  text_outlines [ (3, "#000", 0, 0) ]

        textbutton _("Load") action ShowMenu("load") text_size 35  text_outlines [ (3, "#000", 0, 0) ]

        textbutton _("Settings") action ShowMenu("Settings") text_size 35  text_outlines [ (3, "#000", 0, 0) ]

        textbutton _("Language") action ShowMenu("language_chooser") text_size 35  text_outlines [ (3, "#000", 0, 0) ]

        textbutton _("Patreon") action OpenURL("https://www.patreon.com/IDK") text_idle_color "#ffc86b" text_hover_color "#f2a21d" text_size 35 text_outlines [ (3, "#000", 0, 0) ]

        if _in_replay:

            textbutton _("End Replay") action EndReplay(confirm=True) text_size 35 text_outlines [ (3, "#000", 0, 0) ]

        elif not main_menu:

            textbutton _("Main Menu") action MainMenu() text_size 35 text_outlines [ (3, "#000", 0, 0) ]

        # textbutton _("About") action ShowMenu("about")

        if renpy.variant("pc"):

            # ## Help isn't necessary or relevant to mobile devices.
            # textbutton _("Help") action ShowMenu("help")

            ## The quit button is banned on iOS and unnecessary on Android.
            textbutton _("Quit") action Quit(confirm=not main_menu) text_size 35 text_outlines [ (3, "#000", 0, 0) ]


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")

screen game_menu(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True

                        side_yfill True

                        transclude

                else:

                    transclude

    use navigation

    textbutton _("Return"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_viewport:
    xsize 1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45


## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen Settings():

    tag menu

    use game_menu(_("Settings"), scroll="viewport"):
        vbox:
            hbox:
                box_wrap True

                if renpy.variant("pc"):

                    vbox:
                        style_prefix "radio"
                        label _("Display")
                        textbutton _("Window") action Preference("display", "window")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")

                vbox:
                    style_prefix "radio"
                    label _("Fonts")
                    textbutton _("Roboto") action gui.SetPreference("font", "fonts/Roboto-Regular.ttf")
                    textbutton _("OpenSans") action gui.SetPreference("font", "fonts/OpenSans-Regular.ttf")
                    textbutton _("Corleone") action gui.SetPreference("font", "fonts/Corleone.ttf")
                    textbutton _("Oswald") action gui.SetPreference("font", "fonts/Oswald-Regular.ttf")
                    textbutton _("DancingScript") action gui.SetPreference("font", "fonts/DancingScript-Bold.ttf")

                vbox:
                    style_prefix "check"
                    label _("Skip")
                    textbutton _("Unseen Text") action Preference("skip", "toggle")
                    textbutton _("After Choices") action Preference("after choices", "toggle")
                    textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))

                ## Additional vboxes of type "radio_pref" or "check_pref" can be
                ## added here, to add additional creator-defined preferences.

            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("Text Speed")

                    bar value Preference("text speed")

                    label _("Auto-Forward Time")

                    bar value Preference("auto-forward time")

                vbox:

                    if config.has_music:
                        label _("Music Volume")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("Sound Volume")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)



                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Mute All"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"


# init -2 python:
#     renpy.register_style_preference("font", "DancingScript-Bold", style.default, "font", "fonts/DancingScript-Bold.ttf")
#     renpy.register_style_preference("font", "OpenSans-Regular", style.default, "font", "fonts/OpenSans-Regular.ttf")
#     renpy.register_style_preference("font", "Roboto-Regular", style.default, "font", "fonts/Roboto-Regular.ttf")

style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")

style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 675


# History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False

    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):

        style_prefix "history"

        for h in _history_list:
            window:
                ## This lays things out properly if history_height is None.
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"

                        ## Take the color of the who text from the Character, if
                        ## set.
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what

        if not _history_list:
            label _("The dialogue history is empty.")


## This determines what tags are allowed to be displayed on the history screen.

define gui.history_allow_tags = set()


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("Help"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 23

            hbox:

                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")


screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up\nClick Rollback Side")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")


    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.button_text_properties("help_button")

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0

## Help game stuff
init -2 python:
    #declares a new style called "gamehelp"
    style.gamehelp = Style(style.default)
    style.gamehelp_text.size = 22
    style.gamehelp_text.line_spacing = 3
    style.gamehelp_text.outlines = [ (4, "#000", 1, 1) ]

    # style.infoscreen_button.idle_background = Frame("images/square.png", 10, 10)
    # style.infoscreen_button.hover_background = Frame("images/square.png", 10, 10)
    style.gamehelp_button_text.idle_color = "d8d2b8"
    style.gamehelp_button_text.hover_color = "#ffffff"
    style.gamehelp_button_text.selected_color = "#dbb200"
    style.gamehelp_button_text.outlines = [ (1, "#000", 1, 1) ]
    style.gamehelp_button.top_padding = 5
    style.gamehelp_button.bottom_padding = 5

##############################################################################
# Quick Menu
#
# A screen that's included by the default say screen, and adds quick access to
# several useful functions.
screen quick_menu:

    # Add an in-game quick menu.
    hbox:
        style_group "quick"

        xalign 0.89
        yalign 0.96

        textbutton _("Q.Save") action QuickSave()
        textbutton _("Q.Load") action QuickLoad()
        textbutton _("Save") action ShowMenu('save')
        textbutton _("Skip") action Skip()
        textbutton _("Auto") action Preference("auto-forward", "toggle")
        textbutton _("Prefs") action ShowMenu('preferences')

init -2 python:
    style.quick_button.set_parent('default')
    style.quick_button.background = None
    style.quick_button.xpadding = 5

    style.quick_button_text.set_parent('default')
    style.quick_button_text.size = 18
    style.quick_button_text.idle_color = "#292931"
    style.quick_button_text.hover_color = "#ccc"
    style.quick_button_text.selected_idle_color = "#2d2d3c"
    style.quick_button_text.selected_hover_color = "#cc0"
    style.quick_button_text.insensitive_color = "#4448"

    # Set a default value for the auto-forward time, and note that AFM is
    # turned off by default.
    config.default_afm_time = 10
    config.default_afm_enable = False


##############################################################################
# Choice
#
# Screen that's used to display in-game menus.
# http://www.renpy.org/doc/html/screen_special.html#choice

screen choice:

    window:
        style "menu_window"
        xalign 0.5
        yalign 0.5

        vbox:
            style "menu"
            spacing 2

            for caption, action, chosen in items:

                if action:

                    button:
                        action action
                        style "menu_choice_button"

                        text caption style "menu_choice" color "#000" size 36

                else:
                    text caption style "menu_caption" color "#fff"

init -2 python:
    style.menu_window.set_parent(style.default)
    style.menu_choice.set_parent(style.button_text)
    style.menu_choice.clear()
    #style.menu_choice_button.padding=20
    style.menu_choice_button.set_parent(style.button)
    style.menu_choice_button.xminimum = int(config.screen_width * 0.8)
    style.menu_choice_button.xmaximum = int(config.screen_width * 0.9)

    style.menu_choice_button.yminimum=60
#    style.menu_choice_button_text.color = "#fff"
    style.menu_choice_button.background = Frame("gui/frame.png",22,22)



init:
    $ extras_items = ["cg_gallery", "ch_gallery", "bg_gallery", "music_room"]

    image button_ch_gallery = At(LiveComposite ((335, 74), (0,0), "gui/side_button.png",(19, 19), "gui/icon_ch_gallery.png",  (77, 18), Text("Char. Art", style="side_butt")), side_eff)
    image button_ch_gallery_selected_idle = At(LiveComposite ((335, 74), (0,0), "gui/side_button_selected.png", (19, 19), "gui/icon_ch_gallery.png",   (77, 18), Text("Characters", style="side_butt")), side_eff_selected_idle)
    image button_ch_gallery_selected_hover = At(LiveComposite ((335, 74), (0,0), "gui/side_button_selected.png", (19, 19), "gui/icon_ch_gallery.png",  (77, 18), Text("Characters", style="side_butt")), side_eff_selected_hover)

    image button_bg_gallery = At(LiveComposite ((335, 74), (0,0), "gui/side_button.png",(19, 19), "gui/icon_bg_gallery.png",  (77, 18), Text("BG Art", style="side_butt")), side_eff)
    image button_bg_gallery_selected_idle = At(LiveComposite ((335, 74), (0,0), "gui/side_button_selected.png", (19, 19), "gui/icon_bg_gallery.png", (77, 18), Text("BG Art", style="side_butt")), side_eff_selected_idle)
    image button_bg_gallery_selected_hover = At(LiveComposite ((335, 74), (0,0), "gui/side_button_selected.png", (19, 19), "gui/icon_bg_gallery.png", (77, 18), Text("BG Art", style="side_butt")), side_eff_selected_hover)

    image button_cg_gallery = At(LiveComposite ((335, 74), (0,0), "gui/side_button.png", (19, 19), "gui/icon_cg_gallery.png",  (77, 18), Text("CG Art", style="side_butt")), side_eff)
    image button_cg_gallery_selected_idle = At(LiveComposite ((335, 74), (0,0), "gui/side_button_selected.png", (19, 19), "gui/icon_cg_gallery.png",  (77, 18), Text("CG Art", style="side_butt")), side_eff_selected_idle)
    image button_cg_gallery_selected_hover = At(LiveComposite ((335, 74), (0,0), "gui/side_button_selected.png", (19, 19), "gui/icon_cg_gallery.png",  (77, 18), Text("CG Art", style="side_butt")), side_eff_selected_hover)

    image button_music_room = At(LiveComposite ((335, 74), (0,0), "gui/side_button.png", (19, 19), "gui/icon_jukebox.png",  (77, 18), Text("Jukebox", style="side_butt")), side_eff)
    image button_music_room_selected_idle = At(LiveComposite ((335, 74), (0,0), "gui/side_button_selected.png", (19, 19), "gui/icon_jukebox.png",  (77, 18), Text("Jukebox", style="side_butt")), side_eff_selected_idle)
    image button_music_room_selected_hover = At(LiveComposite ((335, 74), (0,0), "gui/side_button_selected.png", (19, 19), "gui/icon_jukebox.png",  (77, 18), Text("Jukebox", style="side_butt")), side_eff_selected_hover)

    image button_return = At(LiveComposite ((335, 74), (0,0), "gui/side_button.png", (19, 19), "gui/icon_return.png", (77, 18), Text("Return", style="side_butt")), side_eff)
    image button_return_selected_idle = At(LiveComposite ((335, 74), (0,0), "gui/side_button_selected.png", (19, 19), "gui/icon_return.png", (77, 18), Text("CG Art", style="side_butt")), side_eff_selected_idle)
    image button_return_selected_hover = At(LiveComposite ((335, 74), (0,0), "gui/side_button_selected.png", (19, 19), "gui/icon_return.png", (77, 18), Text("CG Art", style="side_butt")), side_eff_selected_hover)

init -1:
    transform side_eff:
        on idle:
            alpha .8
            easein 0.5 xpos 0
        on hover:
            alpha 1.0
            easein 0.3 xpos 20
            easein 0.3 xpos -20
    transform side_eff_selected_idle:
        alpha .8
        easein 0.5 xpos 0
    transform side_eff_selected_hover:
        alpha 1.0
        #easein 0.3 xpos 20
        #easein 0.3 xpos -20
    transform side_eff_insensitive:
        alpha .2
        xpos 0

screen extras:
    add "main_menu_cg_foggy"
    add "gui/main_menu_ground.png"
    add "gui/game_menu_ground.png"
    add "gui/extras_ground.png"
    $ y = 129
    vbox xpos 1020 ypos 129 spacing 9:
        for item in extras_items:
            $ button_name = "button_" + item
            $ button_name_selected_idle = button_name + "_selected_idle"
            $ button_name_selected_hover = button_name + "_selected_hover"
            $ tip_name = "tooltip_extras_" + item
            button background None focus_mask True action ShowMenu(item) hovered [ Play ("sound", "sfx/click.wav"), Show("gui_tooltip", my_picture=tip_name) ] unhovered [Hide("gui_tooltip")]:
                add button_name
                selected_idle_child button_name_selected_idle
                selected_hover_child button_name_selected_hover
        button background None focus_mask True action Return() hovered [ Play ("sound", "sfx/click.wav"), Show("gui_tooltip", my_picture="tooltip_game_menu_return") ] unhovered [Hide("gui_tooltip")]:
            add "button_return"
            selected_idle_child "button_return_selected_idle"
            selected_hover_child "button_return_selected_hover"

screen extras_blank:
    tag menu # This ensures that any other menu screen is replaced.
    use extras # We include the extras navigation screen
    add "extras_title" xpos 152 ypos 20

init:
    #emenies redefined, without an underscore, as simple images
    image enemy1 future = "maze/enemy1_future.png"
    image enemy1 past = "maze/enemy1_past.png"
    image enemy1 present = "maze/enemy1_present.png"
    image enemy1 space = "maze/enemy1_space.png"

    image enemy2 future = "maze/enemy2_future.png"
    image enemy2 past = "maze/enemy2_past.png"
    image enemy2 present = "maze/enemy2_present.png"
    image enemy2 space = "maze/enemy2_space.png"

    image enemy3 future = "maze/enemy3_future.png"
    image enemy3 past = "maze/enemy3_past.png"
    image enemy3 present = "maze/enemy3_present.png"
    image enemy3 space = "maze/enemy3_space.png"

    image enemy4 future = "maze/enemy4_future.png"
    image enemy4 past = "maze/enemy4_past.png"
    image enemy4 present = "maze/enemy4_present.png"
    image enemy4 space = "maze/enemy4_space.png"

    image enemyb1 future = "maze/enemyb1_future.png"
    image enemyb2 future = "maze/enemyb2_future.png"
    image enemyb1 past = "maze/enemyb1_past.png"
    image enemyb2 past = "maze/enemyb2_past.png"
    image enemyb1 present = "maze/enemyb1_present.png"
    image enemyb2 present = "maze/enemyb2_present.png"
    image enemyb1 space = "maze/enemyb1_space.png"
    image enemyb2 space = "maze/enemyb2_space.png"

    image ten neutral = "sprites/ten_smile.png"
    image ten frown = "sprites/ten_frown.png"
    image ten embarressed = "sprites/ten_embarrassed.png"
    image ten cry = "sprites/ten_cry.png"
    image ten worried = "sprites/ten_worried.png"
    image ten shock = "sprites/ten_shock.png"
    image ten nervous = "sprites/ten_nervous.png"
    image ten scared = "sprites/ten_scared.png"
    image ten upset = "sprites/ten_upset.png"

#Galleries:
init python:
    #Galleries settings - start

    #list the CG gallery images here:
    gallery_cg_items = ["angeldead", "orphanend", "secondend", "angel_endcg"]
    #list the BG gallery images here:
    gallery_bg_items = ["bg restaurant side", "bg park1", "bg store womens", "bg sidewalk", "bg home", "bg livingroom"]

    # list one image for each sprite (neutral) here:
    gallery_ch_items = ["seconds open", "angel neutral", "ten neutral", "enemy1 present", "enemy2 present", "enemy3 present", "enemy4 present", "enemyb1 future"]
    #list the images for the rest of expressions for each sprite here:
    gallery_seconds = ["seconds mouth", "seconds floppy", "seconds close", "seconds floppyg", "seconds mouthg", "seconds openg"]
    gallery_angel = ["angel laughing", "angel sad", "angel upset", "angel nervous"]
    gallery_ten = ["ten frown", "ten embarressed", "ten cry", "ten worried", "ten shock", "ten nervous", "ten scared", "ten upset"]

    gallery_enemy1 = ["enemy1_past", "enemy1_space", "enemy1_future"]
    gallery_enemy2 = ["enemy2_past", "enemy2_space", "enemy2_future"]
    gallery_enemy3 = ["enemy3_past", "enemy3_space", "enemy3_future"]
    gallery_enemy4 = ["enemy4_past", "enemy4_space", "enemy4_future"]
    gallery_enemy4 = ["enemy4_past", "enemy4_space", "enemy4_future"]
    gallery_enemyb = ["enemyb2_future", "enemyb1_past", "enemyb2_past", "enemyb1_space", "enemyb2_space", "enemyb1_present", "enemyb2_present"]

    gallery_dev_items = ["angel_concept", "enemy1_lineart", "failattemptatangeldeath", "ghostbosses_concept", "main_menu_mockup2", "minienemies", "second_concept", "ten_concept", "title_screen_sketch"]

    #how many rows and columns in the gallery screens?
    gal_rows = 3
    gal_cols = 3
    #thumbnail size in pixels:
    thumbnail_x = 267
    thumbnail_y = 150
    gal_xpos = 50
    gal_ypos = 120
    #Galleries settings - end

    gal_cells = gal_rows * gal_cols

    g_cg = Gallery()
    for gal_item in gallery_cg_items:
        g_cg.button(gal_item + " butt")
        g_cg.image(gal_item)
        g_cg.unlock(gal_item)
    g_cg.transition = fade
    cg_page=0

    g_dev = Gallery()
    for gal_item in gallery_dev_items:
        g_dev.button(gal_item + " butt")
        g_dev.image("#000", gal_item)
        #g_dev.unlock(gal_item)

    g_dev.transition = fade
    dev_page=0

    g_bg = Gallery()
    for gal_item in gallery_bg_items:
        g_bg.button(gal_item + " butt")
        if gal_item == "bg park1":
            g_bg.image(gal_item, "bg park")
        else:
            g_bg.image(gal_item)
        g_bg.unlock(gal_item)

        #BGs with variations:
        if gal_item == "bg restaurant side":
            g_bg.image("bg restaurant nofood", "restaurant_table nofood")
            g_bg.unlock("bg restaurant nofood")
            g_bg.image("bg restaurant food", "restaurant_table food")
            g_bg.unlock("bg restaurant food")
        if gal_item == "bg store womens":
            g_bg.image( "bg store mens")
            g_bg.unlock("bg store mens")
    g_bg.transition = fade
    bg_page=0

    g_ch = Gallery()
    for gal_item in gallery_ch_items:
        g_ch.button(gal_item + " butt")
        if gal_item=="seconds open":
            g_ch.image("#000", gal_item)
            g_ch.unlock(gal_item)
            for item in gallery_seconds:
                g_ch.image("#000", item)
                g_ch.unlock(item)

        if gal_item=="angel neutral":
            g_ch.image("#000", gal_item)
            g_ch.unlock(gal_item)
            for item in gallery_angel:
                g_ch.image("#000", item)
                g_ch.unlock(item)


        if gal_item=="ten neutral":
            g_ch.image("#000", gal_item)
            #g_ch.unlock(gal_item)
            for item in gallery_ten:
                g_ch.image("#000", item)
                #g_ch.unlock(item)

        if gal_item=="enemy1 present":
            g_ch.image("#000", gal_item)
            g_ch.unlock(gal_item.replace(' ', '_'))
            for item in gallery_enemy1:
                g_ch.image("#000", item.replace('_', ' '))
                g_ch.unlock(item.replace(' ', '_'))

        if gal_item=="enemy2 present":
            g_ch.image("#000", gal_item)
            g_ch.unlock(gal_item.replace(' ', '_'))
            for item in gallery_enemy2:
                g_ch.image("#000", item.replace('_', ' '))
                g_ch.unlock(item.replace(' ', '_'))

        if gal_item=="enemy3 present":
            g_ch.image("#000", gal_item)
            g_ch.unlock(gal_item.replace(' ', '_'))
            for item in gallery_enemy3:
                g_ch.image("#000", item.replace('_', ' '))
                g_ch.unlock(item.replace(' ', '_'))

        if gal_item=="enemy4 present":
            g_ch.image("#000", gal_item)
            g_ch.unlock(gal_item.replace(' ', '_'))
            for item in gallery_enemy4:
                g_ch.image("#000", item.replace('_', ' '))
                g_ch.unlock(item.replace(' ', '_'))

        if gal_item=="enemyb1 future":
            g_ch.image("#000", gal_item)
            g_ch.unlock(gal_item.replace(' ', '_'))
            for item in gallery_enemyb:
                g_ch.image("#000", item.replace('_', ' '))
                g_ch.unlock(item.replace(' ', '_'))

    g_ch.transition = fade
    ch_page=0

init:
    $ border_size=6
    #image gal_bg=LiveComposite((thumbnail_x, thumbnail_y), (0,0), Solid("CECECE"), (border_size,border_size), LiveComposite((thumbnail_x-border_size*2, thumbnail_y-border_size*2), (0,0), Solid("000")))
    image gal_bg=LiveComposite((thumbnail_x, thumbnail_y), (0,0), Solid("dadada"))

    image gal_frame_x=LiveComposite((thumbnail_x, border_size), (0,0), Solid("CECECE"))
    image gal_frame_y=LiveComposite((border_size, thumbnail_y-border_size*2), (0,0), Solid("CECECE"))
    image gal_frame_x_sel=LiveComposite((thumbnail_x, border_size), (0,0), Solid("4abff2"))
    image gal_frame_y_sel=LiveComposite((border_size, thumbnail_y-border_size*2), (0,0), Solid("4abff2"))

init +1:
    image gal_locked=LiveComposite((thumbnail_x, thumbnail_y), (0,0), ImageReference("gal_bg"), (42,50), Text("Locked", style="title"))

    image gal_frame=LiveComposite((thumbnail_x, thumbnail_y), (border_size*2,1), ImageReference("gal_frame_x"), (border_size*2,thumbnail_y-border_size+1), ImageReference("gal_frame_x"), (border_size*2,border_size+1), ImageReference("gal_frame_y"), (thumbnail_x+border_size,border_size+1), ImageReference("gal_frame_y"))

    image gal_frame_sel=LiveComposite((thumbnail_x, thumbnail_y), (border_size*2,1), ImageReference("gal_frame_x_sel"), (border_size*2,thumbnail_y-border_size+1), ImageReference("gal_frame_x_sel"), (border_size*2,border_size+1), ImageReference("gal_frame_y_sel"), (thumbnail_x+border_size,border_size+1), ImageReference("gal_frame_y_sel"))

# init +1 python:
    #Here we create the thumbnails. We create a grayscale thumbnail image for BGs, but we use a special "locked" image for CGs to prevent spoilers.
    # for gal_item in gallery_cg_items:
    #     renpy.image (gal_item + " butt", im.Scale(ImageReference(gal_item), thumbnail_x, thumbnail_y))
    # for gal_item in gallery_bg_items:
    #     renpy.image (gal_item + " butt", im.Scale(ImageReference(gal_item), thumbnail_x, thumbnail_y))
#     for gal_item in gallery_dev_items:
# #        renpy.image (gal_item + " butt", LiveComposite((thumbnail_x, thumbnail_y), (0,0), ImageReference("gal_bg"), (int(thumbnail_x/4),0), ProportionalScale(ImageReference(gal_item), thumbnail_x, thumbnail_y)))
#         renpy.image (gal_item + " butt", im.Scale(ImageReference(gal_item), thumbnail_x, thumbnail_y))
#     for gal_item in gallery_ch_items:
# #        renpy.image (gal_item + " butt", LiveComposite((thumbnail_x, thumbnail_y), (0,0), ImageReference("gal_bg"), (9+int(thumbnail_x/4),5), ProportionalScale(ImageReference(gal_item), thumbnail_x, thumbnail_y) ))
        # renpy.image (gal_item + " butt", LiveComposite((thumbnail_x, thumbnail_y), (0,0), ImageReference("gal_bg"), (int(thumbnail_x/4),0), ProportionalScale(ImageReference(gal_item), thumbnail_x, thumbnail_y)))

screen cg_gallery:
    tag menu
    use extras
    add "cg_gallery_title" xpos 152 ypos 22
    frame background None xpos gal_xpos ypos gal_ypos:
        grid gal_rows gal_cols:
            ypos 10
            $ i = 0
            $ next_cg_page = cg_page + 1
            if next_cg_page > int(len(gallery_cg_items)/gal_cells):
                $ next_cg_page = 0
            for gal_item in gallery_cg_items:
                $ i += 1
                if i <= (cg_page+1)*gal_cells and i>cg_page*gal_cells:
                    add g_cg.make_button(gal_item + " butt", gal_item + " butt", ImageReference("gal_locked"), ImageReference("gal_frame_sel"), ImageReference("gal_frame"), background=None, bottom_margin=24)

            for j in range(i, (cg_page+1)*gal_cells): #we need this to fully fill the grid
                null
        frame:
            yalign 0.97
            vbox:
                if len(gallery_cg_items)>gal_cells:
                    textbutton _("Next Page") action [SetVariable('cg_page', next_cg_page), ShowMenu("cg_gallery")]

screen bg_gallery:
    tag menu
    use extras
    add "bg_gallery_title" xpos 152 ypos 22
    frame background None xpos gal_xpos ypos gal_ypos:
        grid gal_rows gal_cols:
            ypos 10
            $ i = 0
            $ next_bg_page = bg_page + 1
            if next_bg_page > int(len(gallery_bg_items)/gal_cells):
                $ next_bg_page = 0
            for gal_item in gallery_bg_items:
                $ i += 1
                if i <= (bg_page+1)*gal_cells and i>bg_page*gal_cells:
                    add g_bg.make_button(gal_item + " butt", gal_item + " butt", ImageReference("gal_locked"), ImageReference("gal_frame_sel"), ImageReference("gal_frame"), background=None, bottom_margin=24)
                    #add g_bg.make_button(gal_item + " butt", gal_item + " butt", gal_item + " butt dis", xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
            for j in range(i, (bg_page+1)*gal_cells):
                null
        frame:
            yalign 0.97
            vbox:
                if len(gallery_bg_items)>gal_cells:
                    textbutton _("Next Page") action [SetVariable('bg_page', next_bg_page), ShowMenu("bg_gallery")]

screen ch_gallery:
    tag menu
    use extras
    add "character_gallery_title" xpos 152 ypos 22
    frame background None xpos gal_xpos ypos gal_ypos:
        grid gal_rows gal_cols:
            ypos 10
            $ i = 0
            $ next_ch_page = ch_page + 1
            if next_ch_page > int(len(gallery_ch_items)/gal_cells):
                $ next_ch_page = 0
            for gal_item in gallery_ch_items:
                $ i += 1
                if i <= (ch_page+1)*gal_cells and i>ch_page*gal_cells:
                    add g_ch.make_button(gal_item + " butt", gal_item + " butt", ImageReference("gal_locked"), ImageReference("gal_frame_sel"), ImageReference("gal_frame"), background=None, bottom_margin=24)
            for j in range(i, (ch_page+1)*gal_cells):
                null
        frame:
            yalign 0.97
            vbox:
                if len(gallery_ch_items)>gal_cells:
                    textbutton _("Next Page") action [SetVariable('ch_page', next_ch_page), ShowMenu("ch_gallery")]

screen dev_gallery:
    tag menu
    use extras
    add "concept_gallery_title" xpos 152 ypos 22
    frame background None xpos gal_xpos ypos gal_ypos:
        grid gal_rows gal_cols:
            ypos 10
            $ i = 0
            $ next_dev_page = dev_page + 1
            if next_dev_page > int(len(gallery_dev_items)/gal_cells):
                $ next_dev_page = 0
            for gal_item in gallery_dev_items:
                $ i += 1
                if i <= (dev_page+1)*gal_cells and i>dev_page*gal_cells:
                    add g_dev.make_button(gal_item + " butt", gal_item + " butt", ImageReference("gal_locked"), ImageReference("gal_frame_sel"), ImageReference("gal_frame"), background=None, bottom_margin=24)
                    #add g_dev.make_button(gal_item + " butt", gal_item + " butt", im.Scale("gui/gal_locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
            for j in range(i, (dev_page+1)*gal_cells): #we need this to fully fill the grid
                null
        frame:
            yalign 0.97
            vbox:
                if len(gallery_dev_items)>gal_cells:
                    textbutton _("Next Page") action [SetVariable('dev_page', next_dev_page), ShowMenu("dev_gallery")]


# init +1 python:
#     # Step 1. Create a MusicRoom instance.
#     mr = MusicRoom(fadeout=1.0)
#     # Step 2. Add music files.
#     mr.add(HAPPY, always_unlocked=True)
#     # mr.add(SAD)
#     mr.add(DRAMATIC)
#     mr.add(MAZE)
#     mr.add(COMBAT)

screen music_room:
    tag menu
    use extras
    add "music_room_title" xpos 152 ypos 22

    #window background None xpos gal_xpos ypos gal_ypos xminimum 690 yminimum 380: # xalign 0.5 yalign 0.5:

    frame background None xpos 250 ypos 150:
        has vbox spacing 15
        # The buttons that play each track.
        textbutton "Ultra Generic Repetitive Cliché Happy Theme" #action mr.Play(HAPPY)
        # textbutton "My Lost Rain" action mr.Play(SAD)
        textbutton "Revelation" #action mr.Play(DRAMATIC)
        textbutton "Myst Myst"# action mr.Play(MAZE)
        textbutton "Myst Combat" #action mr.Play(COMBAT)
        null height 20

        # Buttons that let us advance tracks.
    # hbox xpos 260 ypos 570 spacing 50:
        # textbutton "Previous" action mr.Previous()
        # textbutton "Next" action mr.Next()
        # null height 20

    # Start the music playing on entry to the music room.
    # on "replace" action mr.Play()
    # Restore the main menu music upon leaving.
    on "replaced" action Play("music", config.main_menu_music)

init -1 python:
    #styling the button for the jukebox and elsewhere
    style.button.background=Frame("gui/frame.png",25,25)
    style.button.yminimum=52
    style.button.xminimum=52
    style.button_text.color="000000DD"
    style.button_text.selected_color="4abff2"
    style.button_text.insensitive_color="fff"
    style.button_text.outlines=[(2, "00000000", 0, 0)]
    style.button_text.hover_outlines=[(2, "ffffff", 0, 0)]
    style.button_text.insensitive_outlines=[(2, "00000000", 0, 0)]
    style.button_text.selected_outlines=[(2, "00000040", 0, 0)]
    style.button_text.selected_hover_outlines=[(2, "ffffffa0", 0, 0)]

    if renpy.variant("touch"):
        style.button.yminimum=52*2
        style.button.xminimum=52*2
        style.button_text.size=32


    #Screen titles:
    style.title = Style(style.default)
    style.title.size=32
    style.title.bold=True
    style.title.font="gui/animeace2_reg.ttf"
    style.title.outlines=[(3, "4abff2", 0, 0)]
    style.title.color="fff"

    style.side_butt = Style(style.title)
    style.side_butt.size=28
    style.side_butt.bold=False
    style.side_butt.outlines=[(2, "4abff2", 0, 0), (0, "4abff2", 3, 3), (0, "4abff2", 4, 4)]

    #Tooltips:
    style.tips_top = Style(style.default)
    #style.title.font="gui/arial.ttf"
    style.tips_top.size=14
    style.tips_top.color="fff"
    style.tips_top.outlines=[(3, "6b7eef", 0,0)]
    style.tips_top.kerning = 5

    style.tips_bottom = Style(style.tips_top)
    style.tips_top.size=20
    style.tips_bottom.outlines=[(0, "6b7eef", 1, 1), (0, "6b7eef", 2, 2)]
    style.tips_bottom.kerning = 2

init:
    #Screen titles:
    image extras_title=Text("extras", style="title")
    image cg_gallery_title=Text("CG gallery", style="title")
    image character_gallery_title=Text("character gallery", style="title")
    image bg_gallery_title=Text("BG gallery", style="title")
    image concept_gallery_title=Text("concept gallery", style="title")
    image music_room_title=Text("Jukebox", style="title")

    image help_title=Text("Help", style="title")

    #Tooltips - game menu:
    image tooltip_game_menu_save=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text("Save a game in progress", style="tips_bottom"))
    image tooltip_game_menu_load=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text("Load a game in progress", style="tips_bottom"))
    image tooltip_game_menu_config=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text("Configure the game settings", style="tips_bottom"))
    image tooltip_game_menu_main=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text("Return to main menu", style="tips_bottom"))
    image tooltip_game_menu_quit=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text("Quit the game :(", style="tips_bottom"))
    image tooltip_game_menu_return=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text("Return to the previous screen", style="tips_bottom"))

    #Tooltips - main menu
    image tooltip_main_menu_start=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text("Start a new game", style="tips_bottom"))
    image tooltip_main_menu_extras=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text("View the additional unlockable\ncontent", style="tips_bottom"))
    # tooltip_main_menu_load, tooltip_main_menu_config and tooltip_main_menu_quit doesn't exist. Use tooltip_game_menu_load, tooltip_game_menu_config and tooltip_game_menu_quit instead

    image tooltip_main_menu_help=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text("View the game help.", style="tips_bottom"))

    #Tooltips - extras:
    image information = Text("INFORMATION", style="tips_top")
    image tooltip_extras_cg_gallery=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text("View the event CG Gallery", style="tips_bottom"))
    image tooltip_extras_ch_gallery=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text("View the characters Gallery", style="tips_bottom"))
    image tooltip_extras_bg_gallery=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text("View the backgrounds Gallery", style="tips_bottom"))
    image tooltip_extras_music_room=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text("Listen to the music", style="tips_bottom"))
    image tooltip_extras_dev_gallery=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text("View the concepts and sketches", style="tips_bottom"))
    # tooltip_extras_dev_return doesn't exist. Use tooltip_game_menu_return instead.

    #Tooltips - options:
    image tooltip_config_windowed=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text("Toggle windowed mode", style="tips_bottom"))
    image tooltip_config_fullscreen=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text("Toggle fullscreen mode", style="tips_bottom"))
    image tooltip_config_enable_transition=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text("Enable in-game transitions", style="tips_bottom"))
    image tooltip_config_enable_transition=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text("Disble in-game transitions", style="tips_bottom"))
    image tooltip_config_stop_skip=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text("Stop fast skipping after a choice", style="tips_bottom"))
    image tooltip_config_go_skip=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text("Resume fast skipping after a choice", style="tips_bottom"))
    image tooltip_config_seen=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text("Fast skip text that has already been seen", style="tips_bottom"))
    image tooltip_config_all=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text("Fast skip all text regardless of whether\nit has already been seen or not", style="tips_bottom"))
    image tooltip_config_skipping=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text("Turn on game skipping", style="tips_bottom"))

    #Tooltips-inventory:
    image tooltip_inventory_chocolate=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text("Generic chocolate to heal\n50 points of health. For Ten.", style="tips_bottom"))
    image tooltip_inventory_chips=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text("Salty chips heal 100 points\nof health. For Ten.", style="tips_bottom"))
    image tooltip_inventory_cola=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text("Ice cold cola recharges 25 Bullet\nPoints for Energy Guns For Ten.", style="tips_bottom"))
    image tooltip_inventory_banana=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text("A healthy banana full of potassium! Recharges\n50 Bullet Points for Energy Guns. For Ten.", style="tips_bottom"))
    image tooltip_inventory_bone=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text("Some old bone from who knows where.\nHeals 100 points of health. For Seconds.", style="tips_bottom"))
    image tooltip_inventory_treat=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text("Scrumptious dog treat that heals\n50 points of health. For Seconds.", style="tips_bottom"))
    image tooltip_inventory_gun=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text("An energy gun that looks like something a cop would\ncarry around. Most effective on enemies from the Present.", style="tips_bottom"))
    image tooltip_inventory_laser=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text("An energy gun that shoots photon beams.\nMost effective on enemies from the Future.", style="tips_bottom"))
    image tooltip_inventory_musket=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text("An energy gun that resembles an old musket from days\nlong gone. Most effective on enemies from the Past.", style="tips_bottom"))



#    $ extras_items = ["cg_gallery", "ch_gallery", "bg_gallery", "music_room", "dev_gallery"]



#function to resize the characters:
init python:
    class ProportionalScale(im.ImageBase): # A mix between im.Scale and im.FactorScale for character images
        def __init__(self, imgname, maxwidth, maxheight, bilinear=True, **properties):
            img = im.image(imgname)
            super(ProportionalScale, self).__init__(img, maxwidth, maxheight, bilinear, **properties)
            self.imgname = imgname
            self.image = img
            self.maxwidth = int(maxwidth)
            self.maxheight = int(maxheight)
            self.bilinear = bilinear

        def load(self):
            child = im.cache.get(self.image)
            currentwidth, currentheight = child.get_size()
            xscale = 1.0
            yscale = 1.0
            if (currentwidth > self.maxwidth):
                xscale = float(self.maxwidth) / float(currentwidth)
            if (currentheight > self.maxheight):
                yscale = float(self.maxheight) / float(currentheight)
            if (xscale < yscale):
                minscale = xscale
            else:
                minscale = yscale
            newwidth = currentwidth * minscale
            newheight = currentheight * minscale
            #renpy.log("Loading image %s from %f x %f to %f x %f" % (self.imgname, currentwidth , currentheight , newwidth, newheight)) # Debug code to see when the loading really happens
            if self.bilinear:
                try:
                    renpy.display.render.blit_lock.acquire()
                    rv = renpy.display.scale.smoothscale(child, (newwidth, newheight))
                finally:
                    renpy.display.render.blit_lock.release()
            else:
                try:
                    renpy.display.render.blit_lock.acquire()
                    rv = renpy.display.pgrender.transform_scale(child, (newwidth, newheight))
                finally:
                    renpy.display.render.blit_lock.release()
            return rv
        def predict_files(self):
            return self.image.predict_files()

screen help:
    variant "touch"
    tag menu
    use navigation
    add "help_title" xpos 152 ypos 22
    frame background None xpos 50 ypos 80 xmaximum 900:
        style_group "help"
        has vbox spacing 15
        text "Story mode:" size 40
        text "To advance through the game, tap the screen."
        text "{b}Menu key{/b} Enter the game menu or returns to the game."
        text "{b}Home:{/b} Returns to the Android home screen, suspending the game. The game will be automatically saved and the save will be automatically loaded when you return to the game."
        text "{b}Back:{/b} Rollback to view previous text."
        text "{b}Volume Up, Volume Down:{/b} Controls volume."
    textbutton "Next Page" xpos 50 ypos .75 action ShowMenu('help2')

screen help:
    tag menu
    use navigation
    add "help_title" xpos 152 ypos 22
    frame background None xpos 50 ypos 80 xmaximum 900:
        style_group "help"
        has vbox spacing 15
        text "Story mode:" size 40
        text "To advance through the game, {b}left-click{/b} or press the {b}space{/b} or {b}enter{/b} key. Any time during gameplay, you can right-click or press the escape key to enter the game menu."
        text "{b}CTRL Key:{/b} Hold to skip text."
        #text "{b}TAB Key:{/b} Press once to begin skipping text, press again to stop."
        text "{b}PageUp Key, Mousewheel-Up:{/b} Rollback to view previous text."
        text "{b}PageDown Key, Mousewheel-Down:{/b} Move forward in rollback text."
        text "{b}F Key:{/b} Toggle fullscreen and window mode."
        text "{b}P Key:{/b} Take a screenshot."
    textbutton "Next Page" xpos 50 ypos .88 action ShowMenu('help2')

screen help2:
    tag menu
    use navigation
    add "help_title" xpos 152 ypos 22
    frame background None xpos 50 ypos 80 xmaximum 900:
        style_group "help"
        has vbox spacing 20
        text "Combat mode - Ten:" size 40

        #player = Actor("Ten",100, [Punch, Kick, Shoot, Defend, Inventory_sk], max_mp=50)
        #dog = Actor("Seconds",100, [Bite, Scratch, Charge, Defend])

        #for action in for item in loot_items:
        text "{b}Defend:{/b} Reduces the damage taken by 50% for the next move."
        text "{b}Punch:{/b} Damages the enemy for [Punch.power]HP. [Punch.hit]% accuracy."
        text "{b}Kick:{/b} Damages the enemy for [Kick.power]HP. [Kick.hit]% accuracy."
        text "{b}Shoot:{/b} Damages the enemy for [Shoot.power]HP. [Shoot.hit]% accuracy. Requires [Shoot.mp]EP. Different guns may cause more or less damage on different enemy types."
        text "{b}Inventory:{/b} Open the inventory to use items or change the gun."
    textbutton "First Page" xpos 50 ypos .88 action ShowMenu('help')

init python:
    style.help = Style(style.default)
    style.help_text.size=32

    #style.title.font="gui/animeace2_reg.ttf"
    #style.title.outlines=[(3, "4abff2", 0, 0)]
    style.help_text.color="000"
