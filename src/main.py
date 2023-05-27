def dar_troco(valor):
    troco = dinheiro - valor  # Calcula o valor do troco subtraindo do valor máximo permitido (R$50,00)
    notas = [20, 10, 5, 2, 1]
    moedas = [0.5, 0.25, 0.10, 0.05]
    qtd_notas = [0] * len(notas)
    qtd_moedas = [0] * len(moedas)

    for i, nota in enumerate(notas):
        qtd_notas[i] = troco // nota
        troco %= nota

    for i, moeda in enumerate(moedas):
        qtd_moedas[i] = troco // moeda
        troco %= moeda

    return qtd_notas, qtd_moedas

dinheiro = float(input("Digite o valor do troco (até R$50,00): "))
valor = 3.80  # Valor da passagem

if valor > 50:
    print("Valor inválido. O troco não pode ser maior que R$50,00.")
else:
    qtd_notas, qtd_moedas = dar_troco(valor)

    print("Troco otimizado:")
    for i, nota in enumerate([20, 10, 5, 2, 1]):
        if qtd_notas[i] > 0:
            print(f"{qtd_notas[i]} nota(s) de R${nota},00")

    for i, moeda in enumerate([0.50, 0.25, 0.10, 0.05]):
        if qtd_moedas[i] > 0:
            print(f"{qtd_moedas[i]} moeda(s) de ¢{moeda}")
