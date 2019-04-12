#Adding a sense that the cars are moving
from addons import car
import pygame
import time
import random

pygame.init()
#resolution of the game
display_width = 800
display_height = 600

BLACK = (0,0,0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GRAY = (51,51,51)

car_width = 37

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Macron Racy')
clock = pygame.time.Clock()

carImg = pygame.image.load('nu.png')

def things(thingx, thingy, thingw, thingh, color):
    #pygame draw
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])




#def car(x,y):
    #blit draws the background in the image tajes in the image and where(tuple)
#    gameDisplay.blit(carImg,(x,y))

def drawCar(car):
    gameDisplay.blit(car.spite, )

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

def drawGameArea():
    #Drawing on Screen
    screen.fill(GREEN)
    #Draw The Road
    pygame.draw.rect(screen, GREY, [40,0, 200,300])
    #Draw Line painting on the road
    pygame.draw.line(screen, WHITE, [140,0],[140,300],5)

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

    #This will be a list that will contain all the sprites we intend to use in our game.
    all_sprites_list = pygame.sprite.Group()

    playerCar = car.Car()
    playerCar.rect.x = 200
    playerCar.rect.y = 450
    print(playerCar.rect.width)
    # Add the car to the list of objects
    all_sprites_list.add(playerCar)

    stripe_y = -100
    stripe_length = 30
    stripe_gap = 70
    speed = 1
    second = 0
    while not gameExit:
        #creates a list of an event per second mouse clicks, keyboard
        '''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                #if there is a key press
            if event.type == pygame.KEY:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

                '''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        keys = pygame.key.get_pressed()
        x_change = 0
        speed_factor = 0.1 + speed/100
        if keys[pygame.K_LEFT]:
            playerCar.moveLeft(10 * speed_factor)
        if keys[pygame.K_RIGHT]:
            playerCar.moveRight(10 * speed_factor)
        x += x_change

        #Drawing on Screen
        gameDisplay.fill(BLACK)
        #Draw The Road
        pygame.draw.rect(gameDisplay, GRAY, [0,0, 480,600])

        for i in range(7):
            gap_x = 60
            stripe_x = gap_x
            for i in range(7):
                pygame.draw.line(gameDisplay, WHITE, [stripe_x,stripe_y],[stripe_x,stripe_y + stripe_length],2)
                stripe_x += gap_x
            #pygame.draw.line(gameDisplay, WHITE, [240,stripe_y],[240,stripe_y + stripe_length],4)
            stripe_y = stripe_y + stripe_length + stripe_gap
            if stripe_y > 600:
                stripe_y -= 600 + 100

        stripe_y += speed
        #Draw Line painting on the road
        #pygame.draw.line(gameDisplay, WHITE, [140,0],[140,300],5)
        #Now let's draw all the sprites in one go. (For now we only have 1 sprite!)
        all_sprites_list.draw(gameDisplay)

        #Refresh Screen
        pygame.display.flip()

        #things(thingx, thingy, thingw, thingh, color)
        #things(thing_startx, thing_starty, thing_width, thing_height, BLACK)
        #thing_starty += thing_speed
        #car(x,y)
        '''
        if x > display_width - car_width or x < 0:
            crash()
            #after box leaves the screen
        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_width)
            '''
        #updates display.update after event takes an arg or updates all
        #pygame.display.flip () always updates the entire thing
        #pygame.display.update()
        if second >= 60:
            speed += 1
            if speed > 50:
                speed = 50
            second = 0
        second +=1
        #how fast are you going to finish a task
        clock.tick(60)


game_loop()
#when the user want to QUIT
pygame.quit()
quit()
