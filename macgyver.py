# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 15:44:00 2018

@author: N4th4lie
"""

import pygame

# QUIT, KEYDOWN,...
from pygame.locals import *

pygame.init()

""" CONSTANTS: filenames, parameters,..."""
from constants import *

""" CLASSES : Labwindow et Characters """
from classes import *

# Open a window
window = pygame.display.set_mode((side_size,side_size))
pygame.display.set_caption(window_title)
icone = pygame.image.load(image_icone)
pygame.display.set_icon(icone)

# Load the labyrinth structure from a text file.
# The labyrinth_structure gives positions of walls, start and finish cases.
# Read the text file in a WITH OPEN() and write the result in a list of lists
# W=wall, S=start, F=finish, n=nothing
with open(fic_labyrinth, "r", encoding="utf8") as f:
    labyrinth_structure = []
    for line in f:
        line_level = [sprite for sprite in line if sprite!="\n"]
        labyrinth_structure.append(line_level)

# Create the labyrinth window
labyrinth = Labwindow(window, labyrinth_structure)
# Display
labyrinth.display()

# Refresh the window               
pygame.display.flip()

""" Etape 2 du projet : créer Mac Gyver et le diriger vers la sortie  """

# Start and Finish localisation :
for num_line, line in enumerate(labyrinth_structure):
    if 'S' in line:
        start_case_x = line.index('S')
        start_case_y = num_line
    if 'F' in line:
        finish_case_x = line.index('F')
        finish_case_y = num_line
    
# Create the caracter Mac Gyver
macgyver = Character(macgyver_im, start_case_x, start_case_y)
# Affichage de Mac Gyver
window.blit(macgyver.image, (macgyver.x, macgyver.y))

# Refresh the window               
pygame.display.flip()

continuer = True
succeed = False
while continuer:
    #Limitation speed for while
    pygame.time.Clock().tick(30)

    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = False
            
        elif event.type == KEYDOWN:
		     
            # Key Tab for moving Mac Gyver
            if (not succeed) and event.key in (K_RIGHT, K_LEFT, K_UP, K_DOWN):
                macgyver.move(str(event.key),labyrinth_structure)
 		     
            # Key Tab for moving Mac Gyver
            if succeed :
               continuer = False
   
    # Display the initial labyrinth without Mac Gyver
    labyrinth.display()

    # Refresh the window with Mac Gyver's new position
    window.blit(macgyver.image, (macgyver.x, macgyver.y))
    pygame.display.flip()
    
    if macgyver.case_x == finish_case_x and macgyver.case_y == finish_case_y:
        
        # Chargement d'une font:
        #calibri_font = pygame.font.SysFont("Calibri", 20)
        arial_font = pygame.font.SysFont("Arial", 20)
        # Font reçoit un fichier
        # Création d'une surface pour le score lui-même:
        succeed = True
        end_message1 = arial_font.render("FELICITATIONS ! Mac Gyver est libre !", True, (223, 255, 0))
        end_message2 = arial_font.render("Appuis sur une touche pour quitter. Au revoir.", True, (223, 255, 0))
        window.blit(end_message1, (0, 5))
        window.blit(end_message2, (0, 20))
        pygame.display.flip()

pygame.quit()
