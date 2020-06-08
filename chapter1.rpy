# Test minigame
label first_test:
    "[mc.name] received his first test of the day: Biochemistry."
    "He looked at the first question on the test."
    menu:
        "What chemical is used as energy in the cell?"
        "ATP":
            "Yeah, that seems right."
            boy.intelligence += 5
        "DNA":
            "I'm really just guessing here..."
        "Glucose":
            "Cells need sugar, right?"
            boy.intelligence += 1
        "Mitochondria":
            "The powerhouse of the cell, of course."
    mc "{i}OK, that was a tough one but most of these are pretty easy.{\i}"
    mc "{i}Hmm. This one's a little tricky though."
    menu:
        "Is the cell membrane hydrophobic or hydrophillic?"
        "Hydrophobic":
            "Cell membranes are lipids, so they must be hydrophobic. Right?"
            boy.intelligence += 1
        "Hydrophillic":
            "The cell membrane is permeable, so it has to be hydrophillic. Right?"
            boy.intelligence += 1
        "Hydroponic":
            "The right answer is always C."
        "Both":
            "Cell membranes are made of two layers of lipids, with a hydrophobic head and hydrophillic tails."
            boy.intelligence += 5
    mc "{i}Nearly finished. Just one question still stumping me...{\i}"
    menu:
        "How many amino acids can human cells synthesize?"
        "22":
            "That's the number of amino acids used to build proteins."
            boy.intelligence += 1
        "20":
            "Two of the amino acids used in protein sysnthesis aren't encoded in DNA, so human cells can't synthesize them."
            boy.intelligence += 1
        "11":
            "Of the 20 standard amino acids, human cells cannot synthesize 9."
            boy.intelligence += 5
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
            boy.intelligence += 5
        "aa":
            "I recall something similar for blue eyes. Those are recessive traits."
            boy.intelligence += 1
    mc "{i}That one was pretty easy. I hope the rest are like this.{\i}"
    mc "{i}Hey, that question looks pretty easy.{\i}"
    menu:
        "What are the 4 letters used to represent the nucleotides in RNA?"
        "ABCD":
            "I think my finger slipped..."
        "GCAT":
            "The same nucleotides as DNA, of course."
            boy.intelligence += 1
        "GCAU":
            "Uracil replaces Thymine in RNA."
            boy.intelligence += 5
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
            boy.intelligence += 1
        "The peppered moth developed weaker eyesight because the lights of humans attracted the moths and killed many of them":
            "Moths do like light."
        "The peppered moth evolved camouflage in response to humans altering the environment":
            "Yeah, they got darker when the industrial revolution made the trees sooty and they got lighter when environmental protection policies were enacted."
            boy.intelligence += 5
