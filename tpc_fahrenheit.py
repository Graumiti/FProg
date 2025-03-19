#convert.py TPC
#programa para converter celsius em fahrenheit
#by: Pedro Gouveia & Miguel Cravo

#Definir funçao da relação ºC - ºF
def Relacao_CF(celsius):
    return (celsius * 9/5) + 32

# Cabeçalho da tabela
print(f"{'Celsius (°C)':<15} {'Fahrenheit (°F)':<15}")
# f antes do texto formata o cabeçalho da tabela. o sinal < ajuda na formataçao da tabela(dá 15 caracteres de espaço)
print("-" * 30)

# Loop para gerar a tabela de 10 em 10. Como a variavel i começa no zero adicionamos mais 1 unidade
for i in range(0, 101, 10):
    f = Relacao_CF(i)
    print(f"{i:<15} {f:<15.1f}")
# .1f para mostrar 1 casa decimal. Mesma formatação que line.10
print('-' * 30)