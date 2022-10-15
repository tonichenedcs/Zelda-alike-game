import pygame, sys
from settings import *
from debug import *

class Game:
    def __init__(self):

        # Start all the imported pygame modules
        pygame.init()

        # Setting the size of the display, which returns a pygame.surface object
        self.monitor = pygame.display.set_mode(size = (WIDTH, HEIGHT))

        # Create an object to track the time
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Mock zelda")

    def run(self):
        while True:
            # Get events from the queue
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # Quit from the pygame program
                    pygame.quit()
                    # Quit from the python
                    sys.exit()

                self.monitor.fill('Black')
                # It can be used to update part of the screen, without parameter it will update the whole screen
                pygame.display.update()
                # Limit the frame rate of our game
                self.clock.tick(FPS)


if __name__ == '__main__':
    game = Game()
    game.run()



