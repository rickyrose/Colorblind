init -2:
    # Declare characters used by this game. The color argument colorizes the
    # name of the character.

    # Main female character. Brass/copper skin. Black hair.
    define g = Character("Aura", who_color="#fc4a1e")
    # Main male character
    define mc = Character("Kaleb", who_color="#2370ff")
    define narrator = Character(None,  ctc_position="fixed")

    #Prologue characters
    define pa = Character(_("P. A."), who_color="#e8efE6")

    #Chapter 1 characters
    define mk = Character("Mr. Kirk", who_color="#46105E", xalign=0.5, yalign=0.5)
    define jsn = Character("Jason", who_color="#ffE023")
    define sne = Character("Syd & Ellie", who_color="#44CCCC")
    define an = Character("???", who_color="#969696")
    define dude = Character("Some Dude", who_color="#2222ff")

    define dc = Character("Doctors", who_color="#91c2ff")
    define gd =  Character("Guards", who_color="#F5F5DC")
    define mr =  Character("Test Subject 42", who_color="#9bc6c0")
    define tri = Character("Elite Soldiers", what_prefix='"', what_suffix='"', ctc="ctc",  ctc_position="fixed")
    define gents = Character("The Dogs", what_prefix='"', what_suffix='"', ctc="ctc",  ctc_position="fixed")
    define bl = Character("Vlad", what_prefix='"', what_suffix='"', ctc="ctc",  ctc_position="fixed")
    define bo1 = Character("Stefano", what_prefix='"', what_suffix='"', ctc="ctc",  ctc_position="fixed")
    define wai = Character("Adam", what_prefix='"', what_suffix='"', ctc="ctc",  ctc_position="fixed")
    define unk = Character("???", what_prefix='"', what_suffix='"', ctc="ctc",  ctc_position="fixed")
    define unkm = Character("1. Male ???", what_prefix='"', what_suffix='"', ctc="ctc",  ctc_position="fixed")
    define unkm2 = Character("2. Male ???", what_prefix='"', what_suffix='"', ctc="ctc",  ctc_position="fixed")
    define unkf = Character("1. Female ???", what_prefix='"', what_suffix='"', ctc="ctc",  ctc_position="fixed")
    define unkf2 = Character("2. Female ???", what_prefix='"', what_suffix='"', ctc="ctc",  ctc_position="fixed")
    define stra = Character("Raymond", what_prefix='"', what_suffix='"', ctc="ctc",  ctc_position="fixed")
    define ruti = Character("Dennis", what_prefix='"', what_suffix='"', ctc="ctc",  ctc_position="fixed")
    define gia = Character("Giovanni", what_prefix='"', what_suffix='"', ctc="ctc",  ctc_position="fixed")
    define luc = Character("Emily", what_prefix='"', what_suffix='"', ctc="ctc",  ctc_position="fixed")
    define vio = Character("Viola", what_prefix='"', what_suffix='"', ctc="ctc",  ctc_position="fixed")
    define lau = Character("Jimmy", what_prefix='"', what_suffix='"', ctc="ctc",  ctc_position="fixed")

init python:
    config.gestures = { "n_s" : "hide_windows", "e" : "toggle_skip", "w_e" : "game_menu", "w" : "rollback" }
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
        girl = Actor("Aura", 100, [Punch, Kick, Magic, Defend, Inventory_sk, Flee], max_mp=50)
        hers = CharStats(strength=40)
        boy = CharStats(intelligence=40) #For later use

        ramen = Item("Ramen", hp=50, player=girl, image="gui/inv_ramen.png")
        red_pill = Item("Red Pill", hp=100, player=girl, image="gui/inv_red_pill.png")
        cola = Item("Cola", mp=25, player=girl, image="gui/inv_cola.png")
        black_pill = Item("Black Pill", mp=50, player=girl, image="gui/inv_black_pill.png")
        # bullet = Item("Bullet", ammo=1, player=girl, image="gui/inv_musket.png")
        # box = Item("Box of Bullets", ammo=5, player=girl, image="gui/inv_laser.png")
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
    scene bg room test
    # jump drunk_text
    # $ rename(g, girl)
    jump chp_1
    narrator "Start story"

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
    #
    # jump drunk_text

    ###############
    #Play escape movie here
    jump dungeon1

label chp_1:
    "This young man is about to take two tests today."
    $ rename(mc)
    jump first_test
label after_test_2:
    # Classroom scene
    scene dozing
    mk "Philosophy is something that has been taught and in question for generations. Your assignment was to choose a philosophy that resonated with you and write a three page paper."
    "[mc.name]'s eyes twitch behind his eyelids. Drool begins to pool on his desk."
    mk "You will be receiving your papers back when you leave class today."
    # Transition to dream scene
    scene rain dream
    "Everyone including [mc.name]’s best friend Jason was listening intently to the professor. Meanwhile [mc.name] was drenched in darkness. In his dream all that could be seen was red flashing red lights and rain hitting the floor."
    mc "W-wait..."
    "There was a shadow figure a few feet ahead of him. He reaches out to touch it but it’s moving too fast as if it was running away."
    mc "Wait!"
    "The shadowy figure stops and looks back at him revealing two bright glowing eyes and then disappears into the distance."
    # Jump back to classroom scene, everyone looking at the dude
    scene teacher staring
    "[mc.name] screams out one more time for the figure to stop but this time it wasn’t just in his head. No the whole class heard him and the room fell into an awkward silence."
    mk "Why don’t you see me after class, [mc.name]."
    "Jason tries to conceal his laughter with his hand. [mc.name] couldn’t help but smirk at the dumb look he had on his face as he wiped his drool off his lip."
    mc "Yes sir."
    mk "Alright, that'll be all for today. Class dismissed. Come and pick up your papers before you leave."
    "Everyone files out of the room except [mc.name]."
    mk "Are you okay, [mc.name]? You don’t normally fall asleep in class like that."
    menu:
        "Yea, I’m fine. Sorry about that.":
            mk "Well don’t let it happen again. This is a place of learning, not sleeping."
        "To be honest I haven’t been sleeping very well.":
            mk "I’m sorry to hear that but you must find a way to get some sleep."
    mk "Well in any case [mc.name] job well done on your paper."
    "Mr. Kirk hands you the three paged writing assignment."
    mk "I will say I was surprised about the philosophy you chose...Solipsism huh? There is nothing that can be confirmed except this present moment."
    mc "And perhaps I’m the only person to exist and the entire world around me is just an illusion."
    mk "Fascinating."
    mc "Mr. Kirk if I did as well as you say, why is there an F on my paper."
    mk "It is because, Mr. Soma, I am a nihilist and therefore grades hold no intrinsic value. In that way anything can be valued as much or as little as you choose."
    mc "Ah I see."
    "He turns to leave."
    mk "Know that I value you very highly [mc.name]."
    mc "Thank you, sir."
    mk "Now get some sleep!"
    # Transition to outside of class
    scene tiger king
    "[mc.name] leaves the classroom and to his surprise someone is waiting for him just outside the building doors."
    jsn "Hey!"
    scene tiger bench
    mc "Hey, what’s up man."
    jsn "I swear you're the only person that would get caught sleeping in that class."
    mc "Haha... whatever dude."
    "He nudges you lightly"
    jsn "Anyways there’s a party tonight at the twins place. Heard shit's gonna get crazy, you in?"
    menu:
        "{i}(Sounds cool but I really should take Kirk's advice and get some sleep. I should make up a excuse.){/i}"
        "Sorry I have a huge assignment I have to get done.":
            mc "Sorry I have a huge assignment I have to get done."
            jsn "Mr. goodie goodie as always."
        "Maybe but I’m waiting on a call from my dad this evening.I don’t think I’ll be able to make it.":
            mc "Maybe but I’m waiting on a call from my dad this evening.I don’t think I’ll be able to make it."
            jsn "Alright man let me know if you change your mind."
    jsn "I’ll catch you later."
    mc "Alright, bye"
    scene dorm enter
    narrator "[mc.name] makes his way back to his dorm room. After setting his bag down, he grabs his headphones from the drawer he keeps them in."
    scene dorm bed with fade
    "Plugging them in, [mc.name] listens to soothing music and falls asleep."
    #Play dream movie 2 here?
    "When [mc.name] wakes up he sees on his phone that it's 7 pm."
    # play "phone_notification.ogg"
    "He gets a text from Jason.
    It's a picture of him partying with a bunch of girls."
    "It says \"Hey you coming or not?!\""
    mc "{i}(I do feel more rested, and for once I’m ahead on my work... maybe I should go out.){\i}"
    "He texts Jason back: \"Ya man see you soon.\""
    #Transition to Sorority scene
    scene party start
    "Kaleb knocks on the door and is greeted by the twins Sydnee and Ellie."
    sne "Hey, Kaleb! Come in, drinks are in the back corner.
    You can find your friend Jason nursing the keg stand."
    mc "Thanks!"
    jsn "HEEYYY, better late than never."
    "They dap each other up."
    jsn "Here, have a drink man."
    "Jason grabs a solo cup and fills it to the brim with beer."
    mc "Ah man you know I don’t really drink."
    jsn "You are tonight... here live a little man."
    "Kaleb goes for a sip but Jason yells “Chug chug” and soon the whole back of the room is too."
    "Kaleb chugs the beer which ends in everyone cheering."
    jsn "AYYEE, that’s my man and look you're not stopping until I say so."
    mc "Alright man."
    "Kaleb starts to make his rounds around the party but with every drink his vision starts to get hazier and things make less sense."
    jump drunk_text
label chp_1_party:
    scene concerned friend
    "At this point [mc.name] doesn’t even remember the girl he’s talking to."
    an "Hey, are you okay? You don’t look so hot."
    menu:
        "I’m fine, Jessie":
            pass
        "I’m fine, Emalee":
            pass
    an "My name is Annabelle."
    "She rolls her eyes and walks away."
    dude "OH SHIT IT'S CAMPUS SECURITY."
    "Everybody runs for the exit including Kaleb. At this point it 12am and pouring outside. It’s a short walk from the sorority house to his dorm room but it feels worse when you're drunk and scared. He begins running in a direction that seems familiar."
    mc "{i}(I hope Jason made it out okay.){\i}"
    "Then he stops suddenly in his tracks. The lights from the security cars can still be seen behind him. He sees a familiar shadowy figure. Except he can see upon further inspection that it’s a girl and she isn’t running. In fact she’s staring right at him."
    mc "H-hello?"
    "He reaches out with the strangest sense of deja vu."
    "Maybe it was the beer finally getting ahead of him or him just being overwhelmed but he collapses onto the street floor."
    "He opens his eyes one last time to see her standing over him and swears she could see a little glow in her eyes."
    jump the_end

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

label the_end:
    scene black
