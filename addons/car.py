import pygame
WHITE = (255, 255, 255)

class Car(pygame.sprite.Sprite):
    #This class represents a car. It derives from the "Sprite" class in Pygame.

    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()

        # Pass in the color of the car, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        #self.image = pygame.Surface([width, height])
        #self.image.fill(WHITE)
        #self.image.set_colorkey(WHITE)

        # Instead we could load a proper pciture of a car...
        self.image = pygame.image.load("addons/car.png").convert_alpha()

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()

        self.angle = 0

    def moveRight(self, pixels):
        self.rect.x += pixels

    def moveLeft(self, pixels):
        self.rect.x -= pixels

    def straight(self):
        self.image = pygame.transform.rotate(self.image, -self.angle)
        self.angle = 0
