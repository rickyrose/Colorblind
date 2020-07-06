################################################################################
# This code defines all images used in this project, and attempts to organize  #
# the images based on what files use them. LiveComposite images left in their  #
# source code instead of being moved.                                          #
################################################################################

# Background images from lab_escape
image sewer_base = "maze/sewer_base.png"
image sewer_left1 = "maze/sewer_left1.png"
image sewer_right1 = im.Flip("maze/sewer_left1.png", horizontal=True)
image sewer_front1 = "maze/sewer_front1.png"
image sewer_left2 = "maze/sewer_left2.png"
image sewer_right2 = im.Flip("maze/sewer_left2.png", horizontal=True)
image sewer_front2 ="maze/sewer_front2.png"
image sewer_left3 = "maze/sewer_left3.png"
image sewer_right3 = im.Flip("maze/sewer_left3.png", horizontal=True)
image sewer_exit1 = "maze/sewer_exit1.png"
image sewer_exit2 = "maze/sewer_exit2.png"

image lab_base:
    "maze/lab_red_base.png" with Dissolve(1.0, alpha=True)
    2.0
    "maze/lab_dark_base.png"
    2.0
    repeat
image lab_left1 = "maze/lab_left1.png"
image lab_right1 = im.Flip("maze/lab_left1.png", horizontal=True)
image lab_front1 = "maze/lab_front1.png"
image lab_left2 = "maze/lab_left2.png"
image lab_right2 = im.Flip("maze/lab_left2.png", horizontal=True)
image lab_front2 ="maze/lab_front2.png"
image lab_left3 = "maze/lab_left3.png"
image lab_right3 = im.Flip("maze/lab_left3.png", horizontal=True)
image lab_exit1 = "maze/lab_exit1.png"
image lab_exit2 = "maze/lab_exit2.png"

image closet = "maze/closet.png"

# Images used for the navigation buttons in lab_escape (may be obsolete if
# Ricky's updated movement code is good)
image up_button = "gui/up_button.png"
image down_button = im.Flip("gui/up_button.png", vertical=True)
image right_buton = "gui/right_button.png"
image left_button = im.Flip("gui/right_button.png", horizontal=True)

# Temporary lab_escape background until proper artwork is received
image p_base = "maze/sewer_base.png"
image p_left1 = "maze/p_left1.png"
image p_right1 = im.Flip("maze/p_left1.png", horizontal=True)
image p_front1 = "maze/p_front1.png"
image p_left2 = "maze/p_left2.png"
image p_right2 = im.Flip("maze/p_left2.png", horizontal=True)
image p_front2 ="maze/p_front2.png"
image p_left3 = "maze/p_left3.png"
image p_right3 = im.Flip("maze/p_left3.png", horizontal=True)
image p_exit1 = "maze/lab_exit1.png"
image p_exit2 = "maze/lab_exit2.png"

# Enemy images, used in the definition of lab_escape enemies
image enemy1_pic:
    contains:
        "maze/dogs.png" #image names to be updated
    fly

image enemy2_pic:
    contains:
        "maze/haz_scientist.png"
    fly

image enemy3_pic:
    contains:
        "maze/robot.png"
    fly

image enemy4_pic:
    contains:
        "maze/soldier.png"
    fly

image enemy5_pic:
    "maze/enemyb1_future.png" with Dissolve(3.0, alpha=True)
    6.0
    "maze/enemyb3_future.png" with Dissolve(3.0, alpha=True)
    6.0
    # "maze/enemyb2.png" with Dissolve(3.0, alpha=True)
    # 6.0
    repeat

# Enemies redefined, without an underscore,
# as simple images for the Character Extras screen (in screens)
init:
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

    #Screen titles used in screens; will eventually be replaced or reformatted
    image extras_title=Text("extras", style="title")
    image cg_gallery_title=Text("CG gallery", style="title")
    image character_gallery_title=Text("character gallery", style="title")
    image bg_gallery_title=Text("BG gallery", style="title")
    image concept_gallery_title=Text("concept gallery", style="title")
    image music_room_title=Text("Jukebox", style="title")

    image help_title=Text("Help", style="title")

#Letters used in texting minigame
init:
    image letter a = "images/a.png"
    image letter b = "images/b.png"
    image letter c = "images/c.png"
    image letter d = "images/d.png"
    image letter e = "images/e.png"
    image letter f = "images/f.png"
    image letter g = "images/g.png"
    image letter h = "images/h.png"
    image letter i = "images/i.png"
    image letter j = "images/j.png"
    image letter k = "images/k.png"
    image letter l = "images/l.png"
    image letter m = "images/m.png"
    image letter n = "images/n.png"
    image letter o = "images/o.png"
    image letter p = "images/p.png"
    image letter q = "images/q.png"
    image letter r = "images/r.png"
    image letter s = "images/s.png"
    image letter t = "images/t.png"
    image letter u = "images/u.png"
    image letter v = "images/v.png"
    image letter w = "images/w.png"
    image letter x = "images/x.png"
    image letter y = "images/y.png"
    image letter z = "images/z.png"
    
# Background image used as placeholder for testing purposes
image bg park = "bg/ParkDuckless.jpg"
image bg party = "bg/9.png"
