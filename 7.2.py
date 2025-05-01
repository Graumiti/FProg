def ler_dados_teclado():
    trajetos = []

    odometro_inicial = float(input("Digite o valor inicial do odómetro (km): "))

    print("Digite os dados de cada trajeto no formato: <odometro_final> <litros_consumidos>")
    print("Pressione ENTER sem digitar nada para terminar.")

    while True:
        entrada = input("Trajeto: ")
        if entrada.strip() == "":
            break
        try:
            odometro_final, litros = map(float, entrada.strip().split())
            trajetos.append((odometro_final, litros))
        except ValueError:
            print("Entrada inválida. Use o formato: <odometro_final> <litros_consumidos>")

    return odometro_inicial, trajetos


def calcular_consumo(odometro_inicial, trajetos):
    total_km = 0
    total_litros = 0

    print("\nConsumo por trajeto:")
    for odometro_final, litros in trajetos:
        distancia = odometro_final - odometro_inicial
        if distancia <= 0:
            print("  Trajeto ignorado (distância inválida ou negativa).")
            continue
        consumo = (litros / distancia) * 100
        print(f"  Distância: {distancia:.1f} km - Combustível: {litros:.1f} L - Consumo: {consumo:.2f} L/100km")

        total_km += distancia
        total_litros += litros
        odometro_inicial = odometro_final

    if total_km > 0:
        consumo_total = (total_litros / total_km) * 100
        print(f"\nConsumo médio total: {consumo_total:.2f} L/100km")
    else:
        print("Não foi possível calcular o consumo total (distância total zero).")


def main():
    odometro_inicial, trajetos = ler_dados_teclado()
    calcular_consumo(odometro_inicial, trajetos)


if __name__ == "__main__":
    main()