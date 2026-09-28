import pygame

class Jogador:
    def __init__(self, tela, x, y):
        self.tela = tela
        self.posicao = [x, y]
        self.tamanho = (50, 30)
        self.velocidade = 6
        self.vidas = 3
        imagem_original = pygame.image.load("assets/drone.png").convert_alpha()
        self.imagem = pygame.transform.scale(imagem_original, self.tamanho)
        self.rect = self.imagem.get_rect()
        self.rect.topleft = (self.posicao[0], self.posicao[1])

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
         self.tela.blit(self.imagem, self.rect)

    def get_rect(self):
        return self.rect

    def perder_vida(self):
        self.vidas -= 1
        return self.vidas <= 0