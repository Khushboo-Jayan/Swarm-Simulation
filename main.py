import pygame
import os       #import operating systems to help you define the path for these images

pygame.init()

displayWidth = 800
displayHeight = 600
imgWidth = 100
imgHeight = 100

black = (0,0,0,)
white = (255,255,255)


gameDisplay = pygame.display.set_mode((displayWidth,displayHeight))
pygame.display.set_caption('A bit racey')
clock = pygame.time.Clock()
carImg = pygame.image.load(os.path.join('Assets', 'raceCar.png'))
raceCarImg = pygame.transform.rotate(pygame.transform.scale(carImg, (imgWidth,imgHeight)), -90)  #resize using scale rotate using rotate both in transform 


#car function
def car(x,y): 
    gameDisplay.blit(raceCarImg,(x,y))

x = (displayWidth * 0.45)
y = (displayHeight * 0.8)

crashed = False

while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

    gameDisplay.fill(white)
    car(x,y)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()