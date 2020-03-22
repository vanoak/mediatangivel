from SimpleCV import Camera
import pygame
from pygame.locals import *

# definir cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERDE = (0, 255, 0)
VERMELHO = (255, 0, 0)

pygame.init()
#python2 projecto.py
# definir altura e largura
dimensoes = (600, 800)
ecran = pygame.display.set_mode(dimensoes)
#ecran = pygame.display.set_mode(dimensoes, pygame.FULLSCREEN) # descomentar para fullscreen

lista_imagens = (pygame.image.load('monalisa01.jpg'),
                 pygame.image.load('monalisa02.jpg'),
                 pygame.image.load('monalisa03.jpg'),
                 pygame.image.load('monalisa04.jpg'),
                 pygame.image.load('monalisa05.jpg'),
                 pygame.image.load('monalisa06.jpg'),
                 pygame.image.load('monalisa07.jpg'),
                 pygame.image.load('monalisa08.jpg'),
                 pygame.image.load('monalisa09.jpg'),
                 pygame.image.load('monalisa010.jpg'),
                 pygame.image.load('monalisa011.jpg'),
                 pygame.image.load('monalisa012.jpg'),
                 pygame.image.load('monalisa13.jpg'),
                 pygame.image.load('monalisa-01.jpg'),
                 pygame.image.load('monalisa-02.jpg'),
                 pygame.image.load('monalisa-03.jpg'),
                 pygame.image.load('monalisa-04.jpg'),
                 pygame.image.load('monalisa-05.jpg'),
                 pygame.image.load('monalisa-06.jpg'),
                 pygame.image.load('monalisa-07.jpg'))



pygame.display.set_caption("Projecto 1")

# flag que se verdadeira termina o programa
quero_sair = False

# usado para calcular as frames por segundo
clock = pygame.time.Clock()

myCamera = Camera(prop_set={'width':320, 'height': 240})

# ciclo principal
while not quero_sair:

    # verifica eventos
    
    frame = myCamera.getImage()
    faces = frame.findHaarFeatures('face')
    
    if faces is not None:
        for face in faces:
            print "Face at: " + str(face.coordinates()) 
    
    for event in pygame.event.get():

        # se o botao da janela sair for clicado, sai
        if event.type == pygame.QUIT:
            quero_sair = True

        # se o rato for clicado, nao faz nada
        if event.type == MOUSEBUTTONDOWN:
            pass

        # se uma tecla for premida
        elif event.type == KEYDOWN:

            # se a tecla premida for o escape, sai
            if event.key == K_ESCAPE:
                quero_sair = True

    # --- processamento deve ser feito aqui

    # --- limpeza de ecran da frame anterior, com cor solida ou cenario previamente carregado.

    ecran.fill(BRANCO)

    # --- desenhar coisas no ecran

    # --- mostrar as coisas que desenhamos
    pygame.display.flip()

    # --- limitar a 60 fps
    clock.tick(60)

# sair
pygame.quit()