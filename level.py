import pygame
from settings import *
from tile import Tile
from player import Player
from debug import debug


class Level:
    def __init__(self):
        # Get the display, so we can draw each level on it
        self.display_surface = pygame.display.get_surface()

        # Split all the assets into two different sprites groups
        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()

        self.create_map()

    def create_map(self):
        for r_index, row in enumerate(WORLD_MAP):
            for c_index, col in enumerate(row):
                x = c_index * TILE_SIZE
                y = r_index * TILE_SIZE

                if col == 'x':
                    Tile(pos=(x, y), groups=[self.visible_sprites, self.obstacle_sprites])
                elif col == 'p':
                    self.player = Player(pos=(x, y), groups=[self.visible_sprites],
                                         obstacle_sprites=self.obstacle_sprites)

    # Update and draw the game
    def run(self):
        # The sprite.Group.draw will blit all the sprite images on the specified surface
        self.visible_sprites.draw(self.display_surface)

        # Update all the sprites that belongs to the visible_sprites group
        self.visible_sprites.update()
        debug(self.player.direction)

