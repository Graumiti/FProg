from graphics import *

def media(lista):
    return sum(lista) / len(lista)

def regressao_linear(xs, ys):
    n = len(xs)
    media_x = media(xs)
    media_y = media(ys)

    soma_xy = sum(x*y for x, y in zip(xs, ys))
    soma_x2 = sum(x**2 for x in xs)

    numerador = soma_xy - n * media_x * media_y
    denominador = soma_x2 - n * media_x**2

    m = numerador / denominador if denominador != 0 else 0
    return media_x, media_y, m

def main():
    win = GraphWin("Regressão Linear", 600, 600)
    win.setCoords(0, 0, 100, 100)

    # Botão "Concluído"
    botao = Rectangle(Point(0, 0), Point(15, 8))
    botao.setFill("lightgray")
    botao.draw(win)
    txt = Text(Point(7.5, 4), "Concluído")
    txt.draw(win)

    # Contador de pontos
    contador = Text(Point(90, 95), "Pontos: 0")
    contador.setSize(10)
    contador.draw(win)

    pontos = []
    xs, ys = [], []

    while True:
        click = win.getMouse()
        x, y = click.getX(), click.getY()

        # Verifica o clique no botão "Concluído"
        if 0 <= x <= 15 and 0 <= y <= 8:
            break

        # Armazena e desenha ponto
        Circle(Point(x, y), 1).draw(win)
        xs.append(x)
        ys.append(y)
        pontos.append((x, y))

        contador.setText(f"Pontos: {len(pontos)}")

    if len(pontos) < 2:
        aviso = Text(Point(50, 50), "Insira pelo menos 2 pontos!")
        aviso.setFill("red")
        aviso.setSize(14)
        aviso.draw(win)
    else:
        media_x, media_y, m = regressao_linear(xs, ys)

        # Cálculo da linha nos extremos da janela
        x_min = 0
        x_max = 100
        y_min = media_y + m * (x_min - media_x)
        y_max = media_y + m * (x_max - media_x)

        # Desenha a linha de regressão
        linha = Line(Point(x_min, y_min), Point(x_max, y_max))
        linha.setWidth(2)
        linha.setOutline("red")
        linha.draw(win)

        # Mostra equação
        eq_texto = Text(Point(50, 95), f"y = {media_y:.2f} + {m:.2f}(x - {media_x:.2f})")
        eq_texto.setTextColor("red")
        eq_texto.setSize(12)
        eq_texto.draw(win)

    # Aguarda clique final para fechar
    win.getMouse()
    win.close()

main()