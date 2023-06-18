import pygame
from sys import exit

width = 1280
height = 720

pygame.init()
clock = pygame.time.Clock()

class Ball(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y) -> None:
        super().__init__()
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.speed = [5,5]
        self.image = pygame.image.load('Ball.png')
        self.rect = self.image.get_rect(center = (self.pos_x, self.pos_y))
    
    def update(self):
        self.collision()
        self.rect.x += self.speed[0]   #update horizontal position of ball
        self.rect.y += self.speed[1]   #update vertical position of the ball

    def collision(self):
        #For better understanding each case is separeted
        if self.rect.right >= width:
            self.speed[0] *= -1
        elif self.rect.left <= 0:
            self.speed[0] *= -1
        if self.rect.top <= 0:
            self.speed[1] *= -1
        elif self.rect.bottom >= height:
            self.speed[1] *= -1

screen = pygame.display.set_mode((width, height))   #screen setup
pygame.display.set_caption('pygame Tutorial')       #create caption

Ball_sprite = Ball(width/2, height/2)   #create Ball class instance
Ball_group = pygame.sprite.Group()   #create sprite group
Ball_group.add(Ball_sprite)   #add Ball sprite to the sprite group

#game loop
while True:
    screen.fill((0,0,125))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    Ball_group.update()     #update sprites
    Ball_group.draw(screen)   #draw sprites

    pygame.display.update()
    clock.tick(60)
