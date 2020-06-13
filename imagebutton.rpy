# standard settings menu 
define gui . choice_button_width =  1280 
define gui . choice_button_height =  72 
define gui . choice_button_borders = Borders ( 150 , 16 , 150 , 16 )
define gui . choice_button_text_xalign =  0.5 
define pad =  150  # indent for the picture on the left

init python:
    # automatic image announcement
    images_auto ()
    window_center ()

    # search for tags with button settings 
    import  re 
    def  get_tags (text, prefix = '#' ):
         # fish out all remark tags 
        return re . findall ( '{'  + prefix +  '([^}] +)}' , text)

    # search in the tag string (and its values) by the name 
    def  get_tag (text, tag, default = None ):
        val = default
        tags = get_tags (text)
         for i in tags:
            parts = i . split ( '=' )
             if  len (parts) >  0 :
                 if parts [ 0 ] . strip () == tag . strip ():
                     if  len (parts) >  1 :
                        val = parts [ 1 ]
         return val

    # find in the remarks the value of the tag 'image' 
    def  get_image (text):
         # by default there is no picture 
        return get_tag (text, 'image' )

    # find the value of the tag 'align' 
    def  get_align (text) in remarks :
         # by default, align text we take the standard 
        return  float (get_tag (text, 'align' , str (gui . choice_button_text_xalign)))

# reassign selection screen
screen choice (items):
    style_prefix "choice"
    vbox:
        for i in items:
            button:
                action i . action
                background None 
                xpadding 0 ypadding 0 xmargin 0 ymargin 0 
                textbutton i . caption action i . action text_xalign get_align (i . caption)
                add get_image (i . caption) yalign . 5 xpos pad

label start:
    menu:
        "Text in the center" :
             pass 
        "{# image = vk} Text in the center, left picture" :
             pass 
        "{image = vk} Text in the center, picture next to the text" :
             pass 
        "{# image = vk} {image = pref} The text with the picture in the center, the picture on the left " :
             pass 
        " {# image = vk} The picture on the left, the text on the right {# align = 1.0} " :
             pass 
        " {image = pref} The text with the picture on the left {# align = .0 } " :
             pass 
        " {# image = vk} {image = pref} Text with a picture on the left and a picture on the left {# align = .25} " :
             pass 
    return
