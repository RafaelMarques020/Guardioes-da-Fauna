import pygame
import random
from scripts.jogador import Jogador
from scripts.ameaca import Ameaca
from scripts.animal import Animal
from scripts.interfaces import Texto, Botao

PERGUNTAS = [
    {
        "pergunta": "O Mico-leão-dourado habita principalmente qual bioma?",
        "opcoes": ["Amazônia", "Caatinga", "Pampa"],
        "correta": 0
    },
    {
        "pergunta": "Qual animal é símbolo do Pantanal?",
        "opcoes": ["Tuiuiú", "Lobo-guará", "Tatu-bola"],
        "correta": 0
    },
    {
        "pergunta": "A Ararinha-azul é nativa de qual região?",
        "opcoes": ["Cerrado", "Caatinga", "Mata Atlântica"],
        "correta": 1
    },
    {
        "pergunta": "O que mais ameaça a fauna brasileira?",
        "opcoes": ["Desmatamento e caça", "Chuva excessiva", "Frio extremo"],
        "correta": 0
    },
    {
        "pergunta": "O Lobo-guará é típico de qual bioma?",
        "opcoes": ["Amazônia", "Cerrado", "Pantanal"],
        "correta": 1
    },
    {
        "pergunta": "Qual é o maior predador terrestre do Brasil?",
        "opcoes": ["Onça-pintada", "Tatu-bola", "Peixe-boi"],
        "correta": 0
    },
    {
        "pergunta": "O Peixe-boi vive em ambientes:",
        "opcoes": ["Aquáticos da Amazônia", "Secos da Caatinga", "Campos do Pampa"],
        "correta": 0
    },
    {
        "pergunta": "A Mata Atlântica sofre com:",
        "opcoes": ["Fragmentação de habitat", "Neve", "Desertos"],
        "correta": 0
    },
]


class Menu:
    def __init__(self, tela):
        self.tela = tela
        self.estado = "menu"
        self.titulo = Texto(tela, "GUARDIÕES DA FAUNA", 120, 80, (34, 139, 34), 42)
        self.subtitulo = Texto(tela, "BRASILEIRA", 220, 130, (0, 100, 0), 36)
        self.instrucao = Texto(tela, "Use SETAS ou W/S para mover a nave", 140, 220, (200, 200, 200), 22)
        self.instrucao2 = Texto(tela, "Resgate animais e responda os quizzes!", 130, 250, (200, 200, 200), 22)
        self.botao_jogar = Botao(tela, "JOGAR", 250, 320, 180, 50, (34, 139, 34))
        self.botao_sair = Botao(tela, "SAIR", 250, 390, 180, 50, (178, 34, 34))

    def atualizar(self, eventos):
        self.estado = "menu"
        for e in eventos:
            if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                if self.botao_jogar.foi_clicado(e.pos):
                    self.estado = "partida"
                elif self.botao_sair.foi_clicado(e.pos):
                    self.estado = "sair"
        return self.estado

    def desenhar(self):
        self.tela.fill((20, 50, 30))
        pontos = [(50, 40), (120, 90), (600, 50), (650, 150), (30, 300), (680, 400), (100, 450), (550, 420)]
        for p in pontos:
            pygame.draw.circle(self.tela, (0, 80, 0), p, 4)
        self.titulo.desenhar()
        self.subtitulo.desenhar()
        self.instrucao.desenhar()
        self.instrucao2.desenhar()
        self.botao_jogar.desenhar()
        self.botao_sair.desenhar()


class Partida:
    def __init__(self, tela):
        self.tela = tela
        self.estado = "partida"
        self.jogador = Jogador(tela, 80, 220)
        self.ameacas = []
        self.animais = []
        self.pontuacao = 0
        self.resgates = 0
        self.meta_resgates = 3
        self.bioma_atual = "Amazônia"
        self.tempo_spawn = 0
        self.intervalo_spawn = 90
        self.velocidade_scroll = 4
        self.erros_quiz_seguidos = 0
        self.animal_para_quiz = None
        self.fonte_hud = pygame.font.SysFont("Arial", 22)
        self.biomas = ["Amazônia", "Caatinga", "Cerrado", "Mata Atlântica", "Pampa", "Pantanal"]
        self.indice_bioma = 0

    def resetar(self):
        self.jogador = Jogador(self.tela, 80, 220)
        self.ameacas = []
        self.animais = []
        self.pontuacao = 0
        self.resgates = 0
        self.tempo_spawn = 0
        self.erros_quiz_seguidos = 0
        self.animal_para_quiz = None
        self.indice_bioma = 0
        self.bioma_atual = self.biomas[0]
        self.velocidade_scroll = 4
        self.intervalo_spawn = 90

    def spawnar(self):
        if random.random() < 0.6:
            self.ameacas.append(Ameaca(self.tela, self.velocidade_scroll))
        else:
            self.animais.append(Animal(self.tela, self.bioma_atual, self.velocidade_scroll))

    def atualizar(self, eventos):
        self.estado = "partida"

        self.tempo_spawn += 1
        if self.tempo_spawn >= self.intervalo_spawn:
            self.spawnar()
            self.tempo_spawn = 0

        self.jogador.atualizar()

        for a in self.ameacas[:]:
            a.atualizar()
            if a.saiu_da_tela():
                self.ameacas.remove(a)
            elif self.jogador.get_rect().colliderect(a.get_rect()):
                self.ameacas.remove(a)
                if self.jogador.perder_vida():
                    self.estado = "gameover"

        for an in self.animais[:]:
            an.atualizar()
            if an.saiu_da_tela():
                self.animais.remove(an)
            elif self.jogador.get_rect().colliderect(an.get_rect()):
                an.coletado = True
                self.animais.remove(an)
                self.animal_para_quiz = an
                self.estado = "quiz"

        return self.estado

    def desenhar(self):
        cores_fundo = {
            "Amazônia": (10, 60, 20),
            "Caatinga": (80, 60, 30),
            "Cerrado": (90, 80, 40),
            "Mata Atlântica": (20, 50, 30),
            "Pampa": (60, 90, 50),
            "Pantanal": (30, 70, 90),
        }
        self.tela.fill(cores_fundo.get(self.bioma_atual, (10, 60, 20)))

        for i in range(0, 700, 40):
            pygame.draw.line(self.tela, (0, 40, 0), (i, 0), (i, 500), 1)

        self.jogador.desenhar()
        for a in self.ameacas:
            a.desenhar()
        for an in self.animais:
            an.desenhar()

        vida_txt = self.fonte_hud.render(f"Vidas: {self.jogador.vidas}", True, (255, 100, 100))
        pontos_txt = self.fonte_hud.render(f"Pontos: {self.pontuacao}", True, (255, 255, 100))
        resgate_txt = self.fonte_hud.render(f"Resgates: {self.resgates}/{self.meta_resgates}", True, (100, 255, 100))
        bioma_txt = self.fonte_hud.render(f"Bioma: {self.bioma_atual}", True, (200, 200, 255))

        self.tela.blit(vida_txt, (10, 10))
        self.tela.blit(pontos_txt, (10, 40))
        self.tela.blit(resgate_txt, (10, 70))
        self.tela.blit(bioma_txt, (450, 10))

    def avancar_bioma(self):
        self.indice_bioma += 1
        if self.indice_bioma >= len(self.biomas):
            self.estado = "vitoria"
            return
        self.bioma_atual = self.biomas[self.indice_bioma]
        self.resgates = 0
        self.velocidade_scroll += 1
        self.intervalo_spawn = max(50, self.intervalo_spawn - 10)
        self.ameacas.clear()
        self.animais.clear()


class Quiz:
    def __init__(self, tela, partida):
        self.tela = tela
        self.partida = partida
        self.estado = "quiz"
        self.pergunta_atual = None
        self.botoes = []
        self.resultado = None
        self.tempo_resultado = 0
        self.fonte_pergunta = pygame.font.SysFont("Arial", 24)
        self.fonte_info = pygame.font.SysFont("Arial", 20)

    def iniciar(self, animal):
        self.pergunta_atual = random.choice(PERGUNTAS)
        self.resultado = None
        self.tempo_resultado = 0
        self.botoes = []
        y = 260
        for i, opcao in enumerate(self.pergunta_atual["opcoes"]):
            self.botoes.append(Botao(self.tela, opcao, 150, y, 400, 45, (50, 50, 120)))
            y += 60

    def atualizar(self, eventos):
        self.estado = "quiz"

        if self.resultado is not None:
            self.tempo_resultado += 1
            if self.tempo_resultado > 90:
                if self.resultado == "certo":
                    self.partida.pontuacao += 100
                    self.partida.resgates += 1
                    self.partida.erros_quiz_seguidos = 0
                    if self.partida.resgates >= self.partida.meta_resgates:
                        self.partida.avancar_bioma()
                        if self.partida.estado == "vitoria":
                            return "vitoria"
                else:
                    self.partida.erros_quiz_seguidos += 1
                    if self.partida.erros_quiz_seguidos >= 3:
                        return "gameover"
                return "partida"
            return "quiz"

        for e in eventos:
            if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                for i, botao in enumerate(self.botoes):
                    if botao.foi_clicado(e.pos):
                        if i == self.pergunta_atual["correta"]:
                            self.resultado = "certo"
                        else:
                            self.resultado = "errado"
                        break
        return self.estado

    def desenhar(self):
        overlay = pygame.Surface((700, 500))
        overlay.set_alpha(220)
        overlay.fill((20, 30, 40))
        self.tela.blit(overlay, (0, 0))

        titulo = self.fonte_info.render("QUIZ EDUCATIVO - Resgate!", True, (100, 255, 100))
        self.tela.blit(titulo, (200, 60))

        if self.pergunta_atual:
            texto_perg = self.fonte_pergunta.render(self.pergunta_atual["pergunta"], True, (255, 255, 255))
            self.tela.blit(texto_perg, (50, 120))

            if self.resultado is None:
                for botao in self.botoes:
                    botao.desenhar()
            else:
                if self.resultado == "certo":
                    msg = self.fonte_pergunta.render("CORRETO! +100 pontos", True, (50, 255, 50))
                    self.tela.blit(msg, (200, 280))
                else:
                    msg = self.fonte_pergunta.render("ERRADO! Tente de novo", True, (255, 80, 80))
                    self.tela.blit(msg, (200, 280))
                    correta = self.pergunta_atual["opcoes"][self.pergunta_atual["correta"]]
                    dica = self.fonte_info.render(f"Resposta: {correta}", True, (200, 200, 100))
                    self.tela.blit(dica, (220, 330))


class GameOver:
    def __init__(self, tela, partida):
        self.tela = tela
        self.partida = partida
        self.estado = "gameover"
        self.titulo = Texto(tela, "FIM DE JOGO", 230, 120, (255, 80, 80), 48)
        self.botao_menu = Botao(tela, "VOLTAR AO MENU", 220, 320, 260, 50, (34, 139, 34))
        self.botao_sair = Botao(tela, "SAIR", 250, 390, 180, 50, (178, 34, 34))

    def atualizar(self, eventos):
        self.estado = "gameover"
        for e in eventos:
            if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                if self.botao_menu.foi_clicado(e.pos):
                    self.estado = "menu"
                elif self.botao_sair.foi_clicado(e.pos):
                    self.estado = "sair"
        return self.estado

    def desenhar(self):
        self.tela.fill((30, 10, 10))
        self.titulo.desenhar()
        fonte = pygame.font.SysFont("Arial", 28)
        pontos = fonte.render(f"Pontuação final: {self.partida.pontuacao}", True, (255, 255, 100))
        resgates = fonte.render(f"Animais resgatados: {self.partida.resgates}", True, (100, 255, 100))
        self.tela.blit(pontos, (200, 200))
        self.tela.blit(resgates, (180, 250))
        self.botao_menu.desenhar()
        self.botao_sair.desenhar()


class Vitoria:
    def __init__(self, tela, partida):
        self.tela = tela
        self.partida = partida
        self.estado = "vitoria"
        self.titulo = Texto(tela, "GUARDIÃO MESTRE!", 160, 100, (255, 215, 0), 44)
        self.subtitulo = Texto(tela, "Você salvou a fauna brasileira!", 150, 170, (100, 255, 100), 28)
        self.botao_menu = Botao(tela, "VOLTAR AO MENU", 220, 320, 260, 50, (34, 139, 34))
        self.botao_sair = Botao(tela, "SAIR", 250, 390, 180, 50, (178, 34, 34))

    def atualizar(self, eventos):
        self.estado = "vitoria"
        for e in eventos:
            if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                if self.botao_menu.foi_clicado(e.pos):
                    self.estado = "menu"
                elif self.botao_sair.foi_clicado(e.pos):
                    self.estado = "sair"
        return self.estado

    def desenhar(self):
        self.tela.fill((10, 40, 20))
        self.titulo.desenhar()
        self.subtitulo.desenhar()
        fonte = pygame.font.SysFont("Arial", 26)
        pontos = fonte.render(f"Pontuação: {self.partida.pontuacao}", True, (255, 255, 100))
        self.tela.blit(pontos, (250, 240))
        self.botao_menu.desenhar()
        self.botao_sair.desenhar()