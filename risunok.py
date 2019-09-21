from graphics import *
from math import *

win = GraphWin("Test1", 820, 680)	#create window of size 300x300

def RT(x1, y1, x2, y2, col):
    L = Rectangle(Point(x1, y1), Point(x2, y2))
    L.setFill(col)
    L.setWidth(5)
    L.draw(win)

def TRI(x1, y1, x2, y2, x3, y3, col):
    L = Polygon(Point(x1, y1), Point(x2, y2), Point(x3, y3))
    L.setFill(col)
    L.setWidth(5)
    L.draw(win)
    
def ELL(x1, y1, x2, y2, col):
    L = Oval(Point(x1, y1), Point(x2, y2))
    L.setFill(col)
    L.setWidth(5)
    L.draw(win)
    
#Прямоугольники на рисунке
RT(0, 0, 820, 680, "#1E90FF") #Небо
RT(0, 570, 820, 680, "#ADFF2F") #Трава
RT(100, 320, 400, 600, "#FF8C00") #Основная стена
RT(100, 530, 400, 600, "#B22222") #Фундамент
RT(400, 440, 490, 600, "#FFA500") #Пристройка
RT(310, 225, 360, 320, "#B22222") #Труба
RT(410, 480, 470, 600, "#8B4513") #Дверь
RT(263, 340, 373, 505, "#00FFFF") #Правое окно
RT(127, 340, 237, 505, "#00FFFF") #Левое окно
RT(660, 340, 720, 600, "#800000") #Ствол

#Треугольники на рисунке
TRI(80, 320, 250, 200, 420, 320, "#FF4500") #Главная крыша
TRI(400, 370, 400, 440, 490, 440, "#FF4500") #Крыша пристройки

#Эллипсы на рисунке
ELL(450, 535, 460, 545, "#708090") #Ручка двери
ELL(30, 30, 130, 130, "#FFFF00") #Солнце
ELL(590, 330, 750, 400, "#ADFF2F") #Крона 1
ELL(570, 170, 800, 370, "#008000") #Крона 2
ELL(580, 180, 650, 217, "#ADFF2F") #Крона 3
ELL(700, 396, 790, 450, "#ADFF2F") #Крона 4
ELL(572, 428, 685, 506, "#008000") #Крона 5
ELL(326, 176, 394, 212, "#C0C0C0") #Дым 1
ELL(367, 130, 475, 180, "#808080") #Дым 2
ELL(440, 74, 575, 138, "#696969") #Дым 3

#Лучики
for i in range(0, 10):
    L = Line(Point(80+75*cos(i*2*pi/10), 80+75*sin(i*2*pi/10)), Point(80+130*cos(i*2*pi/10), 80+130*sin(i*2*pi/10)))
    if (i % 2 == 1): 
        L.setOutline("yellow")
    else: 
        L.setOutline("black")
    L.setWidth(5)
    L.draw(win)

win.getMouse()
win.close()