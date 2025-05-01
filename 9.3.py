from graphics import *

def converter_para_cinza(imagem):
    largura = imagem.getWidth()
    altura = imagem.getHeight()

    for y in range(altura):
        for x in range(largura):
            r, g, b = imagem.getPixel(x, y)
            brilho = int(round(0.299 * r + 0.587 * g + 0.114 * b))
            imagem.setPixel(x, y, color_rgb(brilho, brilho, brilho))
        update()

def converter_para_negativo(imagem):
    largura = imagem.getWidth()
    altura = imagem.getHeight()

    for y in range(altura):
        for x in range(largura):
            r, g, b = imagem.getPixel(x, y)
            imagem.setPixel(x, y, color_rgb(255 - r, 255 - g, 255 - b))
        update()

def main():
    nome_arquivo = input("Digite o nome da imagem (ex: exemplo.gif ou imagem.ppm): ")
    imagem = Image(Point(0, 0), nome_arquivo)
    largura = imagem.getWidth()
    altura = imagem.getHeight()

    win = GraphWin("Conversor de Imagem", largura, altura)
    win.setCoords(0, 0, largura, altura)

    imagem.move(largura // 2, altura // 2)
    imagem.draw(win)

    print("Escolha o tipo de conversão:")
    print("1 - Tons de cinza")
    print("2 - Negativo colorido")
    escolha = input("Digite 1 ou 2: ")

    print("Clique na imagem para aplicar a conversão.")
    win.getMouse()

    if escolha == "1":
        converter_para_cinza(imagem)
    elif escolha == "2":
        converter_para_negativo(imagem)
    else:
        print("Opção inválida. Fechando o programa.")
        win.close()
        return

    print("Imagem convertida.")
    nome_saida = input("Digite o nome do novo arquivo para salvar a imagem modificada (ex: alterado.gif): ")
    imagem.save(nome_saida)
    print(f"Imagem salva como '{nome_saida}'.")

    print("Clique na imagem para fechar a janela.")
    win.getMouse()
    win.close()

main()