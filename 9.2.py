from graphics import *

def converter_para_cinza(imagem):
    largura = imagem.getWidth()
    altura = imagem.getHeight()

    for y in range(altura):
        for x in range(largura):
            r, g, b = imagem.getPixel(x, y)
            brilho = int(round(0.299 * r + 0.587 * g + 0.114 * b))
            imagem.setPixel(x, y, color_rgb(brilho, brilho, brilho))
        update()  # Atualiza a imagem na tela após cada linha

def main():
    # Solicita o nome do arquivo de imagem
    nome_arquivo = input("Digite o nome da imagem (ex: exemplo.gif ou imagem.ppm): ")

    # Cria uma imagem a partir do arquivo
    imagem = Image(Point(0, 0), nome_arquivo)
    largura = imagem.getWidth()
    altura = imagem.getHeight()

    # Cria uma janela do mesmo tamanho da imagem
    win = GraphWin("Conversão para Tons de Cinza", largura, altura)
    win.setCoords(0, 0, largura, altura)

    # Move a imagem para o canto superior esquerdo
    imagem.move(largura // 2, altura // 2)
    imagem.draw(win)

    print("Clique na imagem para convertê-la para tons de cinza.")
    win.getMouse()

    # Converte a imagem para tons de cinza
    converter_para_cinza(imagem)

    print("Imagem convertida.")
    nome_saida = input("Digite o nome do novo arquivo para salvar a imagem em tons de cinza (ex: cinza.gif): ")

    # Salva a imagem modificada
    imagem.save(nome_saida)
    print(f"Imagem salva como '{nome_saida}'.")

    print("Clique na imagem para fechar a janela.")
    win.getMouse()
    win.close()

main()