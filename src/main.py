dinheiro = float(input("Digite o valor para pagar a passagem (até R$50,00): "))

def dar_troco(valor_passagem, dinheiro):
    troco = dinheiro - valor_passagem
    notas = [20, 10, 5, 2, 1]
    moedas = [0.5, 0.25, 0.10, 0.05, 0.01]
    qtd_notas = [0] * len(notas)
    qtd_moedas = [0] * len(moedas)

    for i, nota in enumerate(notas):
        qtd_notas[i] = troco // nota
        troco %= nota

    for i, moeda in enumerate(moedas):
        qtd_moedas[i] = int(troco // moeda)
        troco = round(troco % moeda, 2)  # Arredondar o troco para evitar erro no cálculo

    print(f"Troco calculado: R${dinheiro - valor_passagem:.2f}")

    return qtd_notas, qtd_moedas



print("Escolha o tipo de passagem:")
print("1. Passagem Urbana (R$2.70)")
print("2. Passagem Metropolitana 1 (R$3.80)")
print("3. Passagem Metropolitana 2 (R$5.50)")

opcao = int(input("Digite o número da opção desejada: "))

if opcao == 1:
    valor_passagem = 2.70
elif opcao == 2:
    valor_passagem = 3.80
elif opcao == 3:
    valor_passagem = 5.50
else:
    print("Opção inválida.")
    exit()

if (dinheiro > 50):
    print("Valor inválido. A catraca não aceita notas maiores que R$50,00.")
elif (dinheiro < 0):
    print("Valor inválido.")
else:
    qtd_notas, qtd_moedas = dar_troco(valor_passagem, dinheiro)

    print("Troco otimizado:")
    for i, nota in enumerate([20, 10, 5, 2, 1]):
        if qtd_notas[i] > 0:
            print(f"{qtd_notas[i]} nota(s) de R${nota},00")

    for i, moeda in enumerate([50, 25, 10, 5, 1]):
        if qtd_moedas[i] > 0:
            print(f"{qtd_moedas[i]} moeda(s) de ¢{moeda:.1f}")
