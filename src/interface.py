import tkinter as tk
from PIL import ImageTk, Image

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

def pagar_passagem():
    dinheiro = float(entry_dinheiro.get())

    if dinheiro > 50:
        resultado.configure(text="Valor inválido. A catraca não aceita notas maiores que R$50,00.")
        return
    

    if opcao.get() == 1:
        valor_passagem = 2.70
    elif opcao.get() == 2:
        valor_passagem = 3.80
    elif opcao.get() == 3:
        valor_passagem = 5.50
    else:
        resultado.configure(text="Opção inválida.")
        return

    if dinheiro < valor_passagem:
        resultado.configure(text="Valor inválido.")
        return
    
    qtd_notas, qtd_moedas = dar_troco(valor_passagem, dinheiro)

    troco_text = "Troco otimizado:\n"
    for i, nota in enumerate([20, 10, 5, 2, 1]):
        if qtd_notas[i] > 0:
            troco_text += f"{qtd_notas[i]} nota(s) de R${nota},00\n"

    for i, moeda in enumerate([50, 25, 10, 5, 1]):
        if qtd_moedas[i] > 0:
            troco_text += f"{qtd_moedas[i]} moeda(s) de ¢{moeda:.1f}\n"

    resultado.configure(text=troco_text)

# Cria a janela da interface
janela = tk.Tk()
janela.title("Catraca de Ônibus")

# Carrega a imagem de fundo
imagem = Image.open("bus.jpeg")
imagem = imagem.resize((800, 800), Image.ANTIALIAS)  # Ajusta o tamanho da imagem
imagem_de_fundo = ImageTk.PhotoImage(imagem)

# Cria um Label com a imagem de fundo
label_imagem = tk.Label(janela, image=imagem_de_fundo)
label_imagem.place(x=0, y=0, relwidth=1, relheight=1)  # Posiciona e dimensiona o Label para ocupar toda a janela

# Cria os componentes da interface
label_valor = tk.Label(janela, text="Digite o valor para pagar a passagem (até R$50,00):")
label_valor.pack(anchor="center")

entry_dinheiro = tk.Entry(janela)
entry_dinheiro.pack(anchor="center")

opcao = tk.IntVar()
opcao.set(1)

radio_urbana = tk.Radiobutton(janela, text="Passagem Urbana (R$2.70)", variable=opcao, value=1)
radio_urbana.pack(anchor="center")

radio_metropolitana1 = tk.Radiobutton(janela, text="Passagem Metropolitana 1 (R$3.80)", variable=opcao, value=2)
radio_metropolitana1.pack(anchor="center")

radio_metropolitana2 = tk.Radiobutton(janela, text="Passagem Metropolitana 2 (R$5.50)", variable=opcao, value=3)
radio_metropolitana2.pack(anchor="center")

button_calcular = tk.Button(janela, text="Pagar Passagem", command=pagar_passagem)
button_calcular.pack(anchor="center")

resultado = tk.Label(janela, text="", anchor="center")
resultado.pack(anchor="center")

# Define as dimensões da janela
largura = 300
altura = 300
posicao_x = (janela.winfo_screenwidth() // 2) - (largura // 2)  # Centraliza horizontalmente
posicao_y = (janela.winfo_screenheight() // 2) - (altura // 2)  # Centraliza verticalmente
janela.geometry(f"{largura}x{altura}+{posicao_x}+{posicao_y}")

# Inicia o loop principal da interface
janela.mainloop()
