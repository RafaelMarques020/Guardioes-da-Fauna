import pygame
import random

class Animal:
    ESPECIES = {
        "Amazônia": [
            {"nome": "Mico-leão-dourado", "imagem": "assets/mico_leao.png"},
            {"nome": "Peixe-boi", "imagem": "assets/peixe_boi.png"},
        ],
        "Caatinga": [
            {"nome": "Ararinha-azul", "imagem": "assets/ararinha.png"},
            {"nome": "Tatu-bola", "imagem": "assets/tatu.png"},
        ],
        "Cerrado": [
            {"nome": "Lobo-guará", "imagem": "assets/lobo_guara.png"},
            {"nome": "Tamanduá-bandeira", "imagem": "assets/tamandua.png"},
        ],
        "Mata Atlântica": [
            {"nome": "Jacutinga", "imagem": "assets/jacutinga.png"},
            {"nome": "Tucano", "imagem": "tucano.png"},
        ],
        "Pampa": [
            {"nome": "Veado-campeiro", "imagem": "assets/veado.png"},
            {"nome": "Tuco-tuco", "imagem": "assets/tuco_tuco.png"},
        ],
        "Pantanal": [
            {"nome": "Onça-pintada", "imagem": "assets/onca.png"},
            {"nome": "Tuiuiú", "imagem": "assets/tuiuiu.png"},
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
        imagem_original = pygame.image.load(self.info["imagem"]).convert_alpha()
        self.imagem = pygame.transform.scale(imagem_original, self.tamanho)

    def atualizar(self):
        if not self.coletado:
            self.x -= self.velocidade
            self.rect.x = self.x

    def desenhar(self):
        if not self.coletado:
            self.tela.blit(self.imagem, (self.x, self.y))

    def saiu_da_tela(self):
        return self.x + self.tamanho[0] < 0

    def get_rect(self):
        return self.rect