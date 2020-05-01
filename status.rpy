# Tracking of the stats for the characters
init -3 python:
    import random

    class CharStats():
        def __init__(self, strength=20, intelligence=20, luck=0, reflexes=20):
            self.strength = strength
            self.intelligence = intelligence
            self.luck = luck
            self.reflexes = reflexes

        def upgrade(self):
            skill = renpy.random.randint(0,4)
            if skill is 0:
                self.strength += 10
            elif skill is 1:
                self.intelligence += 10
            elif skill is 2:
                self.luck += 1
            else:
                self.reflexes += 10

init:
    screen stats_screen:
        frame area(500, 0, 780, 400) background Frame("gui/frame.png", 22, 22) left_padding 20 right_padding 20:
            vbox yfill True:
                text "[girl.name]" outlines  [(1, "00000020", 0, 0)] color "#000"
                hbox xfill True:
                    text "Strength [hers.strength]" outlines  [(1, "00000020", 0, 0)] color "#000"
                hbox xfill True:
                    text "Intelligence [hers.intelligence]" outlines  [(1, "00000020", 0, 0)] color "#000"
                hbox xfill True:
                    text "Luck [hers.luck]" outlines  [(1, "00000020", 0, 0)] color "#000"
                hbox xfill True:
                    text "Reflexes [hers.reflexes]" outlines  [(1, "00000020", 0, 0)] color "#000"

                hbox align (.95,.04) spacing 20:
                    textbutton "Close Stats" action [ Hide("stats_screen"), Return(here)]
