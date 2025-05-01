from graphics import *

class Cubo:
    def __init__(self, aresta, win, centro, tipo="isometrico"):
        self.aresta = aresta
        self.win = win
        self.centro = centro

        if tipo == "dimetrico":
            self.draw3D()
        else:
            self.draw3I()

    def getAresta(self):
        return self.aresta

    def faceArea(self):
        return self.aresta ** 2

    def surfaceArea(self):
        return 6 * self.faceArea()

    def volume(self):
        return self.aresta ** 3

    def draw3I(self):
        lado = self.aresta
        dx = lado * 0.7  # inclinação 1:1 (isométrica)
        dy = -lado * 0.7
        self._desenhar_cubo(lado, dx, dy)

    def draw3D(self):
        lado = self.aresta
        profundidade = lado * 0.5
        dx = profundidade * 0.6  # inclinação 3:2 (dimétrica)
        dy = -profundidade
        self._desenhar_cubo(lado, dx, dy)

    def _desenhar_cubo(self, lado, dx, dy):
        x, y = self.centro.getX(), self.centro.getY()
        d = lado / 2

        # Face frontal
        p1 = Point(x - d, y + d)
        p2 = Point(x + d, y + d)
        p3 = Point(x + d, y - d)
        p4 = Point(x - d, y - d)

        # Face traseira deslocada
        p5 = Point(p1.getX() + dx, p1.getY() + dy)
        p6 = Point(p2.getX() + dx, p2.getY() + dy)
        p7 = Point(p3.getX() + dx, p3.getY() + dy)
        p8 = Point(p4.getX() + dx, p4.getY() + dy)

        # Frente
        for (a, b) in [(p1, p2), (p2, p3), (p3, p4), (p4, p1)]:
            Line(a, b).draw(self.win)
        # Trás
        for (a, b) in [(p5, p6), (p6, p7), (p7, p8), (p8, p5)]:
            Line(a, b).draw(self.win)
        # Conexões
        for (a, b) in [(p1, p5), (p2, p6), (p3, p7), (p4, p8)]:
            Line(a, b).draw(self.win)

        # Info
        ybase = 50
        for i, text in enumerate([
            f"Aresta: {self.aresta:.2f}",
            f"Área da face: {self.faceArea():.2f}",
            f"Área da superfície: {self.surfaceArea():.2f}",
            f"Volume: {self.volume():.2f}"
        ]):
            Text(Point(300, ybase + i * 20), text).draw(self.win)

def main():
    win = GraphWin("Cubo Isométrico vs Dimétrico", 800, 500)
    win.setBackground("white")

    Text(Point(400, 30), "Digite a aresta do cubo e clique.").draw(win)
    input_box = Entry(Point(400, 60), 10)
    input_box.draw(win)

    win.getMouse()

    try:
        aresta = float(input_box.getText())

        # Título das vistas
        Text(Point(200, 100), "Vista Isométrica").draw(win)
        Text(Point(600, 100), "Vista Dimétrica").draw(win)

        # Criar cubos com centros separados
        Cubo(aresta, win, Point(200, 300), tipo="isometrico")
        Cubo(aresta, win, Point(600, 300), tipo="dimetrico")

    except ValueError:
        Text(Point(400, 150), "Valor inválido!").draw(win)

    Text(Point(400, 470), "Clique para sair.").draw(win)
    win.getMouse()
    win.close()

main()