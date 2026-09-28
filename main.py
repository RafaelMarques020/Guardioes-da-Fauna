import pygame
import sys
from scripts.cenas import Menu, Partida, Quiz, GameOver, Vitoria

# Inicialização
pygame.init()
pygame.display.set_caption("Guardiões da Fauna Brasileira")

TAMANHO_TELA = (700, 500)
tela = pygame.display.set_mode(TAMANHO_TELA)
relogio = pygame.time.Clock()

# Cenas
partida = Partida(tela)
menu = Menu(tela)
quiz = Quiz(tela, partida)
gameover = GameOver(tela, partida)
vitoria = Vitoria(tela, partida)

lista_cenas = {
    "menu": menu,
    "partida": partida,
    "quiz": quiz,
    "gameover": gameover,
    "vitoria": vitoria,
}

cena_atual = "menu"

# Loop principal
rodando = True
while rodando:
    eventos = pygame.event.get()
    for e in eventos:
        if e.type == pygame.QUIT:
            rodando = False

    # Atualiza cena
    if cena_atual == "partida":
        novo_estado = partida.atualizar(eventos)
        if novo_estado == "quiz":
            quiz.iniciar(partida.animal_para_quiz)
            cena_atual = "quiz"
        elif novo_estado == "gameover":
            cena_atual = "gameover"
        elif novo_estado == "vitoria":
            cena_atual = "vitoria"
    elif cena_atual == "quiz":
        novo_estado = quiz.atualizar(eventos)
        if novo_estado == "partida":
            cena_atual = "partida"
        elif novo_estado == "gameover":
            cena_atual = "gameover"
        elif novo_estado == "vitoria":
            cena_atual = "vitoria"
    elif cena_atual == "menu":
        novo_estado = menu.atualizar(eventos)
        if novo_estado == "partida":
            partida.resetar()
            cena_atual = "partida"
        elif novo_estado == "sair":
            rodando = False
    elif cena_atual == "gameover":
        novo_estado = gameover.atualizar(eventos)
        if novo_estado == "menu":
            cena_atual = "menu"
        elif novo_estado == "sair":
            rodando = False
    elif cena_atual == "vitoria":
        novo_estado = vitoria.atualizar(eventos)
        if novo_estado == "menu":
            cena_atual = "menu"
        elif novo_estado == "sair":
            rodando = False

    # Desenha
    if cena_atual == "partida":
        partida.desenhar()
    elif cena_atual == "quiz":
        partida.desenhar()  # fundo da partida
        quiz.desenhar()
    elif cena_atual == "menu":
        menu.desenhar()
    elif cena_atual == "gameover":
        gameover.desenhar()
    elif cena_atual == "vitoria":
        vitoria.desenhar()

    pygame.display.flip()
    relogio.tick(60)

pygame.quit()
sys.exit()