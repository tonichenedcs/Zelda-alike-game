import pygame

# Start all the modules imported from pygame, so we can create a font object
pygame.init()
# This creates a new font object
font = pygame.font.Font(None, 30)


# debug method used to display information on the corner of the screen
def debug(info, x=10, y=10):
    display_surface = pygame.display.get_surface()
    # This creates a new surface object, with info rendered on it. antialias = True, color = 'White', we want to
    # place it over the display surface
    debug_surface = font.render(str(info), True, 'White')
    debug_screen = debug_surface.get_rect(topleft=(x, y))
    # Draw the debug screen(which is a rectangle) onto the display surface
    pygame.draw.rect(display_surface, 'Black', debug_screen)
    # We will put the debug surface object onto the display screen, at the target location debug screen
    display_surface.blit(debug_surface, debug_screen)

