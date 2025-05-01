from graphics import *
import math

# Classe Esfera, o graphics.py nao consegue desenhar em 3d, entao simulamos um circulo e as suas propriedades no plano R3.
class Esfera:
    def __init__(self, raio):
        self.raio = raio

    def getRadius(self):
        return self.raio

    def surfaceArea(self):
        return 4 * math.pi * self.raio ** 2

    def volume(self):
        return (4 / 3) * math.pi * self.raio ** 3


def main():
    # Criar janela
    win = GraphWin("Calculadora de Esfera", 500, 400)
    win.setBackground("lightblue")

    # Instruções
    instr = Text(Point(250, 30), "Digite o raio da esfera e clique em qualquer lugar.")
    instr.draw(win)

    # Caixa de entrada para o raio
    input_box = Entry(Point(250, 70), 10)
    input_box.draw(win)

    # Esperar o clique do usuário
    win.getMouse()

    try:
        raio = float(input_box.getText())
        esfera = Esfera(raio)

        # Desenha a "esfera" como círculo no centro inferior
        center = Point(250, 280)
        escalar = 10  # fator de escala para caber na janela
        raio_pixel = raio * escalar

        if raio_pixel > 100:
            raio_pixel = 100  # limitar o tamanho visual, para não ultrapassar da janela...

        esfera_circulo = Circle(center, raio_pixel)
        esfera_circulo.setFill("white")
        esfera_circulo.setOutline("black")
        esfera_circulo.draw(win)

        # Textos de resultado
        Text(Point(250, 130), f"Raio: {esfera.getRadius():.2f}").draw(win)
        Text(Point(250, 160), f"Área da superfície: {esfera.surfaceArea():.2f}").draw(win)
        Text(Point(250, 190), f"Volume: {esfera.volume():.2f}").draw(win)

    except ValueError:
        Text(Point(250, 150), "Por favor, digite um número válido.").draw(win)

    # Mensagem final
    Text(Point(250, 360), "Clique para sair.").draw(win)
    win.getMouse()
    win.close()

main()