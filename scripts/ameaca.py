import pygame
import random

class Ameaca:
    TIPOS = [
        {"nome": "Motosserra", "imagem": "assets/motosserra.png"},
        {"nome": "Queimada", "imagem": "assets/queimada.png"},
        {"nome": "Rede de Caça", "imagem": "assets/rede.png"},
        {"nome": "Armadilha", "imagem": "assets/armadilha.png"},
        {"nome": "Poluição", "imagem": "assets/poluicao.png"},
    ]

    def __init__(self, tela, velocidade=4):
        self.tela = tela
        self.tipo = random.choice(self.TIPOS)
        self.tamanho = (40, 40)
        self.x = self.tela.get_width() + 10
        self.y = random.randint(20, self.tela.get_height() - 60)
        self.velocidade = velocidade
        imagem_original = pygame.image.load(self.tipo["imagem"]).convert_alpha()
        self.imagem = pygame.transform.scale(imagem_original, self.tamanho)
        
        self.rect = pygame.Rect(self.x, self.y, self.tamanho[0], self.tamanho[1])

    def atualizar(self):
        self.x -= self.velocidade
        self.rect.x = self.x

    def desenhar(self):
        self.tela.blit(self.imagem, (self.x, self.y))

    def saiu_da_tela(self):
        return self.x + self.tamanho[0] < 0

    def get_rect(self):
        return self.rect