# vk.rpy module imitates a simplified copy of a blogger social network 
# colors and pictures are customizable, you can simulate another similar social network 


init python:
    # automatic image declaration 
    config . automatic_images_minimum_components =  1 
    config . automatic_images = [ '' , '_' , '/' ]
    config . automatic_images_strip = [ "images" ]

init - 999 python:
     # background colors can be replaced with constructs of type Frame ("imagename", 0, 0)

    # commenting option is enabled by default 
    vk_can_comment =  True

    # font of the post and comments 
    vk_font =  "fonts / Tahoma.ttf"

    # strip simulating social 
    media header vk_header =  "vk header"

    # cap height 
    vk_headerheight =  60

    # default 
    ava picture vk_avadefault =  "vk avadefault"

    # mask for cutting avatars 
    vk_ava_mask =  "vk avamask"

    # ava side size 
    vk_avasize =  72

    # picture for clicked 
    vk_likeon =  "vk likeon"

    # picture for 
    unpressed like vk_likeoff =  "vk likeoff"

    # suffix for reduced likes 
    vk_zoom =  "2"

    # picture for comment 
    vk_comment =  "vk comment"

    # username color in the header 
    vk_usercolor =  "#fff"

    # color for title text 
    vk_nickcolor =  "# 175490"

    # color for likes and comments 
    counter vk_countcolor =  "# 96A0B4"

    # color for the like counter when the button is pressed 
    vk_likecolor =  "# CB272F"

    # text color 
    vk_textcolor =  "# 000"

    # screen color outside the post 
    vk_screencolor =  "# EDEEF0"

    # screen color inside the post 
    vk_postcolor =  "#fff"

    # post width 
    vk_postwidth =  1080

    # screen height 
    vk_screenheight =  840

    # indent from the edge of the post to the content 
    # (1080 - 28 - 28 = 1024 - the optimal width for the image in the post) 
    vk_postpadding =  28

    # indent from avatar to comment content 
    vk_commpadding =  14

    # ava from user 
    vk_ava = vk_avadefault

    # username 
    vk_nickname = _ ( "Anon Anonych" )

    # pin size like text 
    vk_likesize =  24

    # 
    pins of header text vk_nicksize =  22

    # size of other text 
    vk_textsize =  20

    # a list of auto-replace the text of smiles on their images 
    vk_smiles = { ":)" : "vk smile smile" , ":(" : "vk smile sad" , "xD" : "vk smile rofl" , ": D" : "vk smile rofl " , " * up * " : " vk smile up " , " ↑ " : " vk smile up " }

    
    #class for the post class  VKpost :
         def  __init__ ( self , nick = _ ( "Anon Anonych" ), text = "" , ava = vk_avadefault, likes = 0 , user = False , comments = []):
             # avatar, cropped by mask (in a circle) 
            self . ava = AlphaMask (ava, renpy . easy . displayable (vk_ava_mask))
             self . nick = nick # author name
            self . text = text # post text 
            self . likes = likes # likes of the post 
            self . comments = comments # comments (list of VKpost instances) 
            self . count =  len (comments) # number of comments on this post 
            self . user = user # did the user like

        # get the number of comments on this post 
        def  get_com_count ( self ):
             return  len ( self . comments)

        # set / remove user’s like if user == True 
        # or just add a bunch of left likes 
        def  add_likes ( self , count = 1 , user = True ):
             if user:
                 if  self . user:
                     self . likes - =  1 
                else :
                     self . likes + =  1 
                self . user =  not  self . user
             else :
                self . likes + = count

    # list of posts in the feed 
    vk_posts = []

    # set user avatar 
    def  vk_set_ava (ava):
         global vk_ava
        vk_ava = AlphaMask (ava, renpy . easy . displayable (vk_ava_mask))

    # likes to the post 
    def  vk_post_add_like (i, count = 1 , user = True ):
         global vk_posts
         if i > =  0  and i <  len (vk_posts):
            vk_posts [i] . add_likes (count, user)
    VKPostAddLike = renpy . curry (vk_post_add_like)

    # 
    Likes to the comment def  vk_comm_add_like (i, ii, count = 1 , user = True ):
         global vk_posts
         if i > =  0  and i <  len (vk_posts):
             if ii > =  0  and ii <  len (vk_posts [i] . comments):
                vk_posts [i] . comments [ii] . add_likes (count, user)
    VKCommAddLike = renpy . curry (vk_comm_add_like)

    # refresh 
    def  repaint () screens :
        renpy . restart_interaction ()
    Repaint = renpy . curry (repaint)

    # add one post (but you can immediately list) 
    def  vk_add_post (post = []):
         global vk_posts
         if  not  isinstance (post, ( list , tuple )):
            post = [post]
         for i in post:
            vk_posts . append (i)
         # for scrolling 
        yadj . value = yadjValue
        renpy . restart_interaction ()
    VKAddPost = renpy . curry (vk_add_post)

    # add a comment (or several in the [list]) 
    def  vk_add_comm (comm, index = 0 ):
         global vk_posts
         if  not  isinstance (comm, list ):
            comm = [comm]
         for i in comm:
             # remove spaces around text 
            i . text = i . text . strip ()
             # remove double whitespace 
            while i . text . find ( "" ) > =  0 :
                i . text = i . text . replace ( "" , "" )
             # replace emoticons with smiley images 
            keys = vk_smiles . keys ()
             for k in keys:
                i . text = i . text . replace (k, "{image ="  + vk_smiles [k] +  "}" )
         # add comments 
        vk_posts [index] . comments = vk_posts [index] . comments + comm

    # define style (color) like 
    def  vk_like_style (user):
         if user:
             return  "vk_like_on" 
        return  "vk_like_off"

    # define comment picture 
    def  vk_comm_text (comments):
        count =  len (comments)
        text =  "{image ="  + vk_comment +  "}" 
        if count >  0 :
            text = text +  ""  +  str (count)
         else :
            text = text +  "" 
        return text

    # define like image 
    def  vk_like_text (user, count = 0 , zoom = "" ):
        text =  "{image ="  + vk_likeoff + zoom +  "}" 
        if user:
            text =  "{image ="  + vk_likeon + zoom +  "}" 
        if count >  0 :
            text = text +  ""  +  str (count)
         else :
            text = text +  "" 
        return text

    # Scroll to the very top 
    def  vk_scroll0 ():
        yadj . value =  0 
        renpy . restart_interaction ()

    # to scroll down when adding posts 
    yadjValue =  float ( "inf" )
    yadj = ui . adjustment ()

    # call the comment input routine 
    def  vk_input (i):
        renpy . call_in_new_context ( "vkinput" , i)
    VKinput = renpy . curry (vk_input)

init 999 :
     # style for the frame without indentation 
    style vk_empty is frame:
         # without indents 
        xpadding 0 ypadding 0 
        xmargin 0 ymargin 0 
        # top center 
        the align ( . 5 , . 0 )
         # background
        background vk_screencolor

    
    #style for the screen style vk_screen is vk_empty:
         # full screen 
        xminimum config . screen_width
        xmaximum config . screen_width
         # height is hardcoded
        yminimum vk_screenheight ymaximum vk_screenheight
        # The center of 
        the align ( . 5 , . 0 )
         # background
        background vk_screencolor

    
    #style for post style vk_post is vk_empty:
         # width is hard-coded
        xminimum vk_postwidth
        xmaximum vk_postwidth
        # indents from post border to content
        xpadding vk_postpadding
        ypadding vk_postpadding
        # ostupy between posts (and comments)
        ymargin vk_commpadding
        # The center of 
        the align ( . 5 , . 0 )
         # background
        background vk_postcolor

    # style for stripes with 
    likes style vk_likes is vk_empty:
         # width is hardcoded
        xminimum vk_postwidth
        xmaximum vk_postwidth
        # indent from post border to 
        xpadding content 0 ypadding 0 
        # vertical ostups
        ymargin vk_commpadding
        # The center of 
        the align ( . 5 , . 0 )
         # background
        background vk_postcolor

    # style for comment 
    style vk_comm is vk_empty:
         # left 
        xalign . 0 
        # less indentation 
        ymargin 0 
        # background 
        background None

    # Avytarok style for 
    style vk_avatar is vk_empty:
         # center left, 
        the align ( . 0 , . 0 )
         # size
        xminimum vk_avasize xmaximum vk_avasize 
        yminimum vk_avasize ymaximum vk_avasize 
        # background 
        background None

    # text 
    style style vk_text is text:
        size vk_textsize
        color vk_textcolor
        font vk_font

    # style text for title / name 
    style vk_nick is text:
        size vk_nicksize
        color vk_nickcolor
        bold true
        font vk_font

    #social screen
    screen vk:
        # screen
        frame:
            style "vk_screen"
            vbox:
                frame:
                    style "vk_empty"
                    yminimum vk_headerheight
                    ymaximum vk_headerheight
                    xfill True The 
                    # cap 
                    the add vk_header the align ( . 5 , . 0 )
                    hbox:
                        xalign . 8
                        spacing vk_commpadding
                        text vk_nickname style "vk_nick" color vk_usercolor yalign . 5
                        add vk_ava:
                            zoom . 75 
                            yalign . 5 
                # viewport for scrolling posts
                viewport:
                    id  "id vk" 
                    xinitial 1.0 
                    yfill False 
                    xfill False 
                    mousewheel True 
                    draggable True 
                    side_xfill False
                    transclude
                    yadjustment yadj
                    xalign . 5 
                    # all posts
                    vbox:
                        for i in  range ( len (vk_posts)):
                             # background of the post
                            frame:
                                style "vk_post"
                                vbox:
                                    spacing vk_commpadding # indent text from ava 
                                    # post title
                                    hbox:
                                        spacing vk_postpadding # distance between ava and title 
                                        # author avatar
                                        frame:
                                            style "vk_avatar" 
                                            add vk_posts [i] . ava
                                         # author name 
                                        text vk_posts [i] . style nick "vk_nick" 
                                    # text post 
                                    text vk_posts [i] . text style "vk_text" 
                                    # likes
                                    frame:
                                        style "vk_likes" 
                                        xpadding 0
                                        hbox:
                                            xalign . 0 
                                            # likes and number 
                                            textbutton vk_like_text (vk_posts [i] . User, vk_posts [i] . Likes ):
                                                action [VKPostAddLike (i), Repaint ()]
                                                style "vk_text" 
                                                if vk_posts [i] . user:
                                                    text_color vk_likecolor
                                                else :
                                                    text_color vk_countcolor
                                                text_size vk_likesize
                                                text_bold True 
                                                xminimum 96 
                                                yoffset 10 
                                            # number of comments 
                                            textbutton vk_comm_text (vk_posts [i] . comments):
                                                 if vk_can_comment:
                                                    action VKinput (i)
                                                else :
                                                    action []
                                                style "vk_text"
                                                text_color vk_countcolor
                                                text_size vk_likesize
                                                text_bold True 
                                                yoffset 10 
                                                xminimum 96 
                                    # comments 
                                    if  len (vk_posts [i] . comments) >  0 :
                                         # window of all comments
                                        frame:
                                            style "vk_comm" 
                                            xpadding 0
                                            vbox:
                                                #
                                                 iterate over comments for ii in  range ( len (vk_posts [i] . comments)):
                                                     # window for the next comment
                                                    frame:
                                                        style "vk_comm"
                                                        hbox:
                                                            spacing vk_commpadding
                                                            # commentator avatar
                                                            frame:
                                                                style "vk_avatar" 
                                                                add vk_posts [i] . comments [ii] . ava
                                                            vbox:
                                                                # commentator name 
                                                                text vk_posts [i] . comments [ii] . nick style "vk_nick" 
                                                                # comment 
                                                                text text vk_posts [i] . comments [ii] . text style "vk_text" 
                                                                # like comments
                                                                frame:
                                                                    style "vk_likes" 
                                                                    xpadding 0
                                                                    hbox:
                                                                        spacing vk_commpadding
                                                                        xalign . 8 
                                                                        # likes and numbers 
                                                                        textbutton vk_like_text (vk_posts [i] . Comments [ii] . User, vk_posts [i] . Comments [ii] . Likes, vk_zoom):
                                                                            action [VKCommAddLike (i, ii), Repaint ()]
                                                                            style "vk_text" 
                                                                            if vk_posts [i] . comments [ii] . user:
                                                                                text_color vk_likecolor
                                                                            else :
                                                                                text_color vk_countcolor
                                                                            vk_likesize text_size *  3  /  4 
                                                                            text_bold True The 
                                                                            yoffset 10

# user input comment routine
label vkinput (post_index):
    scene black
    $ text = renpy . input (_ ( "Enter your comment:" ))
     if text . strip ():
         $ vk_add_comm (VKpost (vk_nickname, text, vk_ava), post_index)
     return

# EXAMPLE OF USE: 
# on the tape screen, in addition to the likes, the comment button next to it
label vk_test:

    scene bg win

    # add post (s)
    python:
        # user avatar 
        vk_set_ava ( "7dots" )

        # nickname of user 
        vk_nickname = _ ( "" 7DOTS visual novels " )

        # zero out all posts 
        vk_posts = []

        # add posts 
        vk_add_post (VKpost (vk_nickname, "Such a maxim was born when discussing the acidity of the torn)) \ n \ n {image = post}" , vk_ava, 8 ))

        # Add comment to post number 0 
        vk_add_comm (VKpost (_ ( "Anonymous Anonistych" ), "Your games are shit!" , vk_avadefault, 1 ), 0 )

        # Add comment to post number 0 
        vk_add_comm (VKpost ( "Vovan Petrov" , "Ahahah xD" , "ava vovan" , 1 , True ), 0 )

        # adding a comment to post number 0 
        vk_add_comm (VKpost (vk_nickname, "* up * And these kamenty confirm my words :)" , vk_ava, 3 ), 0 )

    # rewind to the very top of the tape 
    $ vk_scroll0 ()

    # show vk screen
    show screen vk
    with dissolve

    # we are waiting for a click past the tape 
    "An example of how to simulate a simplified Vkontakte tape. You can like posts and comments. It is also possible to leave comments by entering them from the keyboard." 
    return
