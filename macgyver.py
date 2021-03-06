﻿# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 15:44:00 2018

@author: N4th4lie
"""

import pygame
import random

# QUIT, KEYDOWN,...
from pygame.locals import *
# CONSTANTS: filenames, parameters,...
from constants import *
# CLASSES : Labwindow et Characters
from classes import *

pygame.init()

# Open a window
window = pygame.display.set_mode((side_size, side_size))
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
        line_level = [sprite for sprite in line if sprite != "\n"]
        labyrinth_structure.append(line_level)

# Create the labyrinth window
labyrinth = Labwindow(window, labyrinth_structure, [])
# Display
labyrinth.display()

# Refresh the window
pygame.display.flip()

# To create the characters and the items, you need to know their position

# Start (start_case_x,start_case_y) is Mac Gyver's initial position
# Finish (finish_case_x,finish_case_y) : the guard's place
# Free : the list of all the free cases for the items
free = []
for num_line, line in enumerate(labyrinth_structure):
    for num_sprite, case in enumerate(line):
        if case == 'S':
            start_case_x = num_sprite
            start_case_y = num_line
        elif case == 'F':
            finish_case_x = num_sprite
            finish_case_y = num_line
        elif case == 'n':
            free.append((num_sprite, num_line))

# Create and display Mac Gyver
macgyver = Character(macgyver_im, start_case_x, start_case_y)
window.blit(macgyver.image, (macgyver.x, macgyver.y))

# Randomize the items positions and create the items
# nota: items have the same attributes as Character's objects
labyrinth.items = []
items_im = [item1_im, item2_im, item3_im]
for i in range(0, 3):
    n = random.randrange(0, len(free)-1)
    labyrinth.items.append(Character(items_im[i], free[n][0], free[n][1]))
    del free[n]

# Display the items
labyrinth.display()

# Refresh the window
pygame.display.flip()

go_on = True
game_over = False
while go_on:
    # Limitation speed for while
    pygame.time.Clock().tick(30)

    for event in pygame.event.get():
        if event.type == QUIT:
            go_on = False
        elif event.type == KEYDOWN:
            # Key Tab for moving Mac Gyver
            if (not game_over) and \
                    event.key in (K_RIGHT, K_LEFT, K_UP, K_DOWN):
                macgyver.move(str(event.key), labyrinth_structure)

                # if Mac Gyver is reaching an item,
                # collect it <-> delete the item from the list
                for i, item in enumerate(labyrinth.items):
                    if macgyver.x == item.x and macgyver.y == item.y:
                        del labyrinth.items[i]
                        break
            # Quit game after the game over message has been read
            if game_over:
                go_on = False

    # Display the labyrinth with items
    labyrinth.display()
    # Refresh the window with Mac Gyver's new position
    window.blit(macgyver.image, (macgyver.x, macgyver.y))
    pygame.display.flip()

    # If Mac Gyver reached the finish:
    if macgyver.case_x == finish_case_x \
            and macgyver.case_y == finish_case_y:
        game_over = True
        arial_font = pygame.font.SysFont("comicsansms", 20)
        # arial_font = pygame.font.SysFont("Arial", 20)
        end_message2 = arial_font.render(
            "Appuis sur une touche pour quitter. Au revoir.",
            True, (223, 255, 0))
        # Mac Gyver reached the finish case.
        # If no more items displayed on the window, you won or lost:
        if labyrinth.items == []:
            end_message1 = arial_font.render(
                "FÉLICITATIONS ! Mac Gyver est libre !",
                True, (223, 255, 0))
        else:
            end_message1 = arial_font.render(
                "PERDU ! Le gardien arrête Mac Gyver !",
                True, (223, 255, 0))

        window.blit(end_message1, (10, 30))
        window.blit(end_message2, (10, 50))
        pygame.display.flip()

pygame.quit()
