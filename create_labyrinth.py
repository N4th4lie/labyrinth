# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 11:15:00 2018

@author: N4th4lie
"""

# Jeu (interface graphique,...)
import pygame

# pour les QUIT, KEYDOWN,...
from pygame.locals import *

pygame.init()

""" CONSTANTS: filenames, window parameters,..."""
from constants import *


def create_labyrinth():

    window = pygame.display.set_mode((side_size,side_size))
    pygame.display.set_caption(window_title)
    icone = pygame.image.load(image_icone)
    pygame.display.set_icon(icone)

    # !!!!!!!!! la méthode convert() plante le programme
    # ground = pygame.image.load(image_ground).convert()
    ground = pygame.image.load(image_ground)
    window.blit(ground, (0,0))

    """
    Load the labrinth from a text file
    """	

    # Read the text file in a WITH OPEN() and write the result in a list of lists
    # W=wall, S=start, F=finish, n=nothing
    with open(fic_labyrinth, "r", encoding="utf8") as f:
        labyrinth = []
        for line in f:
            line_level = [sprite for sprite in line if sprite!="\n"]
            labyrinth.append(line_level)
            
    # loading images:
    wall = pygame.image.load(image_wall)
    finish = pygame.image.load(image_finish)
    # The finish line must contain transparence but problem occurs with convert()
    # finish = pygame.image.load(image_finish).convert_alpha()

    # Run through the Labyrinth lines
    for num_line,line in enumerate(labyrinth):
        # Run through sprites of each line
        for num_sprite,sprite in enumerate(line):
            # calculate the real position in pixels
            x = num_sprite * sprite_size
            y = num_line * sprite_size
            if sprite == 'W':
                window.blit(wall, (x,y))
            elif sprite == 'F':
                window.blit(finish, (x,y))

    return(window)   