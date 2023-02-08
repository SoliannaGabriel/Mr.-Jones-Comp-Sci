from cmu_graphics import *
color=input('type a color: ')
 

Circle(200,100,90,fill=color)
Circle(130,170,50,fill=color)
Circle(200,170,50,fill=color)
Circle(270,170,50,fill=color)
# the circles make the tops of the leaves, while the small circles make the sides of the leaves.
Rect(164,200,70,200,fill='saddlebrown')
# the recangles are the trunks of the trees!
Circle(30,100,90,fill=color)
Circle(100,170,50,fill=color)
Circle(30,170,50,fill=color)
Rect(0.5,200,70,200,fill='saddlebrown')
Circle(370,100,90,fill=color)
Circle(310,170,50,fill=color)
Circle(385,170,50,fill=color)
Rect(330,200,65,200,fill='saddlebrown')
cmu_graphics.run()