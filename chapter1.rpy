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

init:
    screen letter_a:
        imagebutton:
            auto "letter a"
            action [Show("letter a", 170, 534), Hide("letter_a")]
            xpos random.randrange(0, 1280)
            ypos random.randrange(0, 441)
    screen letter_b:
        imagebutton:
            auto "letter b"
            action [Show("letter b", 560, 627), Hide("letter_b")]
            xpos random.randrange(0, 1280)
            ypos random.randrange(0, 441)
    screen letter_c:
        imagebutton:
            auto "letter c"
            action [Show("letter c", 370, 627), Hide("letter_c")]
            xpos random.randrange(0, 1280)
            ypos random.randrange(0, 441)
    screen letter_d:
        imagebutton:
            auto "letter d"
            action [Show("letter d", 360, 534), Hide("letter_d")]
            xpos random.randrange(0, 1280)
            ypos random.randrange(0, 441)
    screen letter_e:
        imagebutton:
            auto "letter e"
            action [Show("letter e", 350, 441), Hide("letter_e")]
            xpos random.randrange(0, 1280)
            ypos random.randrange(0, 441)
    screen letter_f:
        imagebutton:
            auto "letter f"
            action [Show("letter f", 455, 534), Hide("letter_f")]
            xpos random.randrange(0, 1280)
            ypos random.randrange(0, 441)
    screen letter_g:
        imagebutton:
            auto "letter g"
            action [Show("letter g", 550, 534), Hide("letter_g")]
            xpos random.randrange(0, 1280)
            ypos random.randrange(0, 441)
    screen letter_h:
        imagebutton:
            auto "letter h"
            action [Show("letter h", 645, 534), Hide("letter_h")]
            xpos random.randrange(0, 1280)
            ypos random.randrange(0, 441)
    screen letter_i:
        imagebutton:
            auto "letter i"
            action [Show("letter i", 645, 441), Hide("letter_i")]
            xpos random.randrange(0, 1280)
            ypos random.randrange(0, 441)
    screen letter_j:
        imagebutton:
            auto "letter j"
            action [Show("letter j", 740, 534), Hide("letter_j")]
            xpos random.randrange(0, 1280)
            ypos random.randrange(0, 441)
    screen letter_k:
        imagebutton:
            auto "letter k"
            action [Show("letter k", 835, 534), Hide("letter_k")]
            xpos random.randrange(0, 1280)
            ypos random.randrange(0, 441)
    screen letter_l:
        imagebutton:
            auto "letter l"
            action [Show("letter l", 930, 534), Hide("letter_l")]
            xpos random.randrange(0, 1280)
            ypos random.randrange(0, 441)
    screen letter_m:
        imagebutton:
            auto "letter m"
            action [Show("letter m", 750, 627), Hide("letter_m")]
            xpos random.randrange(0, 1280)
            ypos random.randrange(0, 441)
    screen letter_n:
        imagebutton:
            auto "letter n"
            action [Show("letter n", 665, 627), Hide("letter_n")]
            xpos random.randrange(0, 1280)
            ypos random.randrange(0, 441)
    screen letter_o:
        imagebutton:
            auto "letter o"
            action [Show("letter o", 740, 441), Hide("letter_o")]
            xpos random.randrange(0, 1280)
            ypos random.randrange(0, 441)
    screen letter_p:
        imagebutton:
            auto "letter p"
            action [Show("letter p", 835, 441), Hide("letter_p")]
            xpos random.randrange(0, 1280)
            ypos random.randrange(0, 441)
    screen letter_q:
        imagebutton:
            auto "letter q"
            action [Show("letter q", 160, 441), Hide("letter_q")]
            xpos random.randrange(0, 1280)
            ypos random.randrange(0, 441)
    screen letter_r:
        imagebutton:
            auto "letter r"
            action [Show("letter r", 445, 441), Hide("letter_r")]
            xpos random.randrange(0, 1280)
            ypos random.randrange(0, 441)
    screen letter_s:
        imagebutton:
            auto "letter s"
            action [Show("letter s", 265, 534), Hide("letter_s")]
            xpos random.randrange(0, 1280)
            ypos random.randrange(0, 441)
    screen letter_t:
        imagebutton:
            auto "letter t"
            action [Show("letter t", 540, 441), Hide("letter_t")]
            xpos random.randrange(0, 1280)
            ypos random.randrange(0, 441)
    screen letter_u:
        imagebutton:
            auto "letter u"
            action [Show("letter u", 730, 441), Hide("letter_u")]
            xpos random.randrange(0, 1280)
            ypos random.randrange(0, 441)
    screen letter_v:
        imagebutton:
            auto "letter v"
            action [Show("letter v", 465, 627), Hide("letter_v")]
            xpos random.randrange(0, 1280)
            ypos random.randrange(0, 441)
    screen letter_w:
        imagebutton:
            auto "letter w"
            action [Show("letter w", 255, 441), Hide("letter_w")]
            xpos random.randrange(0, 1280)
            ypos random.randrange(0, 441)
    screen letter_x:
        imagebutton:
            auto "letter x"
            action [Show("letter x", 275, 627), Hide("letter_x")]
            xpos random.randrange(0, 1280)
            ypos random.randrange(0, 441)
    screen letter_y:
        imagebutton:
            auto "letter y"
            action [Show("letter y", 635, 441), Hide("letter_y")]
            xpos random.randrange(0, 1280)
            ypos random.randrange(0, 441)
    screen letter_z:
        imagebutton:
            auto "letter z"
            action [Show("letter z", 180, 627), Hide("letter_z")]
            xpos random.randrange(0, 1280)
            ypos random.randrange(0, 441)

label drunk_text:
    python:
        letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        for letter in letters:
            renpy.show("letter_" + letter)
