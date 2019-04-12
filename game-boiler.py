import os
from math import tan, radians, degrees, copysign

import pygame
from pygame.math import Vector2

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Brick Drifter")
        width = 1280
        height = 720
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.ticks = 60
        self.exit = False

    def run(self):
        while not self.exit:
            dt = self.clock.get_time() / 1000

            # Event queue
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit = True

            # User input
            pressed = pygame.key.get_pressed()

            # Brick Drifter Logic

            # Drawing
            self.screen.fill((0, 0, 0))
            pygame.display.flip()

            self.clock.tick(self.ticks)
        pygame.quit()

if __name__ == '__main__':
    game = Game()
    game.run()
