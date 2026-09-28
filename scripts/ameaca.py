import pygame
import random

class Ameaca:
    TIPOS = [
        {"nome": "Motosserra", "cor": (139, 69, 19)},
        {"nome": "Queimada", "cor": (255, 69, 0)},
        {"nome": "Rede de Caça", "cor": (70, 70, 70)},
        {"nome": "Armadilha", "cor": (105, 105, 105)},
        {"nome": "Poluição", "cor": (128, 0, 128)},
    ]

    def __init__(self, tela, velocidade=4):
        self.tela = tela
        self.tipo = random.choice(self.TIPOS)
        self.tamanho = (40, 40)
        self.x = self.tela.get_width() + 10
        self.y = random.randint(20, self.tela.get_height() - 60)
        self.velocidade = velocidade
        self.rect = pygame.Rect(self.x, self.y, self.tamanho[0], self.tamanho[1])

    def atualizar(self):
        self.x -= self.velocidade
        self.rect.x = self.x

    def desenhar(self):
        pygame.draw.rect(self.tela, self.tipo["cor"], self.rect, border_radius=6)
        fonte = pygame.font.SysFont("Arial", 10)
        texto = fonte.render(self.tipo["nome"][:6], True, (255, 255, 255))
        self.tela.blit(texto, (self.x + 2, self.y + 12))

    def saiu_da_tela(self):
        return self.x + self.tamanho[0] < 0

    def get_rect(self):
        return self.rect