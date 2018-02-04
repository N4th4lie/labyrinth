# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 2018

@author: N4th4lie
"""

import pygame
from pygame.locals import *
from constants import *
# CONSTANTS: filenames, window parameters,...


class Labwindow:

    def __init__(self, window, structure, items):
        self.window = window
        self.structure = structure
        self.items = items
        # Labwindow displays the list of items

    def display(self):

        # load images:
        ground = pygame.image.load(image_ground)
        wall = pygame.image.load(image_wall)
        finish = pygame.image.load(image_finish)
        # The finish line must contain transparence but problem occurs
        # with convert().
        # finish = pygame.image.load(image_finish).convert_alpha()
        guard = pygame.image.load(guard_im)

        # Initialization
        self.window.blit(ground, (0, 0))

        # Run through the Labyrinth lines. Display them.
        for num_line, line in enumerate(self.structure):
            # Run through sprites of each line
            for num_sprite, sprite in enumerate(line):
                # calculate the real position in pixels
                x = num_sprite * sprite_size
                y = num_line * sprite_size
                if sprite == 'W':
                    self.window.blit(wall, (x, y))
                elif sprite == 'F':
                    self.window.blit(finish, (x, y))
                    self.window.blit(guard, (x, y))

        # If the items are ready, run through the items list.
        for item in self.items:
            self.window.blit(item.image, (item.x, item.y))
        # Items counter :
        arial_font = pygame.font.SysFont("comicsansms", 20)
        n_items = str(3-len(self.items))
        items_counter = arial_font.render("Nombre d'objets collectés : " +
                                          n_items + "/3", True, (223, 255, 0))
        self.window.blit(items_counter, ((side_nb_sprites-1)/3*sprite_size,
                                         (side_nb_sprites-1)*sprite_size))


class Character:

    def __init__(self, image, case_x, case_y):
        self.image = pygame.image.load(image)
        # Position in 15x15 cases (utilisation easier than pixels)
        # and in pixels (parameters of blit())
        self.case_x = case_x
        self.case_y = case_y
        self.x = case_x * sprite_size
        self.y = case_y * sprite_size

    def move(self, direction, structure):

        # Right direction and not at the end of the window
        # and not a wall on the right
        if direction == '275' and self.case_x != (side_nb_sprites - 1) and \
                structure[self.case_y][self.case_x+1] != 'W':
            self.case_x += 1

        # Left direction and not at the beginning of the window
        # and not a wall on the left
        if direction == '276' and self.case_x != 0 and \
                structure[self.case_y][self.case_x-1] != 'W':
            self.case_x -= 1

        # Up direction and not at the top of the window
        # and not a wall above
        if direction == '273' and self.case_y != 0 and \
                structure[self.case_y-1][self.case_x] != 'W':
            self.case_y -= 1

        # Down direction and not at the bottom of the window
        # and not a wall below
        if direction == '274' and self.case_y != (side_nb_sprites - 1) and \
                structure[self.case_y+1][self.case_x] != 'W':
            self.case_y += 1

        # Calculate new position in pixels
        self.x = self.case_x * sprite_size
        self.y = self.case_y * sprite_size
