import pygame
import os
import random

tela_largura = 500
tela_altura = 800

imagem_cano = pygame.transform.scale2x(pygame.image.load('./imgs/pipe.png'))
imagem_chao = pygame.transform.scale2x(pygame.image.load('./imgs/base.png'))
imagem_background = pygame.transform.scale2x(pygame.image.load('./imgs/bg.png'))
imagens_passsaro = [
    pygame.transform.scale2x(pygame.image.load('.imgs/bird1.png')),
    pygame.transform.scale2x(pygame.image.load('.imgs/bird2.png')),
    pygame.transform.scale2x(pygame.image.load('.imgs/bird3.png')),
]

pygame.font.init()
fonte_pontos = pygame.font.SysFont('Arial', 20)

class Passaro:
    imgs = imagens_passsaro

    #animação da rotação
    rotacao_maxima = 25
    velocidade_rotacao = 20
    tempo_animacao = 5

    #atribuindo atributos iniciais
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angulo = 0
        self.velocidade = 0
        self.altura = self.y
        self.tempo = 0
        self.contagem_imagem = 0
        self.imagem = self.imgs

    def pular(self):
        self.velocidade = -10.5
        self.tempo = 0
        self.altura = self.y

    def mover(self):
        #calcular o deslocamento
        self.tempo += 1
        deslocamento = 1.5 * (self.tempo ** 2) + self.velocidade * self.tempo

        #restringir o deslocamento
        if deslocamento > 16:
            deslocamento = 16
        elif deslocamento < 0:
            deslocamento -= 2

        self.y += deslocamento

        #calcular o ângulo do pássaro
        if deslocamento < 0 or self.y < (self.altura + 50):
            if self.angulo < self.rotacao_maxima:
                self.angulo = self.rotacao_maxima
        else:
            if self.angulo > -90:
                self.angulo -= self.velocidade_rotacao

    def desenhar(self):
        #definir qual imagem do pássaro usar:
        if self.contagem_imagem < self.tempo_animacao:
            self.imagem = self.imgs[0]
        elif self.contagem_imagem < self.tempo_animacao * 2:
            self.imagem = self.imgs[1]
        elif self.contagem_imagem < self.tempo_animacao * 3:
            self.imagem = self.imgs[2]
        elif self.contagem_imagem < self.tempo_animacao * 4:
            self.imagem = self.imgs[1]
        elif self.contagem_imagem < self.tempo_animacao * 4 + 1:
            self.imagem = self.imgs[0]
            self.contagem_imagem = 0
            
        #caso o pásssaro estiver caindo ou não, bater asas:
        if self.angulo <= -80:
            self.imagem = self.imgs[1]
            self.contagem_imagem = self.tempo_animacao*2

        #desenhar a imagem:
        imagem_rotacionada = pygame.transform.rotate(self.imagem, self.angulo)
        posicao_centro_imagem = self.imagem.get_rect(topleft = (self.x, self.y)).center
        retangulo = imagem_rotacionada.get_rect(center = posicao_centro_imagem)
        tela.blit(imagem_rotacionada, retangulo.topleft)


# class Cano:
#     pass

# class Chao:
#     pass