def contar_palavras(frase):
    palavras = frase.split()  # Divide a frase em palavras
    return len(palavras)

# Solicita a entrada do usuário
frase = input("Digite uma frase: ")
numero_palavras = contar_palavras(frase)

print(f"A frase contém {numero_palavras} palavras.")