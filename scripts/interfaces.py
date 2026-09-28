import pygame

class Texto:
    def __init__(self, tela, texto, x, y, cor=(255, 255, 255), tamanho=32):
        self.tela = tela
        self.texto = texto
        self.posicao = (x, y)
        self.cor = cor
        self.tamanho = tamanho
        self.fonte = pygame.font.SysFont("Arial", self.tamanho)
        self.imagem = self.fonte.render(self.texto, True, self.cor)

    def desenhar(self):
        self.tela.blit(self.imagem, self.posicao)

    def atualizar(self, novo_texto):
        self.texto = novo_texto
        self.imagem = self.fonte.render(self.texto, True, self.cor)


class Botao:
    def __init__(self, tela, texto, x, y, largura, altura, cor_fundo=(34, 139, 34), cor_texto=(255, 255, 255), tamanho_fonte=28):
        self.tela = tela
        self.texto = texto
        self.rect = pygame.Rect(x, y, largura, altura)
        self.cor_fundo = cor_fundo
        self.cor_texto = cor_texto
        self.fonte = pygame.font.SysFont("Arial", tamanho_fonte)
        self.imagem_texto = self.fonte.render(texto, True, cor_texto)

    def desenhar(self):
        pygame.draw.rect(self.tela, self.cor_fundo, self.rect, border_radius=8)
        pygame.draw.rect(self.tela, (255, 255, 255), self.rect, 2, border_radius=8)
        texto_rect = self.imagem_texto.get_rect(center=self.rect.center)
        self.tela.blit(self.imagem_texto, texto_rect)

    def foi_clicado(self, pos_mouse):
        return self.rect.collidepoint(pos_mouse)