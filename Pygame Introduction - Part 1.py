import pygame
from sys import exit

width = 1280   #screen width
height = 720   #screen height
rect_w = 100   #rectangle width
rect_h = 100   #rectangle height
pos_x = 100    #position of rect
pos_y = 100    #position of rect
speed = 5      

pygame.init()
clock = pygame.time.Clock()

#screen setup
screen = pygame.display.set_mode((width, height))
#game screen title
pygame.display.set_caption('pygame Tutorial')
#load and save image
image = pygame.image.load('Ball.png')
#get rectangle from image surface
rect = image.get_rect(topleft = (400, 200))

#game loop
while True:  
    keys = pygame.key.get_pressed() #get keys pressed
    if keys[pygame.K_RIGHT]:
        pos_x += speed
    elif keys[pygame.K_LEFT]:
        pos_x -= speed
    elif keys[pygame.K_UP]:
        pos_y -= speed
    elif keys[pygame.K_DOWN]:
        pos_y += speed

    screen.fill((0,0,125))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    #draw image surface on screen
    screen.blit(image, rect)
    #draw shapes
    pygame.draw.rect(screen, (250, 0, 0), (pos_x,pos_y,rect_w,rect_h) )
    pygame.draw.rect(screen, (250, 0, 0), (210,100,rect_w,rect_h), width = 5)
    pygame.draw.circle(screen, (0, 250, 0), (width/2, height/2), 50)
    #update display
    pygame.display.update()
    clock.tick(60)
