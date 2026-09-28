import pygame

class Jogador:
    def __init__(self, tela, x, y):
        self.tela = tela
        self.posicao = [x, y]
        self.tamanho = (50, 30)
        self.velocidade = 6
        self.vidas = 3
        self.rect = pygame.Rect(self.posicao[0], self.posicao[1], self.tamanho[0], self.tamanho[1])
        self.cor_corpo = (46, 139, 87)
        self.cor_janela = (135, 206, 235)

    def atualizar(self):
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_UP] or teclas[pygame.K_w]:
            self.posicao[1] -= self.velocidade
        if teclas[pygame.K_DOWN] or teclas[pygame.K_s]:
            self.posicao[1] += self.velocidade

        altura = self.tela.get_height()
        if self.posicao[1] < 0:
            self.posicao[1] = 0
        if self.posicao[1] > altura - self.tamanho[1]:
            self.posicao[1] = altura - self.tamanho[1]

        self.rect.topleft = (self.posicao[0], self.posicao[1])

    def desenhar(self):
        pygame.draw.ellipse(self.tela, self.cor_corpo, self.rect)
        janela = pygame.Rect(self.posicao[0] + 10, self.posicao[1] + 5, 20, 15)
        pygame.draw.ellipse(self.tela, self.cor_janela, janela)
        pygame.draw.rect(self.tela, (0, 100, 0), (self.posicao[0] - 5, self.posicao[1] + 8, 10, 14))
        pygame.draw.rect(self.tela, (0, 100, 0), (self.posicao[0] + self.tamanho[0] - 5, self.posicao[1] + 8, 10, 14))

    def get_rect(self):
        return self.rect

    def perder_vida(self):
        self.vidas -= 1
        return self.vidas <= 0