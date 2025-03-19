#Exercício 4.2
#programa para fazer uma cara
#by: Pedro Gouveia & Miguel Cravo

from graphics import *
def main():

    # faz a janela, com titulo face, e dimensoes 900 por 900 e dá nos o sistema de coordenadas para desenhar
    win = GraphWin("Face", 900, 900)
    win.setCoords(0, 0, 10, 10)

    #desenha oval, pinta de castanho e deixa a linha da forma preta. depois clona e move para o outro lado da face
    ear1 = Oval(Point(1, 4.9), Point(3, 6.9))
    ear1.setFill('brown')
    ear1.setOutline('black')
    ear1.draw(win)
    ear2 = ear1.clone()
    ear2.move(6.7,0)
    ear2.draw(win)

    #cria a cabeça
    head = Oval(Point(1.5, 0.75), Point(9.25, 10.0))
    head.setFill("brown")
    head.draw(win)

    #cria os olhos e as iris e dps clone e move-as
    eye1 = Circle(Point(4.0, 6.75), .50)
    eye1.setFill("white")
    eye1.draw(win)
    iris1 = Circle(Point(4.0, 6.75), .25)
    iris1.setFill("black")
    iris1.draw(win)
    eye2 = eye1.clone()
    eye2.move(2.7, 0)
    eye2.draw(win)
    iris2 = iris1.clone()
    iris2.move(2.7, 0)
    iris2.draw(win)

    #cria nariz
    nose = Oval(Point(4.8, 4.2), Point(x=5.6, y= 6.25))
    nose.draw(win)

    #cria boca, pinta de preto, faz dentes e pinta-os de amarelo para contrastar
    mouth = Oval(Point(3, 2.5), Point(x=7.5, y= 4))
    mouth.setFill("black")
    mouth.draw(win)
    teeth = Rectangle(Point(4.8, 3.5), Point(5.3, 4))
    teeth.setFill('yellow')
    teeth.draw(win)

    #espera pelo click para terminar o programa
    win.getMouse()
    win.close()

main()