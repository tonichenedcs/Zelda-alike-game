import pygame
from settings import *
from tile import Tile
from player import Player


class Level:
    def __init__(self):
        # Get the display so we can draw each level on it
        self.display_surface = pygame.display.get_surface()

        # Split all the assets into two different sprites groups
        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()

        self.create_map()

    def create_map(self):
        for i in range(len(WORLD_MAP)):
            for j in range(len(WORLD_MAP[0])):
                x = j * TILE_SIZE
                y = i * TILE_SIZE

                if WORLD_MAP[i][j] == 'x':
                    Tile(pos=(x, y), groups=[self.visible_sprites, self.obstacle_sprites])
                elif WORLD_MAP[i][j] == 'p':
                    Player(pos=(x, y), groups=[self.visible_sprites])

    # Update and draw the game
    def run(self):
        # The sprite.Group.draw will blit all the sprite images on the specified surface
        self.visible_sprites.draw(self.display_surface)

