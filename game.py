from addons import car
import pygame
import time
import random

pygame.init()

# resolution of the game
display_width = 800
display_height = 600

# Game colors
BLACK = (0,0,0)
RED = (255, 0, 0)
GRAY = (51, 51, 51)
WHITE = (255, 255, 255)

car_width = 40


gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Brick Drifter')
clock = pygame.time.Clock()

carImg = pygame.image.load('nu.png')

def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: "+ str(count), True, RED )
    gameDisplay.blit(text, (0,0))

def things(thingx, thingy, thingw, thingh, color):
    # pygame draw
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

#def car(x,y):
    # blit draws the background in the image and takes in the car and where ( a tuple)
#    gameDisplay.blit(carImg,(x,y))

def text_objects(text, font):
    # True for anti aliasing
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font(None, 115)
    # returns text surface and text rectangle
    TextSurf, TextRect = text_objects(text, largeText)
    # centering the text
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    # pause for 2 seconds
    time.sleep(2)
    game_loop()

def crash():
    message_display('You Crashed')

def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    gameAreaX = 480

    x_change = 0

    thing_startx = random.randrange(0, gameAreaX - 40)
    print(thing_startx)
    thing_starty = -600
    thing_speed = 7
    thing_width = 40
    thing_height = 80

    thingCount = 1
    dodged = 0

    gameExit = False

    all_sprites_list = pygame.sprite.Group()

    playerCar = car.Car()
    playerCar.rect.x = 200
    playerCar.rect.y = 450

    all_sprites_list.add(playerCar)

    stripe_y = -100
    stripe_length = 30
    stripe_gap = 70
    speed = 1
    second = 0

    while not gameExit:
        # creates a list of an event per second mouse clicks, keyboard
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                #if there is a key press

        keys = pygame.key.get_pressed()
        x_change = 0
        speed_factor = 0.1 + speed/100
        if keys[pygame.K_LEFT]:
            playerCar.moveLeft(15 * speed_factor)
        if keys[pygame.K_RIGHT]:
            playerCar.moveRight(15 * speed_factor)
        x += x_change

        # Drawing on Screen
        gameDisplay.fill(black)
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

        # things(thingx, thingy, thingw, thingh, color)
        things(thing_startx, thing_starty, thing_width, thing_height, RED)
        thing_starty += thing_speed
        # car(x,y)
        things_dodged(dodged)

        all_sprites_list.draw(gameDisplay)

        #Refresh Screen
        pygame.display.flip()

        if second >= 60:
            speed += 1
            if speed > 100:
                speed = 100
            second = 0
        second +=1

        if x > gameAreaX - playerCar.rect.width or x < 0:
            crash()
            # after box leaves the screen
        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, gameAreaX - 40)
            dodged += 1
            thing_speed += 0.5



        if playerCar.rect.y < thing_starty + thing_height:
            # x is the location of car (If top left of car is greater than box)
            if playerCar.rect.x > thing_startx and playerCar.rect.x < thing_startx + thing_width or playerCar.rect.x + playerCar.rect.width > thing_startx and playerCar.rect.x + playerCar.rect.width < thing_startx + thing_width:
                crash()
        # updates display.update after event takes an arg or updates all
        # pygame.display.flip () always updates the entire thing
        all_sprites_list.draw(gameDisplay)
        pygame.display.update()

        # how fast are you going to finish a task
        clock.tick(60)


game_loop()
# when the user want to QUIT
pygame.quit()
quit()
