define r = Character('Red Hood', color="#CD0000")
define w = Character('mr.Wolf', color="#B5B5B5")

screen simple_stats_screen:
    frame:
        xalign 0.01 yalign 0.05
        xminimum 220 xmaximum 220
        vbox:
            text "Red Hood" size 22 xalign 0.5
            null height 5
            hbox:
                bar:
                    xmaximum 130
                    value red_hood_hp
                    range red_hood_max_hp
                    left_gutter 0
                    right_gutter 0
                    thumb None
                    thumb_shadow None
                    
                null width 5
                
                text "[red_hood_hp] / [red_hood_max_hp]" size 16
                
                
    frame:
        xalign 0.99 yalign 0.05
        xminimum 220 xmaximum 220
        vbox:
            text "mr.Wolf" size 22 xalign 0.5
            null height 5
            hbox:
                bar:
                    xmaximum 130
                    value wolf_hp
                    range wolf_max_hp
                    left_gutter 0
                    right_gutter 0
                    thumb None
                    thumb_shadow None
                    
                null width 5
                
                text "[wolf_hp] / [wolf_max_hp]" size 16
                
    text "Red Hood vs. mr.Wolf" xalign 0.5 yalign 0.05 size 30
                
# The game starts here.
label battle_game_1:
    #### Some variables that describes the game state.
    $ wolf_max_hp = 30
    $ red_hood_max_hp = 50
    $ wolf_hp = wolf_max_hp
    $ red_hood_hp = red_hood_max_hp
    $ cookies_left = 13
    
    scene black
    
    "Once upon a time there lived in a certain village a little country girl, the prettiest creature who was ever seen."
    "Her mother was excessively fond of her; and her grandmother doted on her still more."
    "This good woman had a little red riding hood made for her. It suited the girl so extremely well that everybody called her Little Red Riding Hood."
    "One day her mother, having made some cookies, said to her, \"Go, my dear, and see how your grandmother is doing, for I hear she has been very ill. Take her some cookies, and this little pot of butter."
    "Little Red Riding Hood set out immediately to go to her grandmother, who lived in another village."
    "As she was going through the wood, she met with a wolf, who had a very great mind to eat her up, but {w}suddenly..."
    jump battle_1_loop


label battle_1_loop:
    
    #### Let's show the game screen.
    #
    show screen simple_stats_screen
    
    #### The game loop.
    # It will exist till both enemies have more than 0 hp.
    #
    while (wolf_hp > 0) and (red_hood_hp > 0):
        
        menu:
            "Atack!":
                $ wolf_hp -= 2
                r "K-y-aaa!!!11 (damage dealt - 2hp)"
                
            "Eat cookie (got [cookies_left] cookies left)" if cookies_left > 0:
                $ red_hood_hp = min(red_hood_hp+5, red_hood_max_hp)
                $ cookies_left -= 1
                r "Mmm, tasty... (restore 5hp)"
        
        $ wolf_damage = renpy.random.randint(1, 6)
        
        $ red_hood_hp -= wolf_damage
        
        w "RrrrrRRrrrr! {i}*wolf bites you*{/i} (damage dealt - [wolf_damage]hp)"
    #
    ####        
        
    hide screen simple_stats_screen
    
    if wolf_hp <= 0:
        if red_hood_hp <= 0:
            "Double KO"
            
        else:
            r "I wiiiin!!!!!111"
            r "Finally, mom sew me a grey hood."
            "(grandmother got [cookies_left] cookies)"
            
    else:
        w "Om-nom-nom-nom {i}*wolf ate you all up*{/i} (along with the basket, of course...)"
    
    jump battle_1_ending
        
label battle_1_ending:
    "The end."
    return
