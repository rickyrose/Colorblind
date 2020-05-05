screen checkMouse():
   if standWalk==0:
       key "mousedown_1" action Jump("checkDist")


###############################################################################


label start:      
   scene bg starpre
   show screen checkMouse


label stand1:
   $ standWalk=0

   if 220<walkDegree<320:
       show Semi standB:
           xpos int(SemX-(37*sZ))
           ypos int(SemY-(150*sZ))
           zoom sZ

   elif 40<walkDegree<140:
       show Semi standF:
           xpos int(SemX-(37*sZ))
           ypos int(SemY-(150*sZ))
           zoom sZ

   elif 90<walkDegree<270:
       show Semi standL:
           xpos int(SemX-(37*sZ))
           ypos int(SemY-(150*sZ))
           zoom sZ

   else:
       show Semi stand:
           xpos int(SemX-(37*sZ))
           ypos int(SemY-(150*sZ))
           zoom sZ


   if inArea(SemX,SemY,240, 420, 335, 480):
       menu:
           "Do you want to go down the stairs?"
           "Yes":
               pass
           "No":
               pass

   elif inArea(SemX,SemY,332, 307, 434, 320):  
       menu:
           "Do you want to take a closer look at the painting at the wall?"
           "Yes":
               pass
           "No":
               pass

   elif inArea(SemX,SemY,542, 316, 592, 340):
       "The door is locked. I don't know how to open it."
       $ standWalk=0

   $ renpy.pause(hard=True)



label walk:
   $ standWalk=1    

   if 220<walkDegree<320:
       show Semi WalkUp:
           xpos int(SemX-(37*sZ))
           ypos int(SemY-(150*sZ))
           zoom sZ
           linear dist/100.0 xpos int(mX-(37*mZ)) ypos int(mY-(150*mZ)) zoom mZ

   elif 40<walkDegree<140:
       show Semi WalkDown:
           xpos int(SemX-(37*sZ))
           ypos int(SemY-(150*sZ))
           zoom sZ
           linear dist/100.0 xpos int(mX-(37*mZ)) ypos int(mY-(150*mZ)) zoom mZ

   elif 90<walkDegree<270:
       show Semi WalkLeft:
           xpos int(SemX-(37*sZ))
           ypos int(SemY-(150*sZ))
           zoom sZ
           linear dist/100.0 xpos int(mX-(37*mZ)) ypos int(mY-(150*mZ)) zoom mZ

   else:
       show Semi WalkRight:
           xpos int(SemX-(37*sZ))
           ypos int(SemY-(150*sZ))
           zoom sZ
           linear dist/100.0 xpos int(mX-(37*mZ)) ypos int(mY-(150*mZ)) zoom mZ


   $ renpy.pause(delay=dist/100.0, hard=True)
   $ SemX=mX
   $ SemY=mY
   $ sZ=mZ

   if sX2>0:
       $ mX=sX2
       $ mY=sY2
       $ sX2=0
       $ sY2=0
       jump cd2
   else:
       jump stand1



label checkDist:
   python:
       mX=renpy.get_mouse_pos()[0]
       mY=renpy.get_mouse_pos()[1]

label cd2:
   python:

       if inArea(mX,mY,0, 0, 254, 406) and inArea(SemX,SemY,0, 406, 640, 480):   ### 2 step
           sX2=mX
           sY2=mY
           mX= 307
           mY= 389

       elif inArea(SemX,SemY,0, 0, 254, 406) and inArea(mX,mY,246, 406, 640, 480):  #### 2 step
           sX2=mX
           sY2=mY
           mX= 307
           mY= 389

       elif inArea(mX,mY,0, 406, 246, 480):
           mX= 298
           mY= 456
           if inArea(SemX,SemY,0, 0, 254, 406):
               sX2=mX
               sY2=mY
               mX= 307
               mY= 389


       elif inArea(mX,mY,307, 164, 442, 263):
           mX= 369
           mY= 318

       elif inArea(mX,mY,571, 214, 594, 320):
           mX= 562
           mY= 325

       elif inArea(mX,mY,0, 391, 174, 407):
           mX= 150
           mY= 405

       if mY<315:
           mY=315


       if mX<205 and 313<mY<396:
           if mX<205-(0.8642*(mY-313)):                
               mX = int(205-(0.8642*(mY-313)))

       if mX>558 and 378>mY:
           if mX>558+(0.31429*(mY-309)):
               mX = int(558+(0.31429*(mY-309)))

       if mX>580 and 379<mY:
           if mX>580+(0.81481*(mY-379)):
               mX = int(580+(0.81481*(mY-379)))

       xD = SemX-mX
       yD = SemY-mY
       dist = (xD**2)+(yD**2)
       dist= math.sqrt(dist)

       mZ= 0.6 + ((mY-315)*0.00276)
       if mZ<0.6:
           mZ=0.6
       elif mZ>1.0:
           mz=1.0

       walkDegree = math.degrees(math.atan2(yD, xD))+180


   jump walk
