from graphics import *

class GrupoGrafico:
    def __init__(self, ancora):
        self.ancora = Point(ancora.getX(), ancora.getY())  # Clona o ponto
        self.objetos = [] #aqui serão adicionados todos os componentes gráficos da cara.

    def retornaAncora(self):
        return Point(self.ancora.getX(), self.ancora.getY()) #é como uma "segunda via" do ponto ancora
    #para que mesmo se o ponto for alterado fora da classe, termos garantia que usamos o original...

    def adicionaObjeto(self, objeto):
        self.objetos.append(objeto) #fora da classe, usamo-lo para adicionar todos os objetos feitos...

    def move(self, dx, dy):
        self.ancora.move(dx, dy)
        for objeto in self.objetos:
            objeto.move(dx, dy) #movimento, a partir de dx, dy

    def desenha(self, win):
        for objeto in self.objetos:
            objeto.draw(win) #desenhar

    def apaga(self):
        for objeto in self.objetos:
            objeto.undraw() #apagar

def desenhaCara(grupo):
    # Cabeça
    cabeca = Circle(grupo.retornaAncora(), 40)
    cabeca.setFill("yellow")
    grupo.adicionaObjeto(cabeca)

    # Olho esquerdo
    olhoE = Circle(grupo.retornaAncora().clone(), 5)
    olhoE.move(-15, -10)
    olhoE.setFill("black")
    grupo.adicionaObjeto(olhoE)

    # Olho direito
    olhoD = Circle(grupo.retornaAncora().clone(), 5)
    olhoD.move(15, -10)
    olhoD.setFill("black")
    grupo.adicionaObjeto(olhoD)

    # Boca
    boca = Line(Point(grupo.retornaAncora().getX() - 15, grupo.retornaAncora().getY() + 10),
                Point(grupo.retornaAncora().getX() + 15, grupo.retornaAncora().getY() + 10))
    grupo.adicionaObjeto(boca)

def main():
    win = GraphWin("Grupo Gráfico - Cara", 400, 400)

    ancora = Point(200, 200) #definir a posiçao inicial da ancora que produz a cara
    grupo = GrupoGrafico(ancora) # chamar a classe
    desenhaCara(grupo)
    grupo.desenha(win)

    while True:
        click = win.getMouse()
        novoX = click.getX()
        novoY = click.getY()

        dx = novoX - grupo.retornaAncora().getX() #definir o dx, dy.
        dy = novoY - grupo.retornaAncora().getY()

        grupo.move(dx, dy)

    win.close()

main()