import pygame
from pygame.locals import *

# Configurações da janela
largura_janela = 400
altura_janela = 200

# Cores
cor_branca = (255, 255, 255)
cor_verde = (0, 255, 0)
cor_vermelha = (255, 0, 0)

# Inicialização do Pygame
pygame.init()
janela = pygame.display.set_mode((largura_janela, altura_janela))
pygame.display.set_caption("Catraca")

# Fonte
fonte = pygame.font.Font(None, 36)

# Função para exibir a mensagem na janela
def exibir_mensagem(mensagem, cor):
    janela.fill(cor_branca)
    texto = fonte.render(mensagem, True, cor)
    posicao_texto = texto.get_rect(center=(largura_janela // 2, altura_janela // 2))
    janela.blit(texto, posicao_texto)
    pygame.display.flip()

# Função para calcular o troco
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

    return qtd_notas, qtd_moedas

# Exibir a janela inicial
exibir_mensagem("Digite o valor para pagar a passagem (até R$50,00):", cor_branca)

# Variáveis de controle
valor_passagem = 0.0
dinheiro = 0.0
esperando_valor_passagem = True
esperando_dinheiro = False

# Loop principal do jogo
executando = True
while executando:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            executando = False
        elif evento.type == KEYDOWN:
            if esperando_valor_passagem:
                if evento.key == K_KP1 or evento.key == K_1:
                    valor_passagem = 2.70
                    esperando_valor_passagem = False
                    esperando_dinheiro = True
                elif evento.key == K_KP2 or evento.key == K_2:
                    valor_passagem = 3.80
                    esperando_valor_passagem = False
                    esperando_dinheiro = True
                elif evento.key == K_KP3 or evento.key == K_3:
                    valor_passagem = 5.50
                    esperando_valor_passagem = False
                    esperando_dinheiro = True
            elif esperando_dinheiro:
                if evento.key == K_BACKSPACE:
                    dinheiro = 0.0
                elif evento.key == K_RETURN:
                    if dinheiro > 50:
                        exibir_mensagem("Valor inválido. A catraca não aceita notas maiores que R$50,00.", cor_vermelha)
                    elif dinheiro < 0:
                        exibir_mensagem("Valor inválido.", cor_vermelha)
                    else:
                        qtd_notas, qtd_moedas = dar_troco(valor_passagem, dinheiro)
                        # Exibir o troco otimizado na janela
                        mensagem_troco = "Troco otimizado:\n"
                        for i, nota in enumerate([20, 10, 5, 2, 1]):
                            if qtd_notas[i] > 0:
                                mensagem_troco += f"{qtd_notas[i]} nota(s) de R${nota},00\n"

                        for i, moeda in enumerate([0.50, 0.25, 0.10, 0.05, 0.01]):
                            if qtd_moedas[i] > 0:
                                mensagem_troco += f"{qtd_moedas[i]} moeda(s) de R${moeda:.2f}\n"

                        exibir_mensagem(mensagem_troco, cor_verde)
                        pygame.display.flip()

