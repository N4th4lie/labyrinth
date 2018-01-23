# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 15:44:00 2018

@author: N4th4lie
"""

# Jeu (interface graphique,...)
import pygame

# pour les QUIT, KEYDOWN,...
from pygame.locals import *

pygame.init()

""" CONSTANTES DU JEU """

#Paramètres de la fenêtre
nombre_sprite_cote = 15
taille_sprite = 30
cote_fenetre = nombre_sprite_cote * taille_sprite

#Personnalisation de la fenêtre
titre_fenetre = "Aide MAC GYVER à s'échapper !"
image_icone = "images\lisasimpson.ico"

#Fichier Labyrinth.txt
fic_labyrinth = "labyrinth.txt"

#Listes des images du jeu
image_fond = "images\ground.jpg"
image_mur = "images\wallbrick.png"
image_arrivee = "images\door_open.png"

""" Fin Constantes du jeu """

fenetre = pygame.display.set_mode((cote_fenetre, cote_fenetre))
pygame.display.set_caption(titre_fenetre)
imico = pygame.image.load(image_icone)
pygame.display.set_icon(imico)

# !!!!!!!!! la méthode convert() plante le programme
# fond = pygame.image.load(image_fond).convert()
fond = pygame.image.load(image_fond)
fenetre.blit(fond, (0,0))

"""
AFFICHAGE DU LABYRINTHE à partir d'un fichier texte
"""	

# Ouverture du fichier texte et parcours des lignes avec WITH OPEN()
# Dans le fichier texte : M=mur, D=départ, A=arrivée, x=rien
with open(fic_labyrinth, "r", encoding="utf8") as f:
    labyrinth = []
    for line in f:
        line_level = [sprite for sprite in line if sprite!="\n"]
        labyrinth.append(line_level)
            
# Chargement des images :
mur = pygame.image.load(image_mur)
arrivee = pygame.image.load(image_arrivee)
# l'arrivée deoit contenir de la transparence mais problème convert()
# arrivee = pygame.image.load(image_arrivee).convert_alpha()

# Parcours des lignes du labyrinthe
for num_line,line in enumerate(labyrinth):
    # Parcours des sprites des lignes
	for num_sprite,sprite in enumerate(line):
	    #On calcule la position réelle en pixels
		x = num_sprite * taille_sprite
		y = num_line * taille_sprite
		if sprite == 'M':		   
		    fenetre.blit(mur, (x,y))
		elif sprite == 'A':		
		    fenetre.blit(arrivee, (x,y))
"""
Fin Affichage du labyrinthe 
"""	                

# Rafraîchissement écran                
pygame.display.flip()

continuer = True
while continuer:
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = False

pygame.quit()
