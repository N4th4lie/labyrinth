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

""" CREATE_LABYRINTH creates the labyrinth screen """
from create_labyrinth import *
create_labyrinth()

# Rafraîchissement écran                
pygame.display.flip()

continuer = True
while continuer:
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = False

pygame.quit()
