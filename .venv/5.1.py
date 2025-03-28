from graphics import *
import time


def main():
    win_width, win_height = 700, 400  # Dimensões da janela
    win = GraphWin("Animação do Círculo", win_width, win_height)
    win.setBackground("white")

    radius = 20
    x, y = win_width // 2, win_height // 2  # Posição inicial do círculo, a meio do ecrã
    dx, dy = 1, 1  # Velocidade do movimento

    circle = Circle(Point(x, y), radius)
    circle.setFill("blue")
    circle.draw(win)

    while True:
        time.sleep(0.01)  # Controla a velocidade da animação
        circle.move(dx, dy)

        center = circle.getCenter()
        x, y = center.getX(), center.getY() #conforme o tempo, pega sempre a posição do centro do circulo.

        # Verifica a posição do circulo, relativamente a xx e yy e inverte a direção quando toca nos limites da janela
        if x - radius <= 0 or x + radius >= win_width:
            dx = -dx
        if y - radius <= 0 or y + radius >= win_height:
            dy = -dy

        if win.checkMouse():  # Permite encerrar ao clicar na janela
            break # quebra do ciclo while, enquanto o utilizador não clicar na janela, o programa corre indefinitivamente.

    win.close()

main()