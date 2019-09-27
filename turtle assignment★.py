import turtle as tu #I'm gonna write 'tu' instead of 'turtle' when I write codes
from random import randint #The stars show up in random places

tu.bgcolor('black') #The background is black
tu.color('#D2D3D5') #This is the colour of the stars
tu.speed(0)


def draw_star():    
    turns = 0
    tu.begin_fill() #It starts to fill in the stars
    while turns < 5:   #the operations below will be repeated for 5 times so that it can draw a star
        tu.forward(25) #the turtle moves 25 steps and rotates in degree of 145.
        tu.left(145)
        turns = turns + 1
    tu.end_fill()

num_stars = 0
while num_stars < 40:  # 40 stars will show up in random places in certain area
    x = randint(-700, 300) #stars show up > x: between -700~300 and y: between 0~300
    y = randint(0, 300)
    draw_star()
    tu.pu()
    tu.goto(x,y)
    tu.pd()
    num_stars = num_stars + 1

def moon (x, Mcolor):
    tu.pu()
    tu.goto(x, 290)
    tu.color(Mcolor)
    tu.begin_fill()
    tu.pd()
    tu.circle(120)
    tu.end_fill()
    
moon (400, "yellow") #A black circle that has same radius with the yellow full moon will cover about half of it so it ultimately draws the crescent moon
moon (480, "black")

tu.pu()
tu.goto(-1400, -170)
tu.color('#6E6E6E')
tu.begin_fill()
tu.pd()
tu.seth(0)
tu.forward(2800)
tu.seth(-90)
tu.forward(400)
tu.seth(180)
tu.forward(2800)
tu.seth(90)
tu.forward(400)
tu.end_fill()

def wheels (x):
    for i in range(2): #the operations below is repeated for twice. I used "for colors in" to make colour gradation. 
        for colors in ["#FF4233", "#FF6B33", "#FFAC33", "#FFE333", "#BBFF33",
                       "#5EFF33", "#33FF8A", "#33FFDA", "#33E6FF", "#33A5FF",
                       "#3374FF", "#3633FF", "#7733FF", "#B533FF", "#EC33FF",
                       "#FF33C1", "#FF3383", "#FF3358", "#FF3333"]:
            tu.pu()
            tu.goto(x ,-220)
            tu.color(colors)
            tu.pd()
            tu.circle(25)
            tu.left(10)

wheels(-450)
wheels(-150)
        
tu.pu()
tu.goto(-450, -50)
tu.color("white")
tu.pensize(2)
tu.pd()

#This operation is for drawing the body of the car
tu.begin_fill()
tu.seth(0)
tu.forward(300)
tu.seth(-55)
tu.forward(80)
tu.seth(0)
tu.forward(70)
tu.seth(-90)
tu.forward(100)
tu.seth(180)
tu.forward(550)
tu.seth(90)
tu.forward(100)
tu.seth(0)
tu.forward(70)
tu.goto(-450, -50)
tu.end_fill()

def windows(x1, seth1, seth3, forward3): #draws the two windows of the car
    tu.pu()
    tu.goto(x1, -55)
    tu.color('black')
    tu.pd()
    tu.begin_fill()
    tu.seth(int(seth1))
    tu.forward(147.5)
    tu.seth(-90)
    tu.forward(60)
    tu.seth(int(seth3))
    tu.forward(int(forward3))
    tu.goto(x1, -55)
    tu.end_fill()

windows(-450, 0, 180, 205)
windows(-150, 180, 0, 189)


def light2(x1, seth1, forward1, seth2, forward2, forward3): #draw the orange light of the car
    tu.pu()
    tu.goto(x1, -115)
    tu.color('#FE7647')
    tu.pd()
    tu.begin_fill()
    tu.seth(int(seth1))
    tu.forward(int(forward1))
    tu.seth(int(seth2))
    tu.forward(int(forward2))
    tu.seth(90)
    tu.forward(int(forward3))
    tu.goto(x1, -115)
    tu.end_fill()

light2(-90, -80, 40, 0, 49, 38)
light2(-530, -100, 38, 180, 47, 36)

def light1(x1, seth1, forward1, seth2, forward2, forward3): #draw the yellow light of the car 
    tu.pu()
    tu.goto(x1, -115)
    tu.color('#FEFE47')
    tu.pd()
    tu.begin_fill()
    tu.seth(int(seth1))
    tu.forward(int(forward1))
    tu.seth(int(seth2))
    tu.forward(int(forward2))
    tu.seth(90)
    tu.forward(int(forward3))
    tu.goto(x1, -115)
    tu.end_fill()

light1(-83, -80, 33, 0, 43, 31.5)
light1(-537, -100, 31, 180, 42, 30)

def car_doors(x1, x2, seth2, forward2): #draw the car doors
    tu.pu()
    tu.goto(x1, -115)
    tu.color('black')
    tu.pensize(2)
    tu.pd()
    tu.seth(-90)
    tu.forward(88)
    tu.seth(int(seth2))
    tu.forward(int(forward2))
    tu.goto(x2, -115)

car_doors(-297.5, -108.5, - 0, 170)
car_doors(-303, -507.5, 180, 180)
    
def car_handles(x): #draw the car handles
    tu.pu()
    tu.goto(x, -120)
    tu.color('black')
    tu.pensize(2)
    tu.pd()
    tu.seth(-90)
    tu.forward(10)
    tu.seth(0)
    tu.forward(40)
    tu.seth(90)
    tu.forward(10)
    tu.goto(x, -120)

car_handles(-280)
car_handles(-490)

def PW_sticks(x): #draw the sticks of the pin wheels
        tu.pu()
        tu.goto(x, -350)
        tu.color('#88FE47')
        tu.pd()
        tu.begin_fill()
        tu.seth(90)
        tu.forward(150)
        tu.seth(0)
        tu.forward(16)
        tu.seth(-90)
        tu.forward(150)
        tu.seth(180)
        tu.forward(16)
        tu.end_fill()
        
PW_sticks(116)
PW_sticks(316)
PW_sticks(506)

def flower1(x, f1_color1, f1_color2, f1_color3, f1_color4, f1_color5, f1_color6): #draw the largest petals
    for i in range (3): 
        for f1_colors in [f1_color1, f1_color2, f1_color3, f1_color4, f1_color5, f1_color6]:
                        tu.pu()
                        tu.goto(x, -150)
                        tu.color(f1_colors)
                        tu.pd()
                        tu.begin_fill()
                        tu.pensize(3)
                        tu.forward(60)
                        tu.right(40)
                        tu.forward(60)
                        tu.right(140)
                        tu.forward(60)
                        tu.right(40)
                        tu.forward(60)
                        tu.end_fill()
                        tu.right(160)
       
flower1(124, "#77A4DE", "#5481BC", "#2E5C97", "#1C4273", "#0F2E55", "#051C39")
flower1(324, "#B063D4", "#8443A3", "#662B82", "#47175E", "#3F055B", "#28023A")
flower1(514, "#E3C96F", "#BCA450", "#917B2E", "#6D5A16", "#453808", "#392D01")

def flower2(x, f2_color): #draw the middle petals
    num_flower2 = 0
    while num_flower2 < 19:
        tu.pu()
        tu.goto(x, -150)
        tu.color(f2_color)
        tu.pd()
        tu.pensize(5)
        tu.forward(30)
        tu.right(50)
        tu.forward(30)
        tu.right(130)
        tu.forward(30)
        tu.right(50)
        tu.forward(30)
        tu.right(150)
        num_flower2 = num_flower2 + 1

flower2(124, "#B6EAFC")
flower2(324, "#AF94B8")
flower2(514, "#F2F906")

def flower3(x,f3_color): #draw the smallest petals
    for i in range (6):
            tu.pu()
            tu.goto(x, -150)
            tu.color(f3_color)
            tu.pd()
            tu.begin_fill()
            tu.circle(15)
            tu.left(60)

flower3(124, "#067EF9")
flower3(324, "#DF9AFF")
flower3(514, "white")

tu.done()
        
