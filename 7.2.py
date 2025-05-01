from graphics import *
import math

# Classe Cubo
class Cubo:
    def __init__(self, aresta):
        self.aresta = aresta

    def getAresta(self):
        return self.aresta

    def faceArea(self):
        return self.aresta ** 2

    def surfaceArea(self):
        return 6 * self.faceArea()

    def volume(self):
        return self.aresta ** 3

# Função para desenhar um cubo isométrico sem sair da janela
def desenhar_cubo(win, centro, lado_real):
    largura_max = 150  # tamanho máximo visual permitido
    fator_escala = min(largura_max / lado_real, 1)  # escalar para caber na tela
    lado = lado_real * fator_escala

    x, y = centro.getX(), centro.getY()
    deslocamento = lado / 2
    dx, dy = lado * 0.6, -lado * 0.6  # deslocamento da parte de trás

    # Pontos da face frontal
    p1 = Point(x - deslocamento, y + deslocamento)
    p2 = Point(x + deslocamento, y + deslocamento)
    p3 = Point(x + deslocamento, y - deslocamento)
    p4 = Point(x - deslocamento, y - deslocamento)

    # Pontos da face traseira
    p5 = Point(p1.getX() + dx, p1.getY() + dy)
    p6 = Point(p2.getX() + dx, p2.getY() + dy)
    p7 = Point(p3.getX() + dx, p3.getY() + dy)
    p8 = Point(p4.getX() + dx, p4.getY() + dy)

    # Frente
    for (a, b) in [(p1, p2), (p2, p3), (p3, p4), (p4, p1)]:
        Line(a, b).draw(win)

    # Traseira
    for (a, b) in [(p5, p6), (p6, p7), (p7, p8), (p8, p5)]:
        Line(a, b).draw(win)

    # Conexões
    for (a, b) in [(p1, p5), (p2, p6), (p3, p7), (p4, p8)]:
        Line(a, b).draw(win)

# Interface principal
def main():
    win = GraphWin("Calculadora de Cubo", 500, 500)
    win.setBackground("lightgray")

    Text(Point(250, 30), "Digite a aresta do cubo e clique para calcular.").draw(win)
    input_box = Entry(Point(250, 70), 10)
    input_box.draw(win)

    win.getMouse()

    try:
        aresta = float(input_box.getText())
        cubo = Cubo(aresta)

        # Resultados
        Text(Point(250, 130), f"Aresta: {cubo.getAresta():.2f}").draw(win)
        Text(Point(250, 160), f"Área da face: {cubo.faceArea():.2f}").draw(win)
        Text(Point(250, 190), f"Área da superfície: {cubo.surfaceArea():.2f}").draw(win)
        Text(Point(250, 220), f"Volume: {cubo.volume():.2f}").draw(win)

        # Desenhar cubo escalado no centro inferior
        desenhar_cubo(win, Point(250, 370), aresta)

    except ValueError:
        Text(Point(250, 150), "Valor inválido! Digite um número.").draw(win)

    Text(Point(250, 470), "Clique para sair.").draw(win)
    win.getMouse()
    win.close()

main()