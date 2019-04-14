from addons import car
import pygame
import time
import random

# Game colors
BLACK = (0,0,0)
RED = (255, 0, 0)
GRAY = (51, 51, 51)
WHITE = (255, 255, 255)

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Brick Drifter')
        # resolution of the game
        self.display_width = 800
        self.display_height = 600
        self.gameDisplay = pygame.display.set_mode((self.display_width, self.display_height))
        self.clock = pygame.time.Clock()
        self.ticks = 60
        self.exit = False
        self.dodged = 0
        self.high_score = 0

    def show_dodged(self):
        font = pygame.font.SysFont(None, 25)
        text = font.render("Dodged: "+ str(self.dodged), True, RED )
        self.gameDisplay.blit(text, (480,0))

    def show_high_score(self):
        font = pygame.font.SysFont(None, 25)
        text = font.render("High Score: "+ str(self.high_score), True, WHITE )
        self.gameDisplay.blit(text, (480, 40))

    def things(self, thingx, thingy, thingw, thingh, color):
        # pygame draw
        pygame.draw.rect(self.gameDisplay, color, [thingx, thingy, thingw, thingh])

    def message_display(self, text):
        largeText = pygame.font.Font(None, 115)

        def text_objects(text, font):
            # True for anti aliasing
            textSurface = font.render(text, True, BLACK)
            return textSurface, textSurface.get_rect()
        # returns text surface and text rectangle
        TextSurf, TextRect = text_objects(text, largeText)
        # centering the text
        TextRect.center = ((self.display_width/2),(self.display_height/2))
        self.gameDisplay.blit(TextSurf, TextRect)
        pygame.display.update()
        # pause for 2 seconds
        time.sleep(2)
        self.run()

    def crash(self):
        if self.dodged > self.high_score:
            self.high_score = self.dodged
        self.message_display('You Crashed')

    def run(self):
        self.dodged = 0
        x = (self.display_width * 0.45)
        y = (self.display_height * 0.8)
        gameAreaX = 480
        x_change = 0
        thing_startx = random.randrange(0, gameAreaX - 40)
        thing_starty = -600
        thing_speed = 7
        thing_width = 40
        thing_height = 80

        all_sprites_list = pygame.sprite.Group()

        playerCar = car.Car()
        playerCar.rect.x = 200
        playerCar.rect.y = 450

        all_sprites_list.add(playerCar)

        stripe_y = -100
        stripe_length = 30
        stripe_gap = 70
        speed = 15
        second = 0

        while not self.exit:
            # Event queue
            # creates a list of an event per second mouse clicks, keyboard
            for event in pygame.event.get():
                # if user wants to quit
                if event.type == pygame.QUIT:
                    self.exit = True

            keys = pygame.key.get_pressed()
            x_change = 0
            speed_factor = 0.1 + speed/100
            if keys[pygame.K_LEFT]:
                playerCar.moveLeft(15 * speed_factor)
            if keys[pygame.K_RIGHT]:
                playerCar.moveRight(15 * speed_factor)
            x += x_change

            # Drawing on Screen
            self.gameDisplay.fill(BLACK)
            pygame.draw.rect(self.gameDisplay, GRAY, [0,0, 480, 600])

            for i in range(7):
                gap_x = 60
                stripe_x = gap_x
                for i in range(7):
                    pygame.draw.line(self.gameDisplay, WHITE, [stripe_x,stripe_y],[stripe_x,stripe_y + stripe_length],2)
                    stripe_x += gap_x
                # pygame.draw.line(self.gameDisplay, WHITE, [240,stripe_y],[240,stripe_y + stripe_length],4)
                stripe_y = stripe_y + stripe_length + stripe_gap
                if stripe_y > 600:
                    stripe_y -= 700

            stripe_y += speed

            # self.things(thingx, thingy, thingw, thingh, color)
            self.things(thing_startx, thing_starty, thing_width, thing_height, RED)
            thing_starty += thing_speed
            # car(x,y)
            self.show_dodged()
            self.show_high_score()

            all_sprites_list.draw(self.gameDisplay)

            #Refresh Screen
            pygame.display.flip()

            if second >= 60:
                speed += 1
                if speed > 100:
                    speed = 100
                second = 0
            second +=1

            if x > gameAreaX - playerCar.rect.width or x < 0:
                self.crash()
                # after box leaves the screen
            if thing_starty > self.display_height:
                thing_starty = 0 - thing_height
                thing_startx = random.randrange(0, gameAreaX - 40)
                self.dodged += 1
                thing_speed += 0.5

            if playerCar.rect.y < thing_starty + thing_height:
                # x is the location of car (If top left of car is greater than box)
                if playerCar.rect.x > thing_startx and playerCar.rect.x < thing_startx + thing_width or playerCar.rect.x + playerCar.rect.width > thing_startx and playerCar.rect.x + playerCar.rect.width < thing_startx + thing_width:
                    self.crash()
            # updates display.update after event takes an arg or updates all
            # pygame.display.flip () always updates the entire thing
            all_sprites_list.draw(self.gameDisplay)
            pygame.display.update()

            # how fast are you going to finish a task
            self.clock.tick(self.ticks)

        pygame.quit()

if __name__ == '__main__':
    game = Game()
    game.run()
