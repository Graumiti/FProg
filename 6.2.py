from graphics import *
from facenew import Face
import time


def main():
    win_width, win_height = 700, 400  # Dimensões da janela
    win = GraphWin("Animação do Círculo", win_width, win_height)
    win.setBackground("white")
    x, y = win_width // 2, win_height // 2  # Posição inicial do círculo, a meio do ecrã
    size = 50
    center = Point(x,y)
    dx, dy = 1, 1  # Velocidade do movimento

    circle = Face(win, center, size)


    while True:
        time.sleep(0.01)  # Controla a velocidade da animação
        circle.move(dx, dy)

        center = circle.getCenter()
        x, y = center.getX(), center.getY() #conforme o tempo, pega sempre a posição do centro do circulo.

        # Verifica a posição do circulo, relativamente a xx e yy e inverte a direção quando toca nos limites da janela
        if x - size <= 0 or x + size >= win_width:
            dx = -dx
        if y - size <= 0 or y + size >= win_height:
            dy = -dy

        if win.checkMouse():  # Permite encerrar ao clicar na janela
            break # quebra do ciclo while, enquanto o utilizador não clicar na janela, o programa corre indefinitivamente.

    win.close()

main()