import pygame
import random

class Animal:
    ESPECIES = {
        "Amazônia": [
            {"nome": "Mico-leão-dourado", "cor": (255, 215, 0)},
            {"nome": "Peixe-boi", "cor": (70, 130, 180)},
        ],
        "Caatinga": [
            {"nome": "Ararinha-azul", "cor": (0, 100, 255)},
            {"nome": "Tatu-bola", "cor": (160, 82, 45)},
        ],
        "Cerrado": [
            {"nome": "Lobo-guará", "cor": (210, 105, 30)},
            {"nome": "Tamanduá-bandeira", "cor": (139, 90, 43)},
        ],
        "Mata Atlântica": [
            {"nome": "Jacutinga", "cor": (0, 100, 0)},
            {"nome": "Mico-leão-preto", "cor": (40, 40, 40)},
        ],
        "Pampa": [
            {"nome": "Saci-da-praia", "cor": (255, 165, 0)},
            {"nome": "Tuco-tuco", "cor": (139, 69, 19)},
        ],
        "Pantanal": [
            {"nome": "Onça-pintada", "cor": (255, 140, 0)},
            {"nome": "Tuiuiú", "cor": (255, 255, 255)},
        ],
    }

    def __init__(self, tela, bioma="Amazônia", velocidade=4):
        self.tela = tela
        especies = self.ESPECIES.get(bioma, self.ESPECIES["Amazônia"])
        self.info = random.choice(especies)
        self.tamanho = (45, 35)
        self.x = self.tela.get_width() + 10
        self.y = random.randint(20, self.tela.get_height() - 60)
        self.velocidade = velocidade
        self.rect = pygame.Rect(self.x, self.y, self.tamanho[0], self.tamanho[1])
        self.coletado = False

    def atualizar(self):
        if not self.coletado:
            self.x -= self.velocidade
            self.rect.x = self.x

    def desenhar(self):
        if not self.coletado:
            pygame.draw.ellipse(self.tela, self.info["cor"], self.rect)
            pygame.draw.circle(self.tela, (0, 0, 0), (self.x + 30, self.y + 12), 4)
            pygame.draw.circle(self.tela, (255, 255, 255), (self.x + 31, self.y + 11), 2)

    def saiu_da_tela(self):
        return self.x + self.tamanho[0] < 0

    def get_rect(self):
        return self.rect