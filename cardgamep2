image tb = "tb.webp"
screen c78a:
    if btnn<5:
        textbutton "Another card" xalign .5 yalign .5 action [SetVariable("karta"+str(btnn),renpy.random.randint(2,11)),SetVariable("kartam"+str(btnn),renpy.random.choice([100,200,300,400])),SetVariable("kart"+str(btnn),renpy.random.randint(2,11)),SetVariable("kartm"+str(btnn),renpy.random.choice([100,200,300,400])),SetVariable("btnn",btnn+1),Jump("cpui")]
    textbutton "Enough" xalign .5 yalign .54 action Jump("cstand")
screen c78:
    hbox xalign .1:
        add str(kart1+kartm1)+".png"
        add str(kart2+kartm2)+".png"
        add str(kart3+kartm3)+".png"
        add str(kart4+kartm4)+".png"
    hbox xalign .1 yalign .94:
        add str(karta1+kartam1)+".png"
        add str(karta2+kartam2)+".png"
        add str(karta3+kartam3)+".png"
        add str(karta4+kartam4)+".png"
label card78:
    scene tb
    $ btnn=2
    $ kart1=renpy.random.randint(2,11)
    $ kartm1=renpy.random.choice([100,200,300,400])
    $ karta1=renpy.random.randint(2,11)
    $ kartam1=renpy.random.choice([100,200,300,400])
    $ kart2=0
    $ kart3=0
    $ kart4=0
    $ kartm2=0
    $ kartm3=0
    $ kartm4=0
    $ karta2=0
    $ karta3=0
    $ karta4=0
    $ kartam2=0
    $ kartam3=0
    $ kartam4=0
    $ cpupoint=kart1
    $ ipoint=karta1
label bgme:
    show screen c78
    show screen c78a
    e "Opponent - [cpupoint]\n Your cards - [ipoint]"
    jump bgme
label cpui:
    if cpupoint>16:
        if btnn==4:
            $ kart3=0
            $ kartm3=0
        if btnn==5:
            $ kart4=0
            $ kartm4=0
    $ cpupoint=kart1+kart2+kart3+kart4
    $ ipoint=karta1+karta2+karta3+karta4
    if cpupoint>21:
        if kart1==11:
            $ kart1=1
        elif kart2==11:
            $ kart2=1
        elif kart3==11:
            $ kart3=1
        elif kart4==11:
            $ kart4=1
        $ cpupoint=kart1+kart2+kart3+kart4
    if ipoint>21:
        if karta1==11:
            $ karta1=1
        elif karta2==11:
            $ karta2=1
        elif karta3==11:
            $ karta3=1
        elif karta4==11:
            $ karta4=1
        $ ipoint=karta1+karta2+karta3+karta4
    jump bgme
label cstand:
    hide screen c78a
    $ cpupoint=kart1+kart2+kart3+kart4
    $ ipoint=karta1+karta2+karta3+karta4
    if ipoint>21:
        if cpupoint>21:
            e "Draw"
        else:
            e "Losing bust"
    elif cpupoint>21:
        e "Victory"
    elif ipoint==cpupoint:
        e "Draw"
    elif ipoint>cpupoint:
        if cpupoint<17:
            if kart2==0:
                $ kart2=renpy.random.randint(2,11)
                $ kartm2=renpy.random.choice([100,200,300,400])
                jump cstand
            elif kart3==0:
                $ kart3=renpy.random.randint(2,11)
                $ kartm3=renpy.random.choice([100,200,300,400])
                jump cstand
            elif kart4==0:
                $ kart4=renpy.random.randint(2,11)
                $ kartm4=renpy.random.choice([100,200,300,400])
                jump cstand
        e "Victory"
    else:
        e "Loss"
    return
