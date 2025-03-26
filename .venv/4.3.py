from graphics import *


def main():
    # Perguntar ao usuário o tamanho da janela
    tamanho = input("Escolha o tamanho da janela (grande/pequena): ").strip().lower()

    if tamanho == "grande":
        largura, altura = 800, 800  # Janela grande
    else:
        largura, altura = 400, 400  # Janela pequena por padrão

    # Criar a janela gráfica
    win = GraphWin("Desenhar Retângulo", largura, altura)
    win.setCoords(0, 0, 10, 10)  # Define o sistema de coordenadas para 10x10 metros

    # Mensagem inicial
    message = Text(Point(5, 9), "Clique em dois pontos para desenhar um retângulo")
    message.draw(win)

    # Obter dois pontos do usuário
    point1 = win.getMouse()
    point2 = win.getMouse()
    x1, y1 = point1.getX(), point1.getY()
    x2, y2 = point2.getX(), point2.getY()

    # Calcular área e perímetro
    area = abs((x2 - x1) * (y2 - y1))
    perimeter = 2 * (abs(x2 - x1) + abs(y2 - y1))

    # Desenhar retângulo
    r = Rectangle(point1, point2)
    r.draw(win)

    # Exibir área e perímetro
    area_text = Text(Point(5, 2), f"Área: {round(area, 2)} m²")
    area_text.draw(win)
    perimeter_text = Text(Point(5, 1), f"Perímetro: {round(perimeter, 2)} m")
    perimeter_text.draw(win)

    # Esperar um clique antes de fechar
    win.getMouse()
    win.close()


main()
