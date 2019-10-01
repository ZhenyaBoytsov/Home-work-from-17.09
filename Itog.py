from graphics import *
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
    
def dopil(x = 0, y = 0, k = 1):
    Golova = Oval(Point(x,y), Point(x+k*30,y+k*30))
    Golova.setFill("Orange")
    Golova.draw(win)
    
    Telo = Rectangle(Point(x,y+k*30), Point(x+k*30, y+k*70))
    Telo.setFill("Orange")
    Telo.draw(win)
    
    Stvol = Rectangle(Point(x+k*50,y+k*70), Point(x+k*80, y+k*250))
    Stvol.setFill("Brown")
    Stvol.draw(win)
    
    Krona = Oval(Point(x,y+k*30), Point(x+k*130,y+k*150))
    Krona.setFill("Green")
    Krona.draw(win)
    
    Lenta = Rectangle(Point(x+k*40,y+k*180), Point(x+k*90, y+k*200))
    Lenta.setFill("red")
    Lenta.draw(win)
    
    
Grass = Rectangle(Point(0,210), Point(400,400))
Grass.setFill("Green")
Grass.draw(win)

Sky = Rectangle(Point(0,0), Point(400,210))
Sky.setFill("Light Blue")
Sky.draw(win)

draw_house()
draw_sun()
draw_pond()
dopil(200, 200, 0.5)

win.getMouse()
win.close()