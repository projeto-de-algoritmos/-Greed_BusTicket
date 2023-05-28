
dinheiro = float(input("Digite o valor_passagem do troco (até R$50,00): "))
valor_passagem = 2.7  # Valor da passagem

def dar_troco(valor_passagem, dinheiro):
    troco = dinheiro - valor_passagem  # Calcula o valor_passagem do troco subtraindo do valor_passagem máximo permitido (R$50,00)
    print(f"Troco calculado: R${troco:.2f}")
    notas = [20, 10, 5, 2, 1]
    moedas = [0.5, 0.25, 0.10, 0.05, 0.01]
    qtd_notas = [0] * len(notas)
    qtd_moedas = [0] * len(moedas)

    for i, nota in enumerate(notas):
        qtd_notas[i] = troco // nota
        troco %= nota

    for i, moeda in enumerate(moedas):
        qtd_moedas[i] = troco // moeda
        troco %= moeda

    return qtd_notas, qtd_moedas


if dinheiro > 50:
    print("Valor inválido. O troco não pode ser maior que R$50,00.")
else:
    qtd_notas, qtd_moedas = dar_troco(valor_passagem, dinheiro)

    print("Troco otimizado:")
    for i, nota in enumerate([20, 10, 5, 2, 1]):
        if qtd_notas[i] > 0:
            print(f"{qtd_notas[i]} nota(s) de R${nota},00")

    for i, moeda in enumerate([50, 25, 10, 5, 1]):
        if qtd_moedas[i] > 0:
            print(f"{qtd_moedas[i]} moeda(s) de ¢{moeda}")
