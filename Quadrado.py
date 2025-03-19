from graphics import *
def main():

    win = GraphWin("click2rectangle", 400, 400)
    win.setCoords(x1 = -10, y1= -10, x2 = 10, y2 = 10)

    message = Text(Point(-0, 8), "Desenha um retangulo")
    message.draw(win)

#getmouse dá a posiçao do rato, escolhemos os pontos clicando na janela

    point1 = win.getMouse()
    point2 = win.getMouse()
    x1 = point1.getX()
    x2 = point2.getX()
    y1 = point1.getY()
    y2 = point2.getY()

#Calcula a area e o perimetro

    area = (x2 - x1)*(y2 - y1)
    perimeter = 2 * ((x2-x1)+(y2-y1))

#Draw Rectangle

    r = Rectangle(point1, point2)
    r.draw(win)

#dá print na área e perimetro do retangulo

    area = Text(Point(0, 7), ("A área do retângulo é", round(area, 2)))
    area.draw(win)
    perimetro = Text(Point(0, 6), ("O perímetro do retângulo é", round(perimeter, 2)))
    perimetro.draw(win)

    win.getMouse()
    win.close()

main()