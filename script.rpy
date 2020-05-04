#Update is Coming at 2 pm!!!

init -2:
    image bg park = "bg/ParkDuckless.jpg"

    # Declare characters used by this game. The color argument colorizes the
    # name of the character.

    # Main female character. Brass/copper skin. Black hair.
    define g = Character("The Girl", who_color="#fc4a1e")
    define mc = Character("You", who_color="#2370ff")
    define pa = Character(_("P. A."), who_color="#e8ef26")
    define n = Character(None, kind=nvl, say_thought_color = "#FFF")
    
init python:
     config.gestures = { "n_s" : "hide_windows", "e" : "toggle_skip", "w_e" : "game_menu", "w" : "rollback" }

    python:
        def rename(character, actor=None):
            replace = renpy.input("What is their name?", default=character.name, length=25)
            replace = replace.strip()
            if not replace:
                pass
            else:
                character.name = replace
                if actor:
                    actor.name = replace

label language_chooser:
    scene black

    menu:
        "*Will restart the game, so make sure to save.*"
        "English":
            $ renpy.change_language(None)
            stop ambient
            stop music
            stop sound
        # "German":
        #     $ renpy.change_language("german")
        #     stop ambient
        #     stop music
        #     stop sound
        "French":
            $ renpy.change_language("french")
            stop ambient
            stop music
            stop sound
        # "Italian":
        #      $ renpy.change_language("italian")
        #      stop ambient
        #      stop music
        #      stop sound
        # "Spanish":
        #      $ renpy.change_language("spanish")
        #      stop ambient
        #      stop music
        #      stop sound
        # "Arabic":
        #      $ renpy.change_language("arabic")
        #      stop ambient
        #      stop music
        #      stop sound
        "{b}Return{/b}":
            return

    $ renpy.utter_restart()
label splashscreen:

    if not persistent.chose_lang:
        $ persistent.chose_lang = True
        jump language_chooser

    return

label start:
    python:
        girl = Actor("The Girl", 100, [Punch, Kick, Magic, Defend, Inventory_sk, Flee], max_mp=50)
        hers = CharStats(strength=40)
        boy = CharStats(intelligence=40) #For later use

        ramen = Item("Ramen", hp=50, player=girl, image="gui/inv_chocolate.png")
        red_pill = Item("Red Pill", hp=100, player=girl, image="gui/inv_chips.png")
        cola = Item("Cola", mp=25, player=girl, image="gui/inv_cola.png")
        white_pill = Item("White Pill", mp=50, player=girl, image="gui/inv_banana.png")
        bullet = Item("Bullet", ammo=1, player=girl, image="gui/inv_musket.png")
        box = Item("Box of Bullets", ammo=5, player=girl, image="gui/inv_laser.png")
        # gun = Item("Gun", player=girl, element="bullets", image="gui/inv_gun.png")

        #reset hp on game start
        # girl.hp=girl.max_hp
        # girl.mp=girl.max_mp

        inventory = Inventory()
        #initial inventory
        # inventory.add(gun)
        inventory.add(ramen)

#################
label story:
    scene bg park
    $ rename(g, girl)
    n "Start story"

    # "bg lab.png" not yet created. Description follows:
    # Sterile gray room lined with infrared cameras. On wall is a large 2-way mirror
    # parallel to stainless steel chair.
    scene bg lab

    # "tubes empty.png" not yet created. Description follows:
    # Clear tubes lying on the lab floor and up the chair back.
    show tubes empty
    # "girl bolted eyes shut.png" not yet created. Description follows:
    # Young woman ~19 years old bolted to stainless steel chair. She looks dead,
    # her brass skin an eroded copper, her eyes shut
    show girl bolted eyes shut
    # "tubehat empty.png" not yet created. Description follows:
    # Ends of multiple tubes stuck on head of the girl in this scene. Currently clear and empty.
    show tubehat empty

    pa "{i}krrrch{w=1}
        \n{cps=50}Commencing test 439{/cps}{w=1}
        \nkrrzch{/i}"

    # "fan_whirr.ogg" not implemented. Sounds like industrial fan spinning.
#    play music "fan_whirr.ogg" fadeout 1.6

    # "tubes filling.png" not yet created. Description follows:
    # A thick black chrome liquid starts to flow through the tubes, looking as
    # if snakes had begun to crawl up the back of the steel chair
    show tubes filling behind girl
    "{w=1.5}"
    # "tubes full.png" not yet created. Description follows:
    # A thick black chrome liquid fills the tubes completely.
    show tubes full behind girl
    # "tubehat full.png" not yet created. Description follows:
    # A thick black chrome liquid fills the tube entering the head of the girl.
    show tubehat full

    "An hour passes."
    # "girl bolted twitch.png" not yet created. Description follows:
    # Identical to "girl bolted eyes shut.png" but with right index finger raised.
    show girl bolted twitch behind tubehat
    "{w=.5}"
    # "girl shoulder twitch.png" not yet created. Description follows:
    # Girl bolted in chair with raised shoulder tugging at restraints
    show girl shoulder twitch behind tubehat
    "{w=.5}"
    # "girl_thrashing.webm" shows the main female character thrashing more and more
    # violently.
#    $ renpy.movie_cutscene("girl_thrashing.webm")
    show tubes full
    # "girl bolted turned.png" not yet created. Description follows:
    # Girl bolted in chair turned to face the 2-way mirror. Eyes dead.
    show girl bolted turned
    show tubehat full
    "{w=.5}"
    # "girl black tears.png" not yet created. Description follows:
    # Girl bolted in chair, turned to face mirror. Eyes dead with black chrome
    # liquid pouring from her eyes and nose.
    show girl black tears behind tubehat
    "A minute passes."
    pa "{i}krrrch{w=.5}
        \nAhem--{/i}"
    # "girl tensing.png" not yet created. Description follows:
    # Girl bolted in chair with head upturned and feet curled under chair
    show girl tensing behind tubehat
    # Need to rotate tubehat to stay on her head
    "{w=.25}"

    # "girl lifted torso.png" not yet created. Description follows:
    # Girl has her waist and chest lifted out of the chair she is bound to.
    show girl lifted torso behind tubehat
    "{w=.25}"
    # "girl tethered levitating.png" not yet created. Description follows:
    # Girl completely lifted from chair, held down only by hands and ankles
    show girl tethered levitating


    ###############
    #Play escape movie here
    jump dungeon1

    #Maze Events
label event_a:
    $ config.rollback_enabled = True
    "This scientist had a keycard on the furniture behind him. As [girl.name] crept up to grab it, he turned and began to attack."
    $ battle1 = ["", [Enemy2]]
    $ here = Position(battle1, 1, 8, 1, 0, 1)
    $ config.rollback_enabled=False
    $ special_battle = True
    call battle
    $ config.rollback_enabled = True
    "Collapsing to the floor, the scientist no longer posed any threat. [girl.name] took the badge and went on her way."
    jump dungeon1_1

label event_b:
    $ config.rollback_enabled = True
    "[girl.name] discovered a soldier hunkering down in this room."
    "Seeing his higher rank badge, she knew what she needed to do."
    $ battle2 = ["", [Enemy4]]
    $ here = Position(battle2, 1, 7, 0, 1, 2)
    $ config.rollback_enabled = False
    $ special_battle = True
    call battle
    $ config.rollback_enabled = True
    "The soldier was more of a challenge than the scientist had been, but ultimately [girl.name] was able to overpower them."
    "Grabbing the keycard from her fallen enemy, she set off on her escape."
    jump dungeon2_1

label event_e:
    $ config.rollback_enabled = True
    "[girl.name] tensed as she opened the closet, prepared to fight anything that came out."
    "To her surprise, she found nothing that was prepared to harm her."
    "Tied up in the closet..."
    "Was an abandoned sex robot. It turned to look at her with an expression that almost was begging."
    "This robot almost seemed like a kindred spirit in the flickering light of this hallway."
    "[girl.name] felt she had a choice to make."
    menu:
        "Untie the robot":
            jump free_bot
        "Leave the robot":
            "While the robot was not necessarily harmful, [girl.name] had no reason to expect the robot to be helpful either."
            "[girl.name] closed the door to the closet and left the odd robot where she found it. Better safe than sorry."
            jump bot_end
label free_bot:
    "[girl.name] simply couldn't bear to see another victim of this facility left helpless.
    \nShe grabbed the ropes binding the robot and began to pull on the knots holding her new friend captive."
    "After struggling for a good while, she was finally successful. The sex robot looked at her with what could only be described as awe
    \nand gratitude."
    "In a few seconds, the robot picked itself up and gave [girl.name] a nod of approval."
    "And just as quickly, the robot ran off."
    "Though she had failed to gain an ally, [girl.name] felt she had at least allowed another the same chance for freedom now before her."
label bot_end:
    "[girl.name] turned back to the task at hand: Escaping this lab."
    jump dungeon3_1

label event_f:
    $ config.rollback_enabled = True
    "After all this time fighting, the sight of another test subject made [girl.name] hopeful. Seeing the grate the other subject stood on gave her more hope that escape was possible."
    g "Pst! Hey! Let me help you pull that grate off. Then we can both get out of here!"
    "The other subject turned. She seemed very lifeless and cold, just as [girl.name] had felt during the experiments."
    "[girl.name] had never met this girl before, but was certain that she would be an ally."
    "Suddenly, she noticed a glimmer in the other girl's hand. A scalpel that she wasn't sure had been there before.
    \nNext thing she knew, the other girl vanished completely."
    "Within seconds, a younger girl armed with a large kitchen knife stood in her place."
    "Though this girl was younger and looked healthy, she had the same cold, dead expression her older counterpart carried."
    "With a screech, she lunged at [girl.name] swinging the knife wildly before vanishing once again."
    "This time when she reappeared, it was as an older woman. In her hands was a glowing tool clearly designed for cutting.
    \n[girl.name] could feel the heat coming from the tool even this far away."
    g "I really didn't want to fight you, but I guess you leave me no choice."
    "For the first time, the other's facial expression changed, twisting into a cruel smile."
    jump exit_dungeon_4

    #Between level events
label exit_dungeon_1:
    jump dungeon2
label exit_dungeon_2:
    jump dungeon3
label exit_dungeon_3:
    jump dungeon4
label exit_dungeon_4:
    jump dungeon5
label exit_dungeon_5:
    $ battle3 = ["", [Enemy5]]
    $ here = Position(battle3, 1, 6, here.dy, here.dx, 4)
    $ config.rollback_enabled = False
    $ special_battle = True
    call battle
    $ config.rollback_enabled = True
    "Staggering back, [girl.name] felt as though she was on her last legs. Clearly this other test subject was about to overpower her."
    "The fight drawing closer to its end seemed to accelerate the transformations this girl underwent. She kept vanishing faster and faster."
    "The deadly test subject charged for one final attack, when suddenly..."
    "She vanished completely."
    "[girl.name] looked around for her opponent. Throughout their fight, no disappearance had lasted this long. Had she been spared?"
    "After getting her breath back, [girl.name] grabbed the grate and tugged until it was removed."
    "Sure enough, the foul smell of a sewer greeted her. Steeling herself, she climbed down into the sewer to make her final break for it."
    jump dungeon6
label exit_dungeon_6:
    "Having escaped the sewers, [girl.name] ran off into the night."

# label credits:
#     $ credits_speed = 25 #scrolling speed in seconds
#     scene black #replace this with a fancy background
#     with dissolve
#     show cred at Move((0.5, 3.0), (0.5, 0.0), credits_speed, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
#     with Pause(credits_speed)
#     show thanks:
#         yanchor 0.5 ypos 0.5
#         xanchor 0.5 xpos 0.5
#     with dissolve
#     with Pause(3)
#     hide thanks
#     return
#
# label the_end:
#     call credits
#     return
#
# init python:
#     credits = ('Writing', 'Maelstrom-Fenrir'), ('Art', 'Chocojax'), ('Art', 'Tag-'), ('Art', 'AzureXtwighlight'), ('Art', 'Leon Zavšek'), ('Programming', 'Leon Zavšek'), ('Music', 'Ziassan'), ('Additional Help', 'CheeryMoya'), ('Special Thanks', 'nyaatrap'), ('Special Thanks', 'Uncle Mugen')
#     credits_s = "{size=80}Credits\n\n"
#     c1 = ''
#     for c in credits:
#         if not c1==c[0]:
#             credits_s += "\n{size=40}" + c[0] + "\n"
#         credits_s += "{size=60}" + c[1] + "\n"
#         c1=c[0]
#     credits_s += "\n{size=40}Engine\n{size=60}" + renpy.version()
#
# init:
# #    image cred = Text(credits_s, text_align=0.5, font="GUI/Chivo.ttf")
#     image cred = Text(credits_s, text_align=0.5 )
#     image theend = Text("{size=80}The end", text_align=0.5)
#     image thanks = Text("{size=80}Thanks for Playing!", text_align=0.5)


label reset_stats:
    python:
        pass
        girl.hp=girl.max_hp
        girl.mp=girl.max_mp
        # if not isinstance(inventory.items, Item):
            # pass
        # else:
            # if here.num==3 and len(inventory.items<8):
                # inventory.add(ramen)
            # if here.num==4 and len(inventory.items<7):
                # inventory.add(ramen)
                # inventory.add(cola)
            # if here.num==5 and len(inventory.items<7):
                # inventory.add(red_pill)
                # inventory.add(cola)
            # if here.num>5 and len(inventory.items<7):
                # inventory.add(red_pill)
                # inventory.add(white_pill)
    return

label pre_dungeon:
    call reset_stats
    return

label dungeon1:
    $ img_pref = "p_"
    $ encounter_chance = 0.1
    $ here=Position(stage1, 5, 2, 0, 1, 1)
    call pre_dungeon
    jump dungeon

label dungeon1_1:
    $ img_pref = "p_"
    $ encounter_chance = 0.1
    $ here=Position(stage1_1, 1, 8, -1, 0, 1)
    call pre_dungeon
    jump dungeon

label dungeon2:
    $ img_pref = "p_"
    $ encounter_chance = 0.2
    $ here=Position(stage2, 5, 8, 0, -1, 2)
    call pre_dungeon
    jump dungeon

label dungeon2_1:
    $ img_pref = "p_"
    $ encounter_chance = 0.2
    $ here = Position(stage2_1, 1, 7, 0, 1, 2)
    call pre_dungeon
    jump dungeon

label dungeon3:
    $ img_pref = "p_"
    $ encounter_chance = 0.2
    $ here=Position(stage3, 7, 4, -1, 0, 3)
    call pre_dungeon
    jump dungeon
label dungeon3_1:
    $ img_pref = "p_"
    $ encounter_chance = 0.2
    $ here = Position(stage3_1, 5, 1, 0, -1, 3)
    call pre_dungeon
    jump dungeon

label dungeon4:
    $ img_pref = "p_"
    $ encounter_chance = 0.4
    $ here=Position(stage4, 5, 1, -1, 0, 4)
    call pre_dungeon
    jump dungeon

label dungeon5:
    $ img_pref = "p_"
    $ encounter_chance = 0
    $ here=Position(stage5, 3, 1, 0, 1, 5)
    call pre_dungeon
    jump dungeon

label dungeon6:
    $ img_pref = "p_"
    $ encounter_chance = 0
    $ here = Position(stage6, 5, 1, 0, 1, 6)
    call pre_dungeon
    jump dungeon
