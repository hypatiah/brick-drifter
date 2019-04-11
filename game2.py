#Adding a sense that the cars are moving

import pygame
import time
import random

pygame.init()
#resolution of the game
display_width = 800
display_height = 600

black = (0,0,0)
white = (255, 255, 255)
RED = (255, 0, 0)
car_width = 73

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Macron Racy')
clock = pygame.time.Clock()

carImg = pygame.image.load('nu.png')

def things(thingx, thingy, thingw, thingh, color):
    #pygame draw
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])




def car(x,y):
    #blit draws the background in the image tajes in the image and where(tuple)
    gameDisplay.blit(carImg,(x,y))

def text_objects(text, font):
    #True for anti aliasing
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font(None, 115)
    #returns text surface and text rectangle
    TextSurf, TextRect = text_objects(text, largeText)
    #centering the text
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    #pause for 2 seconds
    time.sleep(2)
    game_loop()

def crash():
    message_display('You Crashed')


def game_loop():

    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0

    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 7
    thing_width = 100
    thing_height = 100

    gameExit = False

    while not gameExit:
        #creates a list of an event per second mouse clicks, keyboard
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                #if there is a key press
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change
        #Background color
        gameDisplay.fill(white)
        #things(thingx, thingy, thingw, thingh, color)
        things(thing_startx, thing_starty, thing_width, thing_height, black)
        thing_starty += thing_speed
        car(x,y)

        if x > display_width - car_width or x < 0:
            crash()
            #after box leaves the screen
        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_width)

        #updates display.update after event takes an arg or updates all
        #pygame.display.flip () always updates the entire thing
        pygame.display.update()

        #how fast are you going to finish a task
        clock.tick(60)


game_loop()
#when the user want to QUIT
pygame.quit()
quit()
