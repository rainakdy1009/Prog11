import turtle

x = "1"

while x == "1" :
    angle = input("Enter an angle: ")
    penColour = input("Enter a pen colour: ")
    lineLength = input ("Enter a line length: ")
    turtle.pencolor(penColour)
    turtle.left(float(angle))
    turtle.forward(float(lineLength))
    if lineLength == 0 :
        x = 0
    
    
