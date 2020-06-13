# an example of using parallax:

# label start: 
    # $ mouse_parallax.set ((- 20, -5, "l0"), (-40, -10, "l1"), (-60, -15, "l2")) 
    # $ showp ( "city0", "city1", "city2", "bg room") 
    # with dissolve 
    # "Move the mouse. \ nNormal parallax. The layers closest to the camera move more strongly." 
    # $ scenep () 
    # with dissolve 
    # $ mouse_parallax.set ((- 60, -15, "l0"), (-40, -10, "l1"), (-20, -5, "l2")) 
    # $ showp ("city0", "city1", "city2", "bg room") 
    # with dissolve 
    # "Move the mouse. \ nMirror parallax. The values ​​for shifting the layers are reset. Now the far layers move stronger. As if we are looking in the mirror . "
    
    
    

init 1111 python:
     # parallax 
    class class  MouseParallax (renpy . Displayable):
         def  set ( self , * args):
             self . xoffset, self . yoffset =  0.0 , 0.0 
            self . layer_info = args
             for i in  self . layers ():
                 if i in config . layers + ["master2" ]:
                    config . layers . remove (i)
            index = config . layers . index ( "master" ) +  1 
            for xdist, ydist, layer in args:
                 if  not layer in config . layers:
                    config . layers . insert (index, layer)
                    index + =  1 
            config . layers . insert (index, "master2" )

        def  __init__ ( self , * args):
             super (renpy . Displayable, self ) . __init __ ()
             self . set ( * args)
            config . overlay_functions . append ( self . overlay)
             return

        def  layers ( self ):
            layers = []
             for dx, dy, layer in  self . layer_info:
                layers . insert ( 0 , layer)
             return layers

        def  render ( self , width, height, st, at):
             return renpy . Render (width, height)

        def  parallax ( self , xdist, ydist):
            func = renpy . curry (trans) (xdist = xdist, ydist = ydist, disp = self )
             return Transform (function = func)

        def  overlay ( self ):
            ui . add ( self )
             for xdist, ydist, layer in  self . layer_info:
                renpy . layer_at_list ([ self . parallax (xdist, ydist)], layer)
             return

        def  event ( self , ev, x, y, st):
             import  pygame 
            if ev . type == pygame . MOUSEMOTION:
                 self . xoffset, self . yoffset = (( float ) (x) / (config . screen_width)) -  0.5 , (( float ) (y) / (config . screen_height)) -  0.5 
            return

    def  trans (d, st, at, xdist = None , ydist = None , disp = None ):
        d . xoffset, d . yoffset =  int ( round (xdist * disp . xoffset)), int ( round (ydist * disp . yoffset))
         if xdist ! =  0  or ydist ! =  0 :
            xzoom = (config . screen_width +  abs (xdist + xdist)) /  float (config . screen_width)
            yzoom = (config . screen_height +  abs (ydist + ydist)) /  float (config . screen_height)
             if yzoom > xzoom:
                d . zoom = yzoom
             else :
                d . zoom = xzoom
            d . anchor = ( . 5 , 1.0 )
            d . align = ( . 5 , 1.0 )
         return  0

    # a list for storing images indicating layers 
    parallax_images = []

    # show several images, each on its own parallax layer 
    # you can use the transform effect or even several 
    # the number of images should not exceed the number of layers 
    # otherwise the extra ones will be displayed on the master2 layer on top of the rest 
    # $ showp ("city1", ("city2", truecenter), ("city3", [truecenter, woo])) 
    def  showp ( * args):
         global parallax_images
        layers = mouse_parallax . layers ()
         for i in args:
            at = []
            image = i
             if  isinstance (image, tuple ):
                image, at = image
                 if  not  isinstance (at, list ):
                    at = [at]
            l =  "master2" 
            if  len (layers) >  0 :
                l = layers . pop ()
            renpy . show (image, at_list = at, layer = l)
            i = (image, l)
             if  not i in parallax_images:
                parallax_images . append (i)

    # remove one image from the specified (or from any) layer 
    def  hidep (image, layer = None ):
         global parallax_images
         if  not layer:
            layer =  "master2" 
            for ii, ll in parallax_images:
                 if ii == image:
                    layer = ll
        i = (image, layer)
        renpy . hide (image, layer = layer)
         if i in parallax_images:
            parallax_images . remove (i)

    # clear all parallax layers 
    # and if necessary add new images 
    def  scenep ( * args):
         global parallax_images
         for i in parallax_images:
            image, layer = i
            renpy . hide (image, layer = layer)
        parallax_images = []
         if args:
            showp ( * args)

    mouse_parallax = MouseParallax (( - 60 , - 15 , "l0" ), ( - 40 , - 10 , "l1" ), ( - 20 , - 5 , "l2" ))

