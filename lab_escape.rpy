init -2 python:
    import renpy.store as store
    import renpy.exports as renpy
    import random
    from operator import attrgetter
    special_battle = False #for battles called outside of the dungeon

    encounter_chance = .8
    # img_pref = "lab_"
    img_pref = "p_"
    move_keys_visible = True
    inv_page = 0

    # Create skills (name, hit, power)
    Bomb = Skill("Bomb", 70, 30) #21 avg
    Taser = Skill("Taser", 70, 10) #7 avg
    Slash = Skill("Slash", 100, 20) #20 avg

    Magic = Skill("???", 40, 40, mp=25) #16 avg
    Punch = Skill("Punch", 90, 10)
    Kick = Skill("Kick", 70, 17)

    Bite = Skill("Bite", 70, 20) #14 avg
    Scratch = Skill("Scratch", 80, 10) #8 avg
    Charge = Skill("Charge", 60, 40) #24 avg

    Shoot = Skill("Shoot", 100, 40, ammo=1, element="bullets") #40 avg
    Defend = Skill("Defend", 0, 0, "defend")
    Inventory_sk = Skill("Inventory", 0, 0, "inventory")
    Flee = Skill("Run Away", 0, 0, "flee")

    # Create battle actors (name, max_hp, skills)

    Enemy1 = Actor("Guard Dogs",50,[Bite, Scratch], image="enemy1_pic", weak="bullets")

    Enemy2 = Actor("Scientist",65,[Taser], image="enemy2_pic", weak="bullets")

    Enemy3 = Actor("Robot",100,[Taser, Bomb], image="enemy3_pic", weak="none")

    Enemy4 = Actor("Soldier",80,[Bomb, Charge], image="enemy4_pic", weak="bullets")

    Enemy5 = Actor("Test Subject",10000,[Slash], image="enemy5_pic", weak="bullets")

    # Create maps. 1=wall, 2=exit, 3=entrance(entrance position must be also set in the script)


#image bg room= "lab.png"


#image semi stand = "girl6.png"
 

 #image semi walk:
  #   "girl1.png"
 #    0.3
#     "girl2.png"
#     0.3
#     "girl3.png"
#     0.3
 #    "girl4.png"
 #    0.3
 #    "girl5.png"
 #     0.3
 #   "girl6.png"
 #   0.3
 #   repeat
#position of characters
#    define sX=310
#    define sY=335
#    default mX=0
    
#    default dist=0
#    #checking what character is doing
#    default standWalk=0
    #background of room 0 is as far to the left as you can get
#    default rx= -1000

#    screen checkMouse():
#        if standWalk==0:
#        key "mousedown_1" action Jump ("checkDist")


#label start:
#    scene bg room:
#            xpos rx
#    show screen checkMouse

#label standRight
#    $ standWalk=0
    
#    show semi stand:
#    xpos sX
#    ypos sY
#    xzoom 1.0

#    $ renpy.pause(hard=True)

#label standLeft
#    $ standWalk=0

#show semi stand:
#    xpos sX
#    ypos sY
#    xzoom -1.0
    
#    $ renpy.pause(hard=True)

#label walkRight
#    $standWalk=1
#    scene bg room:
#        xpos rX
#        linear dist/100.0 xpos rx-dist

#    show semi walk:
#    xpos sX
#    ypos sY
#    xzoom 1.0

#    $ renpy.pause(delay=dist/100.0, hard=True)
#    $rX -=dist
#    jump standRight

 #   label walkLeft
 #       $standWalk=1
 #       scene bg room:
 #           xpos rX
 #           linear dist/100.0 xpos rx+dist
    
 #       show semi walk:
 #       xpos sX
 #       ypos sY
 #       xzoom -1.0
    
 #       $ renpy.pause(delay=dist/-100.0, hard=True)
 #       $rX +=dist
 #       jump standLeft

#label checkDist:
#    $ mX=renpy.get_mouse_pos()[0]

#    if mX>320:
        #prevents character from walking outside area
#        $ dist = mX-320
#        if Rx-dist<-4067:
#            $dist= 4067 + rX
#        jump walkRight

 #   else:
        #prevents character from walking outside area
 #       $dist = 320-mX
 #       if rX+dist>-351:
 #           $ dist= -(351 + rX)
 #       jump walkLeft
        

    #First level. Player starts next to future exit but can't leave until after defeating the opponent at event a
    stage1 = [
    "1111111111",
    "11110111a1",   #First keycard battle (scientist)
    "1100000001",
    "1111111101",
    "1111111101",
    "1230000001",
    "1111111111",
    [Enemy1]
    ]
    stage1_1 = [
    "1111111111",
    "1111011101",
    "1100000001",
    "1111111101",
    "1111111101",
    "1230000001",
    "1111111111",
    [Enemy1]
    ]

    #Second level.
    stage2 = [
    "1111111111",
    "1211000b11",   #Second keycard battle (soldier)
    "1011011111",
    "1000000011",
    "1110000011",
    "1110000031",
    "1111111111",
    [Enemy1, Enemy2]
    ]
    stage2_1 = [
    "1111111111",
    "1211000011",
    "1011011111",
    "1000000011",
    "1110000011",
    "1110000031",
    "1111111111",
    [Enemy1, Enemy2]
    ]

    #Third level
    stage3 = [
    "111111111",
    "111121111",
    "111101111",
    "100000001",
    "111101111",
    "1e0000001",    #Sex bot easter egg
    "111101111",
    "111131111",
    "111111111",
    [Enemy1, Enemy2, Enemy3]
    ]
    stage3_1 = [
    "111111111",
    "111121111",
    "111101111",
    "100000001",
    "111101111",
    "100000001",
    "111101111",
    "111131111",
    "111111111",
    [Enemy1, Enemy2, Enemy3]
    ]

    #Final lab level
    stage4 = [
    "111111111",
    "101010001",
    "101010001",
    "101010111",
    "100000021",
    "131010111",
    "111111111",
    [Enemy1, Enemy2, Enemy3, Enemy4]
    ]

    #Boiler room
    stage5 = [
    "111111111",
    "100001111",
    "110101f01",    #Final battle
    "120101101",
    "110000101",
    "110110001",
    "111111111",
    []
    ]

    #Sewer system
    stage6 = [
    "11111111111111111111",
    "11111011110110001111",
    "11011011110110001101",
    "11011011110111101101",
    "11011011110111101101",
    "13000000000000000001",
    "11011011011011011011",
    "11011011011011011011",
    "11011011011011211011",
    "11111001111011111011",
    "11111001111011111011",
    "11111111111111111111",
    []
    ]

label dungeon:
    $ event_check=False
    $ config.rollback_enabled=False
    python:
        # Try-except clauses are used to prevent the List Out of Index Error
        def showWall(where, val, what):
            try:
                if where.map[where.y][where.x] == val:
                    renpy.show(img_pref + what)
            except:
                pass
        while 1:
            # Calculate relative coordinates
            # Here is a visualised relative coordinate in this code. Image here=player and facing top.
            # left3, front2, right3
            # left2, front1, right2
            # left1,  here , right1
            turnback    = Position(here.map,   here.y,               here.x,               -here.dy,  -here.dx,  here.num)
            turnright   = Position(here.map,   here.y,               here.x,               here.dx,   -here.dy,  here.num)
            turnleft    = Position(here.map,   here.y,               here.x,               -here.dx,  here.dy,   here.num)
            right1      = Position(here.map,   here.y + here.dx,     here.x - here.dy,     here.dy,   here.dx,   here.num)
            left1       = Position(here.map,   here.y - here.dx,     here.x + here.dy,     here.dy,   here.dx,   here.num)
            front1      = Position(here.map,   here.y + here.dy,     here.x + here.dx,     here.dy,   here.dx,   here.num)
            right2      = Position(front1.map, front1.y + front1.dx, front1.x - front1.dy, front1.dy, front1.dx, here.num)
            left2       = Position(front1.map, front1.y - front1.dx, front1.x + front1.dy, front1.dy, front1.dx, here.num)
            front2      = Position(front1.map, front1.y + front1.dy, front1.x + front1.dx, front1.dy, front1.dx, here.num)
            right3      = Position(front2.map, front2.y + front2.dx, front2.x - front2.dy, front2.dy, front2.dx, here.num)
            left3       = Position(front2.map, front2.y - front2.dx, front2.x + front2.dy, front2.dy, front2.dx, here.num)

            # Composite background images.
            renpy.scene()
            renpy.show(img_pref + "base")
            showWall(left3, "1", "left3")
            showWall(right3, "1", "right3")
            showWall(front2, "1", "front2")
            showWall(left2, "1", "left2")
            showWall(right2, "1", "right2")
            showWall(front1, "1", "front1")
            showWall(left1, "1", "left1")
            showWall(right1, "1", "right1")
            showWall(front2, "2", "exit2")
            showWall(front1, "2", "exit1")
            buffer = img_pref
            img_pref = ""
            showWall(front1, "e", "closet")
            img_pref = buffer

            #exit maze events:
            if here.map[here.y][here.x]=="2":
                if here.num > 2:
                    renpy.jump("exit_dungeon_" + str(here.num))
                elif here.map[1][8] != "a" and here.map[1][7] != "b":
                    renpy.jump("exit_dungeon_" + str(here.num))
                else:
                    if here.num == 1:
                        here = Position(stage1, 5, 3, 0, -1, 1)
                        narrator("That door is locked.")
                    else:
                        here = Position(stage2, 2, 1, 1, 0, 2)
                        narrator("That scientist's card isn't working for this door.")

            #other events:
            if here.map[here.y][here.x] == "a":
                renpy.jump("event_a")
            elif here.map[here.y][here.x] == "b":
                renpy.jump("event_b")
            elif here.map[here.y][here.x] == "e":
                renpy.jump("event_e")
            elif here.map[here.y][here.x] == "f":
                renpy.jump("event_f")

            if here.num > 5:   #Sewer Poison
                girl.hp -= 1
                if girl.hp <= 0:
                    # renpy.music.play(DEFEAT, "sound")
                    narrator ("Your consciousness is fading...")
                    #reset the stuff for the next gameplay:
                    # girl.hp=girl.max_hp
                    # girl.mp=girl.max_mp
                    renpy.full_restart()

            # loot events:
            if event_check and renpy.random.random()<0.06: #and here.num>1:
                loot_items = ["R", "P", "C", "W"]#, "B", "X"]
                random.shuffle(loot_items)
                for item in loot_items:
                    renpy.jump("loot_"+item)

            # Check events and jump if happens
            if event_check and not here.map[-1] == [] and renpy.random.random() < encounter_chance:
                renpy.jump("battle")

            # Else, call the move screen
            event_check = True

            try:
                res = renpy.call_screen("move") #Updates based on player movement. Uses inventory items and updates "here" values.
            except:
                res = here
            if isinstance(res, Item):
                item = res
                if item.hp > 0:
                    item.player.hp += item.hp
                    if item.player.hp > item.player.max_hp:
                        item.player.hp = item.player.max_hp
                    inventory.drop(res)
                elif item.mp > 0:
                    item.player.mp += item.mp
                    if item.player.mp > item.player.max_mp:
                        item.player.mp = item.player.max_mp
                    hers.upgrade()
                    inventory.drop(res)
                elif item.ammo > 0:
                    item.player.ammo += item.ammo
                    inventory.drop(res)
                else:
                    Shoot.element = item.element
                renpy.hide_screen("inventory_screen")
                renpy.hide_screen("gui_tooltip")
                renpy.show_screen("move")
            else:
                here = res

label battle:
    $ escape = False
    $ config.rollback_enabled = False
    # $ renpy.music.set_volume(0.75, 2.5, channel="combat")
    $ enemy=copy(renpy.random.choice(here.map[-1])) # Copy monster instances not to modify the originals
    show screen battle_ui
    $ renpy.show(enemy.image)
label no_escape:
    python:
        while enemy.hp>0:
            girl.command(girl, enemy)
            if enemy.hp<=0:
                break

            if girl.hp <1:
                if special_battle and here.num == 4:
                    renpy.jump("escaped")
                # renpy.music.play(DEFEAT, "sound")
                narrator ("Your consciousness is fading...")
                #reset the stuff for the next gameplay:
                # girl.hp=girl.max_hp
                # girl.mp=girl.max_mp
                renpy.full_restart()

    "You won!"
    # $ renpy.music.set_volume(0.0, 2.5, channel="combat")
    # play sound VICTORY
    python:
        if event_check and renpy.random.random()<0.5:
            loot_items = ["R", "P", "C", "W"]#, "B", "X"]
            random.shuffle(loot_items)
            for item in loot_items:
                renpy.jump("loot_"+item)
    pass
label escaped:
    if escape:
        if special_battle and not here.num == 4:
            "There's no turning back. You have to defeat this opponent."
            $ escape = False
            jump no_escape
        $ encounter_chance *= 1.1
        if encounter_chance > 0.9:
            $ encounter_chance = 0.9
    $ renpy.hide(enemy.image)
    hide screen battle_ui

    if special_battle:
        $ special_battle = False
        return
    jump dungeon

init -3 python:
    # Import the copy module for copying instances.
    from copy import copy

    # Class used for relative coodinate
    class Position():
        def __init__(self,map,y,x,dy,dx,num=0):
            self.map=map
            self.y=y
            self.x=x
            self.dy=dy
            self.dx=dx
            self.num=num

    # Class used for battle skills
    class Skill():
        def __init__(self, name, hit, power, type="attack", element="", mp=0, ammo=0):
            self.name = name
            self.mp = mp
            self.hit = hit
            self.power = power
            self.type = type
            self.element = element
            self.ammo = ammo

    # Class used for battle characters. Inherit renpy.store.object for the rollback function.
    class Actor(renpy.store.object):
        def __init__(self, name, max_hp=0, skills=[], image="", weak="", max_mp=0, ammo=0):
            self.name = name
            self.max_hp = max_hp
            self.hp = max_hp
            self.skills = skills
            self.image = image
            self.weak = weak
            self.defending = False
            self.dead = False
            self.max_mp = max_mp
            self.mp = max_mp
            self.ammo = ammo

        def command(self, who, target):
            who.defending = False
            self.skill = renpy.call_screen("command", char=who)
            target.skill = renpy.random.choice(target.skills)
            if self.skill.type == "attack":
                self.attack(self.skill, target)
            # elif self.skill.type=="heal":
                # self.heal(self.skill)
            elif self.skill.type == "inventory":
                self.inventory_skill()
            elif self.skill.type == "defend":
                self.defend()
            elif self.skill.type == "flee":
                escape = True
                renpy.jump("escaped")
            if target.hp < 1:
                return
            target.attack(target.skill, self)

        def attack(self,skill, target):
            if self.name == girl.name:
                if int(self.skill.hit * (1 - (hers.luck * 0.1))) < renpy.random.randint(0,100):
                    narrator("{} dodged {}'s attack!".format(target.name, self.name))
                else:
                    damage = self.skill.power
                    if self.skill.mp > 0:
                        self.mp -= self.skill.mp
                    elif skill.name == "Shoot":
                        self.ammo -= 1
                        if Shoot.element != target.weak:
                            damage = int(damage * 0.5)
                    else:
                        damage = int(damage * (100 + hers.strength) / 100)

                    if target.defending:
                        damage = int(damage / 2)
                    target.hp -= damage
                    narrator ("{} took {} damage.".format(target.name, damage))
                    if target.hp < 1:
                        pass
            else:
                if self.skill.hit < renpy.random.randint (0,100):
                    narrator ("{} dodged {}'s attack!".format(target.name, self.name))
                else:
                    if self.skill.mp > 0:
                        self.mp -= self.skill.mp
                    damage = self.skill.power

                    if skill.name=="Shoot":
                        self.ammo -= 1
                        if Shoot.element != target.weak:
                            damage = int(damage * 0.5)

                    if target.defending:
                        damage = int(damage / 2)
                    target.hp -= damage
                    narrator ("{} took {} damage.".format(target.name, damage))
                    if target.hp < 1:
                        pass

        # def heal(self, skill):
            # self.hp += self.skill.power

        def inventory_skill(self):
            item = renpy.call_screen("inventory_screen")
            if isinstance(item, Item):
                if item.hp > 0:
                    item.player.hp += item.hp
                    if item.player.hp > item.player.max_hp:
                        item.player.hp = item.player.max_hp
                    inventory.drop(item)
                elif item.mp > 0:
                    item.player.mp += item.mp
                    if item.player.mp > item.player.max_mp:
                        item.player.mp = item.player.max_mp
                    hers.upgrade()
                    inventory.drop(item)
                elif item.ammo > 0:
                    item.player.ammo += item.ammo
                    inventory.drop(item)
                else:
                    Shoot.element=item.element
                    # item.girl.skills.remove(Shoot)
                    # item.girl.skills.append(Shoot)

                renpy.hide_screen("inventory_screen")
                renpy.hide_screen("gui_tooltip")

            #renpy.show_screen("inventory_screen")
            #renpy.show_menu("inventory_screen")

        def defend(self):
            narrator ("{} defends.".format(self.name))
            self.defending = True

init:
    # Screen used for moving
    screen move:
        fixed:
            if move_keys_visible:
                if front1.map[front1.y][front1.x] != "1":
                    imagebutton auto up_button xpos .5 ypos .34 action Return(value=front1)
                    # textbutton "^" action Return(value=front1)  xcenter .5 ycenter .34 # background Frame("gui/frame.png",24,24) ypadding 10 xpadding 20 text_color "#000" # hover_text_color "#FFF"
                imagebutton auto right_button xpos .57 ypos .47 action Return(value=turnright)
                # textbutton ">" action Return(value=turnright) xcenter .57 ycenter .47 #background Frame("gui/frame.png",24,24) ypadding 10 xpadding 20
                imagebutton auto down_button xpos .5 ypos .6 action Return(value=turnback)
                # textbutton "v" action Return(value=turnback) xcenter .5 ycenter .6 #background Frame("gui/frame.png",24,24) ypadding 10 xpadding 20
                imagebutton auto left_button xpos .43 ypos .47 action Return(value=turnleft)
                # textbutton "<" action Return(value=turnleft) xcenter .43 ycenter .47 #background Frame("gui/frame.png",24,24) ypadding 10 xpadding 20
                $ move_keys_visible_text = "Hide controls"
            else:
                $ move_keys_visible_text = "Show controls"

            if front1.map[front1.y][front1.x] != "1":
                key "K_UP" action Return(value=front1)
                key "w" action Return(value=front1)
            key "K_LEFT" action Return(value=turnleft)
            key "a" action Return(value=turnleft)
            key "K_DOWN" action Return(value=turnback)
            key "s" action Return(value=turnback)
            key "K_RIGHT" action Return(value=turnright)
            key "d" action Return(value=turnright)

            hbox align (.95,.04) spacing 20:
                if not renpy.variant("touch"):
                    textbutton move_keys_visible_text action ToggleVariable("move_keys_visible", true_value=True, false_value=False)
                textbutton "Show Inventory" action [ Hide("move"), Show("inventory_screen")]
                textbutton "Show Stats" action [Hide("move"), Show("stats_screen")]

    # Screen used for selecting skills
    screen command:
        vbox align (.75,.5):
            text "[char.name]" size 45
            for i in char.skills:
                if char.mp >= i.mp and char.ammo >= i.ammo:
                    textbutton "[i.name]" size_group "commands" action Return (value=i)

    # Screen which shows battle status
    screen battle_ui:
#        use battle_frame(char=girl, position=(.95,.05))
        # use battle_frame(char=girl, position=(0.97, 0.20))
        # use battle_frame(char=enemy, position=(0.05, 0.20))
        frame area (0, 0, 270, 160) align (0.97, 0.20) background Frame("gui/frame.png", 22, 22) left_padding 20 right_padding 20:
            vbox yfill True:
                text "[girl.name]" outlines [(1, "00000020", 0, 0)] color "#000"
                hbox xfill True:
                    text "HP " outlines [(1, "00000020", 0, 0)] color "#000"
                    text "[girl.hp]/[girl.max_hp]" xalign 1.0 outlines [(1, "00000020", 0, 0)] color "#000"
            if girl.ammo > 0:
                vbox yfill True ypos 110:
                    hbox xfill True:
                        text "Ammo " outlines [(1, "00000020", 0, 0)] color "#000"
                        text "[girl.ammo]" xalign 1.0 outlines [(1, "00000020", 0,0)] color "#000"
        frame area (1010, 0, 1280, 160) align (0.95, 0.20) background Frame("gui/frame.png", 22, 22) left_padding 20 right_padding 20:
            vbox yfill True:
                text "[enemy.name]" outlines [(1, "00000020", 0, 0)] color "#000"
                hbox xfill True:
                    text "HP [enemy.hp]/[enemy.max_hp]" outlines [(1, "00000020", 0, 0)] color "#000"

    screen battle_frame:
        #Needs fixing to separate enemy hp from player hp
        frame area (0, 0, 270, 160) align position background Frame("gui/frame.png", 22, 22) left_padding 20 right_padding 20:

            vbox yfill True:
                text "[char.name]" outlines  [(1, "00000020", 0, 0)] color "#000"
                hbox xfill True:
                    text "HP " outlines  [(1, "00000020", 0, 0)] color "#000"
                    text "[char.hp]/[char.max_hp]" xalign 1.0 outlines  [(1, "00000020", 0, 0)] color "#000"
            if char.ammo > 0:
                vbox yfill True  ypos 110:
                    hbox xfill True:
                        text "Ammo " outlines  [(1, "00000020", 0, 0)] color "#000"
                        text "[char.ammo]" xalign 1.0 outlines  [(1, "00000020", 0, 0)] color "#000"

init:
    transform fly:
        parallel:
            anchor(0.0,0.0)
            xpos 0.05
        parallel:
            ypos -0.01
            ease 2.0 ypos 0.01
            ease 2.0 ypos -0.01
            repeat

init:
    transform exit_hover:
        alpha 0.5
        parallel:
            anchor(0.5,0.5)
            ypos 0.5
            easeout 3.0 alpha 0.3
            easeout 3.0 alpha 0.5
            repeat
        parallel:
            ease 2.0 ypos 0.53
            ease 2.0 ypos 0.47
            repeat

init -2 python:
    class Item(store.object):
        def __init__(self, name, space=0, player=None, cost=0, hp=0, mp=0, ammo=0, element="", image=""):
            self.name = name
            self.space=space
            self.player = player
            self.cost=cost
            self.hp = hp
            self.mp = mp
            self.ammo = ammo
            self.element = element
            self.image = image

    class Inventory(store.object):
        def __init__(self, money=0):
            self.money = money
            self.items = []

        def add(self, item):
            # if len(self.items)>8:
                # narrator ("Your inventory is full!")
            # else:
            self.items.append(item)

        def drop(self, item):
            self.items.remove(item)

screen inventory_screen:
    add "gui/inventory.png"
    modal True
    use battle_frame(char=girl, position=(.97,.20))
    hbox align (.95,.04) spacing 20:
        textbutton "Close Inventory" action [ Hide("inventory_screen"), Return(here)]

    $ x = 0.375
    $ y = 15
    $ i = 0
    $ sorted_items = sorted(inventory.items, key=attrgetter('element'), reverse=True) #guns first

    $ next_inv_page = inv_page + 1
    if next_inv_page > int(len(inventory.items) / 9):
        $ next_inv_page = 0

    for item in sorted_items: #inventory.items:
        if i+1 <= (inv_page + 1)*9 and i+1 > inv_page*9:
            $ x += 0.14
            if i%3 == 0:
                $ y += 160
                $ x = 0.375
            $ pic = item.image
            $ my_tooltip = "tooltip_inventory_" + pic.replace("gui/inv_", "").replace(".png", "")
            imagebutton idle pic hover pic xpos x ypos y action [Hide("gui_tooltip"), Return(item)] hovered [ Play ("sound", "sfx/click.wav"), Show("gui_tooltip", my_picture=my_tooltip, my_tt_ypos=693) ] unhovered [Hide("gui_tooltip")] at inv_eff
            if Shoot.element and (Shoot.element == item.element): #indicate the selected gun
                add "gui/selected.png" xpos x ypos y anchor(.5,.5)
        $ i += 1
        if len(inventory.items)>9:
            textbutton _("Next Page") action [SetVariable('inv_page', next_inv_page), Show("inventory_screen")] xpos .475 ypos .83

init -2:
    transform inv_eff:
        zoom 0.5 xanchor 0.5 yanchor 0.5
        on idle:
            #easein 0.5 zoom 0.5
            linear 0.2 alpha 1.0
        # on selected_idle:
            # easein 0.5 zoom 0.5
        on hover:
            #easein 0.5 zoom 0.65
            linear 0.2 alpha 2.5
        # on selected_hover:
            # easein 0.5 zoom 0.65

    transform boss_kill:
        parallel:
            linear 0.1 xalign 0.54
            linear 0.1 xalign 0.43
            linear 0.05 xalign 0.45
            linear 0.05 xalign 0.55
            linear 0.1 xalign 0.59
            linear 0.1 xalign 0.44
            repeat
        parallel:
            linear 1.0 alpha 5.0
            linear 1.0 alpha 0.0

init python:
    showitems = False #turn True to debug the inventory
    def display_items_overlay():
        if showitems:
            inventory_show = "Inventory: "
            for i in range(0, len(inventory.items)):
                item_name = inventory.items[i].name
                if i > 0:
                    inventory_show += ", "
                inventory_show += item_name
            ui.frame()
            ui.text(inventory_show, color="#000")
    config.overlay_functions.append(display_items_overlay)

label loot_R:
    $ inventory.add(ramen)
    "You found some [ramen.name]."
    if special_battle:
        $ special_battle = False
        return
    jump dungeon
label loot_P:
    $ inventory.add(red_pill)
    "You found a [red_pill.name]."
    if special_battle:
        $ special_battle = False
        return
    jump dungeon
label loot_C:
    $ inventory.add(cola)
    "You found a [cola.name]."
    if special_battle:
        $ special_battle = False
        return
    jump dungeon
label loot_W:
    $ inventory.add(black_pill)
    "You found a [black_pill.name]."
    if special_battle:
        $ special_battle = False
        return
    jump dungeon
# label loot_B:
#     "You found a [bullet.name]."
#     $ girl.ammo += bullet.ammo
#     if special_battle:
#         $ special_battle = False
#         return
#     jump dungeon
# label loot_X:
#     "You found a [box.name]."
#     $ girl.ammo += box.ammo
#     if special_battle:
#         $ special_battle = False
#         return
#     jump dungeon
