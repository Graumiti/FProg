coffee = eval(input('Quantos quilos de café quer encomendar: '))

coffee_kg = 2.5

coffee_cost = coffee * coffee_kg
custo_envio = 0.86 * coffee + 1.50

custo_no_iva = custo_envio + coffee_cost
iva = custo_no_iva * 0.23

custo_w_iva = iva + custo_no_iva

print(f'Detalhes da encomenda:')
print('-' * 30)
print(f'Custo do café: {coffee_cost:.2f} euros')
print('-' * 30)
print(f'Detalhes do iva: {iva:.2f} euros')
print('-' * 30)
print(f'Detalhes do envio: {custo_envio:.2f} euros')
print('-' * 30)
print(f'Custo total: {custo_w_iva:.2f} euros')
print('-' * 30)
