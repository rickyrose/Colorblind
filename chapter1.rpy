init -2 python:
    import random
    import renpy.exports as renpy

# Test minigame
label first_test:
    "[mc.name] received his first test of the day: Biochemistry."
    "He looked at the first question on the test."
    menu:
        "What chemical is used as energy in the cell?"
        "ATP":
            "Yeah, that seems right."
            $ boy.intelligence += 5
        "DNA":
            "I'm really just guessing here..."
        "Glucose":
            "Cells need sugar, right?"
            $ boy.intelligence += 1
        "Mitochondria":
            "The powerhouse of the cell, of course."
    mc "{i}OK, that was a tough one but most of these are pretty easy.{\i}"
    mc "{i}Hmm. This one's a little tricky though."
    menu:
        "Is the cell membrane hydrophobic or hydrophillic?"
        "Hydrophobic":
            "Cell membranes are lipids, so they must be hydrophobic. Right?"
            $ boy.intelligence += 1
        "Hydrophillic":
            "The cell membrane is permeable, so it has to be hydrophillic. Right?"
            $ boy.intelligence += 1
        "Hydroponic":
            "The right answer is always C."
        "Both":
            "Cell membranes are made of two layers of lipids, with a hydrophobic head and hydrophillic tails."
            $ boy.intelligence += 5
    mc "{i}Nearly finished. Just one question still stumping me...{\i}"
    menu:
        "How many amino acids can human cells synthesize?"
        "22":
            "That's the number of amino acids used to build proteins."
            $ boy.intelligence += 1
        "20":
            "Two of the amino acids used in protein sysnthesis aren't encoded in DNA, so human cells can't synthesize them."
            $ boy.intelligence += 1
        "11":
            "Of the 20 standard amino acids, human cells cannot synthesize 9."
            $ boy.intelligence += 5
        "4":
            "There are 4 types of rungs in the DNA ladder, which must mean there are 4 amino acids."
    mc "{i}All done. And just in time, too.{\i}"
    # jump after_test
label second_test:
    "[mc.name] received his second test of the day: Genetics."
    menu:
        "What is the proper way of indicating that an individual is a carrier of a recessive allele?"
        "AA":
            "That's how I'm used to seeing alleles talked about in my books"
        "aA":
            "Little and then big like pH, right?"
        "Aa":
            "Dominant traits are represented by capital letters, and recessive traits by lowercase letters."
            $ boy.intelligence += 5
        "aa":
            "I recall something similar for blue eyes. Those are recessive traits."
            $ boy.intelligence += 1
    mc "{i}That one was pretty easy. I hope the rest are like this.{\i}"
    mc "{i}Hey, that question looks pretty easy.{\i}"
    menu:
        "What are the 4 letters used to represent the nucleotides in RNA?"
        "ABCD":
            "I think my finger slipped..."
        "GCAT":
            "The same nucleotides as DNA, of course."
            $ boy.intelligence += 1
        "GCAU":
            "Uracil replaces Thymine in RNA."
            $ boy.intelligence += 5
        "GCRT":
            "The A is replaced by an R because it's RNA."
    "[mc.name] continued answering questions. He started to slow as he felt the effects of the caffeine fading."
    mc "{i}Wow, I am getting pretty tired. I feel like I should know the answer to this question...{\i}"
    menu:
        "What how did the peppered moth evolve due to human influence?"
        "Humans domesticated the moths, making them larger and more docile":
            "Moths sure are useful!"
        "The peppered moth remained the same color because humans took them from the wild when their habitat was destroyed":
            "I remember that the moths were white before and after the industrial revolution..."
            $ boy.intelligence += 1
        "The peppered moth developed weaker eyesight because the lights of humans attracted the moths and killed many of them":
            "Moths do like light."
        "The peppered moth evolved camouflage in response to humans altering the environment":
            "Yeah, they got darker when the industrial revolution made the trees sooty and they got lighter when environmental protection policies were enacted."
            $ boy.intelligence += 5
    jump after_test

init -2:
    screen letter_a:
        imagebutton:
            idle "letter a"
            action [ToggleDict(key_flags, "s"),
                    ToggleDict(key_flags, "n"),
                    SetDict(key_flags, "a", True),
                    ToggleDict(key_flags, "c"),
                    ToggleDict(key_flags, "k")]
            pos positions[0]
    screen right_a:
        add "letter a" xpos 170 ypos 534
    screen letter_b:
        imagebutton:
            idle "letter b"
            action [SetDict(key_flags, "b", True),
                    ToggleDict(key_flags, "e"),
                    ToggleDict(key_flags, "a"),
                    ToggleDict(key_flags, "r"),
                    ToggleDict(key_flags, "d")]
            pos positions[1]
    screen right_b:
        add "letter b" xpos 560 ypos 627
    screen letter_c:
        imagebutton:
            idle "letter c"
            action [SetDict(key_flags, "c", True),
                    ToggleDict(key_flags, "b"),
                    ToggleDict(key_flags, "u"),
                    ToggleDict(key_flags, "s"),
                    ToggleDict(key_flags, "t")]
            pos positions[2]
    screen right_c:
        add "letter c" xpos 370 ypos 627
    screen letter_d:
        imagebutton:
            idle "letter d"
            action [SetDict(key_flags, "d", True),
                    ToggleDict(key_flags, "w"),
                    ToggleDict(key_flags, "v"),
                    ToggleDict(key_flags, "r"),
                    ToggleDict(key_flags, "s")]
            pos positions[3]
    screen right_d:
        add "letter d" xpos 360 ypos 534
    screen letter_e:
        imagebutton:
            idle "letter e"
            action [SetDict(key_flags, "e", True),
                    ToggleDict(key_flags, "r"),
                    ToggleDict(key_flags, "u"),
                    ToggleDict(key_flags, "s"),
                    ToggleDict(key_flags, "t")]
            pos positions[4]
    screen right_e:
        add "letter e" xpos 350 ypos 441
    screen letter_f:
        imagebutton:
            idle "letter f"
            action [SetDict(key_flags, "f", True),
                    ToggleDict(key_flags, "a"),
                    ToggleDict(key_flags, "l"),
                    ToggleDict(key_flags, "e"),
                    ToggleDict(key_flags, "x")]
            pos positions[5]
    screen right_f:
        add "letter f" xpos 455 ypos 534
    screen letter_g:
        imagebutton:
            idle "letter g"
            action [SetDict(key_flags, "g", True),
                    ToggleDict(key_flags, "c"),
                    # ToggleDict(key_flags, "a"),
                    ToggleDict(key_flags, "u"),
                    ToggleDict(key_flags, "m")]
            pos positions[6]
    screen right_g:
        add "letter g" xpos 550 ypos 534
    screen letter_h:
        imagebutton:
            idle "letter h"
            action [SetDict(key_flags, "h", True),
                    ToggleDict(key_flags, "e"),
                    ToggleDict(key_flags, "u"),
                    ToggleDict(key_flags, "r"),
                    ToggleDict(key_flags, "o")]
            pos positions[7]
    screen right_h:
        add "letter h" xpos 645 ypos 534
    screen letter_i:
        imagebutton:
            idle "letter i"
            action [SetDict(key_flags, "i", True),
                    ToggleDict(key_flags, "c"),
                    ToggleDict(key_flags, "h"),
                    ToggleDict(key_flags, "a"),
                    ToggleDict(key_flags, "d")]
            pos positions[8]
    screen right_i:
        add "letter i" xpos 825 ypos 441
    screen letter_j:
        imagebutton:
            idle "letter j"
            action [SetDict(key_flags, "j", True),
                    ToggleDict(key_flags, "n"),
                    ToggleDict(key_flags, "g"),
                    ToggleDict(key_flags, "l"),
                    ToggleDict(key_flags, "e")]
            pos positions[9]
    screen right_j:
        add "letter j" xpos 740 ypos 534
    screen letter_k:
        imagebutton:
            idle "letter k"
            action [SetDict(key_flags, "k", True),
                    ToggleDict(key_flags, "i"),
                    ToggleDict(key_flags, "c"),
                    ToggleDict(key_flags, "u"),
                    ToggleDict(key_flags, "p")]
            pos positions[10]
    screen right_k:
        add "letter k" xpos 835 ypos 534
    screen letter_l:
        imagebutton:
            idle "letter l"
            action [SetDict(key_flags, "l", True),
                    ToggleDict(key_flags, "i"),
                    ToggleDict(key_flags, "z"),
                    ToggleDict(key_flags, "r"),
                    ToggleDict(key_flags, "d")]
            pos positions[11]
    screen right_l:
        add "letter l" xpos 930 ypos 534
    screen letter_m:
        imagebutton:
            idle "letter m"
            action [SetDict(key_flags, "m", True),
                    ToggleDict(key_flags, "i"),
                    ToggleDict(key_flags, "t"),
                    ToggleDict(key_flags, "x"),
                    ToggleDict(key_flags, "n")]
            pos positions[12]
    screen right_m:
        add "letter m" xpos 750 ypos 627
    screen letter_n:
        imagebutton:
            idle "letter n"
            action [SetDict(key_flags, "n", True),
                    ToggleDict(key_flags, "o"),
                    ToggleDict(key_flags, "s"),
                    ToggleDict(key_flags, "u"),
                    ToggleDict(key_flags, "p")]
            pos positions[13]
    screen right_n:
        add "letter n" xpos 655 ypos 627
    screen letter_o:
        imagebutton:
            idle "letter o"
            action [SetDict(key_flags, "o", True),
                    ToggleDict(key_flags, "w"),
                    ToggleDict(key_flags, "r"),
                    ToggleDict(key_flags, "s"),
                    ToggleDict(key_flags, "t")]
            pos positions[14]
    screen right_o:
        add "letter o" xpos 920 ypos 441
    screen letter_p:
        imagebutton:
            idle "letter p"
            action [SetDict(key_flags, "p", True),
                    ToggleDict(key_flags, "s"),
                    ToggleDict(key_flags, "c"),
                    ToggleDict(key_flags, "y"),
                    ToggleDict(key_flags, "h")]
            pos positions[15]
    screen right_p:
        add "letter p" xpos 1015 ypos 441
    screen letter_q:
        imagebutton:
            idle "letter q"
            action [SetDict(key_flags, "q", True),
                    ToggleDict(key_flags, "a"),
                    ToggleDict(key_flags, "c"),
                    ToggleDict(key_flags, "r"),
                    ToggleDict(key_flags, "b")]
            pos positions[16]
    screen right_q:
        add "letter q" xpos 160 ypos 441
    screen letter_r:
        imagebutton:
            idle "letter r"
            action [SetDict(key_flags, "r", True),
                    ToggleDict(key_flags, "w"),
                    ToggleDict(key_flags, "h"),
                    ToggleDict(key_flags, "o"),
                    ToggleDict(key_flags, "e")]
            pos positions[17]
    screen right_r:
        add "letter r" xpos 445 ypos 441
    screen letter_s:
        imagebutton:
            idle "letter s"
            action [SetDict(key_flags, "s", True),
                    ToggleDict(key_flags, "l"),
                    ToggleDict(key_flags, "g"),
                    ToggleDict(key_flags, "h"),
                    ToggleDict(key_flags, "r")]
            pos positions[18]
    screen right_s:
        add "letter s" xpos 265 ypos 534
    screen letter_t:
        imagebutton:
            idle "letter t"
            action [SetDict(key_flags, "t", True),
                    ToggleDict(key_flags, "i"),
                    ToggleDict(key_flags, "e"),
                    ToggleDict(key_flags, "v"),
                    ToggleDict(key_flags, "l")]
            pos positions[19]
    screen right_t:
        add "letter t" xpos 540 ypos 441
    screen letter_u:
        imagebutton:
            idle "letter u"
            action [SetDict(key_flags, "u", True),
                    ToggleDict(key_flags, "q"),
                    ToggleDict(key_flags, "t"),
                    ToggleDict(key_flags, "p"),
                    ToggleDict(key_flags, "i")]
            pos positions[20]
    screen right_u:
        add "letter u" xpos 730 ypos 441
    screen letter_v:
        imagebutton:
            idle "letter v"
            action [SetDict(key_flags, "v", True),
                    ToggleDict(key_flags, "i"),
                    ToggleDict(key_flags, "x"),
                    ToggleDict(key_flags, "e"),
                    ToggleDict(key_flags, "n")]
            pos positions[21]
    screen right_v:
        add "letter v" xpos 465 ypos 627
    screen letter_w:
        imagebutton:
            idle "letter w"
            action [SetDict(key_flags, "w", True),
                    ToggleDict(key_flags, "v"),
                    ToggleDict(key_flags, "x"),
                    ToggleDict(key_flags, "y"),
                    ToggleDict(key_flags, "z")]
            pos positions[22]
    screen right_w:
        add "letter w" xpos 255 ypos 441
    screen letter_x:
        imagebutton:
            idle "letter x"
            action [SetDict(key_flags, "x", True),
                    ToggleDict(key_flags, "g"),
                    ToggleDict(key_flags, "o"),
                    ToggleDict(key_flags, "l"),
                    ToggleDict(key_flags, "d")]
            pos positions[23]
    screen right_x:
        add "letter x" xpos 275 ypos 627
    screen letter_y:
        imagebutton:
            idle "letter y"
            action [SetDict(key_flags, "y", True),
                    ToggleDict(key_flags, "k"),
                    ToggleDict(key_flags, "w"),
                    ToggleDict(key_flags, "r"),
                    ToggleDict(key_flags, "j")]
            pos positions[24]
    screen right_y:
        add "letter y" xpos 635 ypos 441
    screen letter_z:
        imagebutton:
            idle "letter z"
            action [SetDict(key_flags, "z", True),
                    ToggleDict(key_flags, "j"),
                    ToggleDict(key_flags, "o"),
                    ToggleDict(key_flags, "g"),
                    ToggleDict(key_flags, "m")]
            pos positions[25]
    screen right_z:
        add "letter z" xpos 180 ypos 627
    screen clear_keys:
        imagebutton:
            idle "gui/frame.png"
            action [SetDict(key_flags, "a", False), SetDict(key_flags, "b", False), SetDict(key_flags, "c", False),
                    SetDict(key_flags, "d", False), SetDict(key_flags, "e", False), SetDict(key_flags, "f", False),
                    SetDict(key_flags, "g", False), SetDict(key_flags, "h", False), SetDict(key_flags, "i", False),
                    SetDict(key_flags, "j", False), SetDict(key_flags, "k", False), SetDict(key_flags, "l", False),
                    SetDict(key_flags, "m", False), SetDict(key_flags, "n", False), SetDict(key_flags, "o", False),
                    SetDict(key_flags, "p", False), SetDict(key_flags, "q", False), SetDict(key_flags, "r", False),
                    SetDict(key_flags, "s", False), SetDict(key_flags, "t", False), SetDict(key_flags, "u", False),
                    SetDict(key_flags, "v", False), SetDict(key_flags, "w", False), SetDict(key_flags, "x", False),
                    SetDict(key_flags, "y", False), SetDict(key_flags, "z", False)]
            pos (0.9, 0.9)
label drunk_text:
    window hide
    python:
        event_check=False
        config.rollback_enabled=False
        letters = [ "a","b","c","d","e","f","g","h","i","j","k","l","m",
                    "n","o","p","q","r","s","t","u","v","w","x","y","z"]
        positions = [(random.randrange(0,1200), random.randrange(0, 350)) for l in letters]
        directions = [(random.randrange(-8,9), random.randrange(-4,5)) for l in letters]
        key_flags = {} # Used to determine when all the buttons have been placed.
        for letter in letters:
            key_flags[letter] = False
            renpy.show_screen("letter_" + letter)
        renpy.show_screen("clear_keys")
        while False in key_flags.values():
            for i in range(0, 26):
                if not key_flags[letters[i]]:
                    renpy.show_screen("letter_" + letters[i])
                    renpy.hide_screen("right_" + letters[i])
                    if directions[i][0] == 0 and directions[i][1] == 0:
                        directions[i] = (random.randrange(-8,9), random.randrange(-4,5))
                    positions[i] = tuple(map(sum, zip(positions[i], directions[i])))
                    if positions[i][0] <= 0:
                        positions[i] = (0, positions[i][1])
                        directions[i] = (random.randrange(0, 9), directions[i][1])
                    elif positions[i][0] >= 1200:
                        positions[i] = (1200, positions[i][1])
                        directions[i] = (random.randrange(-8, 1), directions[i][1])
                    if positions[i][1] <= 0:
                        positions[i] = (positions[i][0], 0)
                        directions[i] = (directions[i][0], random.randrange(0, 5))
                    elif positions[i][1] >= 350:
                        positions[i] = (positions[i][0], 350)
                        directions[i] = (directions[i][0], random.randrange(-4, 1))
                else:
                    renpy.show_screen("right_" + letters[i])
                    renpy.hide_screen("letter_" + letters[i])
            renpy.pause(0.01)
    window show
    jump chp_1_party
