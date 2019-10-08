from graphics import *
import random as rnd
win = GraphWin("Wing", 400, 400)

def draw_house(x = 0, y = 0, k = 1, col = "yellow", smoke = 1, light = 1):
    Pipe = Rectangle(Point(x+k*130, y+k*80), Point(x+k*160,y+k*140))
    Pipe.setFill("Black")
    Pipe.draw(win)
    
    House = Rectangle(Point(x+k*100, y+k*150), Point(x+k*300,y+k*250))
    House.setFill(col)
    House.draw(win)
    
    Roof = Polygon(Point(x+k*100,y+k*150), Point(x+k*300,y+k*150), Point(x+k*200,y+k*80))
    Roof.setFill("Red")
    Roof.draw(win)
    
    Door = Rectangle(Point(x+k*230,y+k*170), Point(x+k*270,y+k*240))
    Door.setFill("Black")
    Door.draw(win)
    
    Window = Rectangle(Point(x+k*125,y+k*175), Point(x+k*165, y+k*215))
    Window.setFill("Black")
    if (light == 1): Window.setFill("White")
    Window.draw(win)
    
    Smoke1 = Oval(Point(x+k*130,y+k*80), Point(x+k*160,y+k*60))
    Smoke1.setFill("Grey")
    if (smoke == 1): Smoke1.draw(win)
    
    Smoke2 = Oval(Point(x+k*140,y+k*70), Point(x+k*165,y+k*55))
    Smoke2.setFill("White")
    if (smoke == 1): Smoke2.draw(win)
    
    Line1 = Line(Point(x+k*145, y+k*175), Point(x+k*145,y+k*215))
    Line1.draw(win)
    
    Line2 = Line(Point(x+k*125,y+k*195), Point(x+k*165,y+k*195))
    Line2.draw(win)
    
    Hand = Oval(Point(x+k*260,y+k*213), Point(x+k*265,y+k*220))
    Hand.setFill("White")
    Hand.draw(win)

def draw_sun(x = 0, y = 0, k = 1, col = "yellow"):
    Sun1part = Polygon(Point(x+k*30,y+k*30), Point(x+k*80,y+k*30), Point(x+k*55,y+k*80))
    Sun1part.setFill(col)

    Sun2part = Polygon(Point(x+k*55,y+k*17), Point(x+k*30,y+k*67.26), Point(x+k*80, y+k*67.26))
    Sun2part.setFill(col)

    Sun1part.setOutline(col)
    Sun2part.setOutline(col)

    Sun1part.draw(win)
    Sun2part.draw(win)
    
def draw_pond(x = 0, y = 0, k = 1, col = "blue"):
    PondSide = Oval(Point(x+k*142.9,y+k*285.7), Point(x+k*367.5,y+k*367.5))
    PondSide.setFill("Yellow")
    PondSide.draw(win)

    Pond = Oval(Point(x+k*150,y+k*300), Point(x+k*350,y+k*350))
    Pond.setFill(col)
    Pond.draw(win)
    
def dopil(move,  move_x, move_y, move_x_2, move_y_2, x, y, height, width, body_color, window, numb_of_move = 0, numb_of_move_2 = 0, timer = 0.1, k = 1):
    if move == False:
        body = Oval(Point(x, y + height / 4), Point(x + width, y + 5 * height / 7))
        head = Oval(Point(x, y), Point(x + width, y + height / 4))
        leg1 = Line(Point(x + width / 2, y + 4 * height / 7), Point(x, y + height))
        leg2 = Line(Point(x + width / 2, y + 4 * height / 7), Point(x + width, y + height))
        arm1 = Line(Point(x + width / 8, y + 6 * height / 16), Point(x - width / 3, y + 4 * height / 7))
        arm2 = Line(Point(x + 7 * width / 8, y + 6 * height / 16), Point(x + 4 * width / 3, y + 4 * height / 7))
        eye1 = Circle(Point(x + width / 4, y + height / 16), 1)
        eye2 = Circle(Point(x + 3 * width / 4, y + height / 16), 1)
        mouth = Line(Point(x + width / 3, y + 3 * height / 16), Point(x + 2 * width / 3, y + 3 * height / 16))

        body.setFill(body_color)
        head.setFill(body_color)
        leg1.setOutline(body_color)
        leg2.setOutline(body_color)
        arm1.setOutline(body_color)
        arm2.setOutline(body_color)
        mouth.setOutline("red")
        eye1.setFill("blue")
        eye2.setFill("blue")

        arm1.setWidth(3)
        arm2.setWidth(3)
        leg1.setWidth(3)
        leg2.setWidth(3)

        head.draw(window)
        leg1.draw(window)
        leg2.draw(window)
        arm1.draw(window)
        arm2.draw(window)
        body.draw(window)
        eye2.draw(window)
        eye1.draw(window)
        mouth.draw(window)
        Door_2.setFill("Black")
        Hand_2.setFill("White")
        head.undraw()
        leg1.undraw()
        leg2.undraw()
        arm1.undraw()
        arm2.undraw()
        body.undraw()
        eye2.undraw()
        eye1.undraw()
        mouth.undraw()

    elif move == True :
        body = Oval(Point(x, y + height / 4), Point(x + width, y + 5 * height / 7))
        head = Oval(Point(x, y), Point(x + width, y + height / 4))
        leg1 = Line(Point(x + width / 2, y + 4 * height / 7), Point(x, y + height))
        leg2 = Line(Point(x + width / 2, y + 4 * height / 7), Point(x + width, y + height))
        arm1 = Line(Point(x + width / 8, y + 6 * height / 16), Point(x - width / 3, y + 4 * height / 7))
        arm2 = Line(Point(x + 7 * width / 8, y + 6 * height / 16), Point(x + 4 * width / 3, y + 4 * height / 7))
        eye1 = Circle(Point(x + width / 4, y + height / 16), 1)
        eye2 = Circle(Point(x + 3 * width / 4, y + height / 16), 1)
        mouth = Line(Point(x + width / 3, y + 3 * height / 16), Point(x + 2 * width / 3, y + 3 * height / 16))

        body.setFill(body_color)
        head.setFill(body_color)
        leg1.setOutline(body_color)
        leg2.setOutline(body_color)
        arm1.setOutline(body_color)
        arm2.setOutline(body_color)
        mouth.setOutline("red")
        eye1.setFill("blue")
        eye2.setFill("blue")

        arm1.setWidth(3)
        arm2.setWidth(3)
        leg1.setWidth(3)
        leg2.setWidth(3)

        head.draw(window)
        leg1.draw(window)
        leg2.draw(window)
        arm1.draw(window)
        arm2.draw(window)
        body.draw(window)
        eye2.draw(window)
        eye1.draw(window)
        mouth.draw(window)
        
    
        for i in range(numb_of_move):
            head.move(move_x, move_y)
            leg1.move(move_x, move_y)
            leg2.move(move_x, move_y)
            arm1.move(move_x, move_y)
            arm2.move(move_x, move_y)
            body.move(move_x, move_y)
            eye1.move(move_x, move_y)
            eye2.move(move_x, move_y)
            mouth.move(move_x, move_y)
            time.sleep(timer)
        for i in range(numb_of_move_2):
            head.move(move_x_2, move_y_2)
            leg1.move(move_x_2, move_y_2)
            leg2.move(move_x_2, move_y_2)
            arm1.move(move_x_2, move_y_2)
            arm2.move(move_x_2, move_y_2)
            body.move(move_x_2, move_y_2)
            eye1.move(move_x_2, move_y_2)
            eye2.move(move_x_2, move_y_2)
            mouth.move(move_x_2, move_y_2)
            time.sleep(timer)
        head.undraw()
        leg1.undraw()
        leg2.undraw()
        arm1.undraw()
        arm2.undraw()
        body.undraw()
        eye2.undraw()
        eye1.undraw()
        mouth.undraw()






def brizgi():
    for i in range(30):
        radius = rnd.uniform(1,3)
        koord_x = rnd.uniform(-100,100)
        koord_y = rnd.uniform(0,-30)
        c = Circle(Point(255 - koord_x, 280 + koord_y), radius)
        c.setFill("Blue")
        c.setOutline("Blue")
        c.draw(win)
        for k in range(5):
            move_x_ = rnd.uniform(-5,5)
            move_y_ = rnd.uniform(-5,5)
            c.move(-move_x_, move_y_)
            time.sleep(0.05)
        c.undraw()









    
    
Grass = Rectangle(Point(0,210), Point(400,400))
Grass.setFill("Green")
Grass.draw(win)

Sky = Rectangle(Point(0,0), Point(400,210))
Sky.setFill("Light Blue")
Sky.draw(win)

coords = Point(200, 200)
velocity = Point(1, -2)
acceleration = Point(0, 0.1)


draw_house()
draw_sun()
draw_pond()
dopil(True, 1, 0, 1, -1, 0, 200, 70, 30, "Grey", win, 200, 30, 0.01, 0.5)

Door_2 = Rectangle(Point(230,170), Point(270,240))
Door_2.setFill("Orange")
Door_2.draw(win)
time.sleep(1)
Door_2.setFill("Black")
Hand_2 = Oval(Point(260,213), Point(265,220))
Hand_2.setFill("White")
Hand_2.draw(win)

brizgi()

Door_2.setFill("Orange")
Hand_2.setFill("Orange")
time.sleep(1)

dopil(False, 0, 0, 0, 0, 250, 170, 70, 30, "Grey", win, 0, 0, 0, 0.5)

dopil(True, 1, 1, 1, 0, 250, 170, 70, 30, "Grey", win, 30, 200, 0.01, 0.5)


i = 0
while (i<2):
	print(i)
	i+=1

win.getMouse()
win.close()
