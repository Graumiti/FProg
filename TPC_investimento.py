#convert.py TPC
#programa para soma de juros não compostos
#by: Pedro Gouveia & Miguel Cravo
def invest():
    print('Este programa calcula o valor de um futuro investimento, sem juros compostos.')
    capital = eval(input('Insira o total do capital investido: '))
    intrate = eval(input('Insira a taxa de juro anual do investimento: '))
    anos = eval(input('Quantos anos irá deixar o capital investido? '))
#looping para o a soma dos juros ao capital
    for i in range(anos):
         capital = capital * (1+intrate)
    print('O valor do investimento em', anos ,'anos será de: ', round(capital, 2), 'Euros')

invest()