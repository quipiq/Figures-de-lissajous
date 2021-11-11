from math import *
from time import *
import pygame
from pygame.locals import *
import pygame.gfxdraw
import sys

os.system('cls')

print("\n\nFonctionement : \ntouche q : arette le programme\ntouche fleche du haut : augmente delta (accèlère la vitesse de la figure dans un sens)\ntouche fleche du bas : diminue delta (accèlère dans le sens inverse de la fleche du haut la figure, cela permet de l'aretter et de la faire changer de sens)\n\n\n")

delta_val = 0.01
A = 100
B = 100
a = 0
b = 0
delta = 0
t=0

run = True

pygame.init()

fenetre = pygame.display.set_mode((640, 480))

while run:

    for evenement in pygame.event.get():
        if evenement.type==KEYDOWN:
            Touche = pygame.key.get_pressed()
            if Touche[K_q]:
                pygame.quit()
                sys.exit()
            if Touche[K_UP]:
                delta_val+=0.01
            if Touche[K_DOWN]:
                delta_val-=0.01

    for i in range(0,1000):
        t+=0.01
        x = A * sin(a*t + delta) 
        y = B * sin(b*t) 
        pygame.gfxdraw.pixel(fenetre, int(x+300), int(y+220), (255,0,0))

    delta+=delta_val
    pygame.display.flip()
    sleep(0.01)
    fenetre.fill(0)
    if a<1 and b<1:
        b+=0.001
        a+=0.001
    print(f"a = {a}   b = {b}")




