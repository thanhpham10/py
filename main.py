import pygame
from pygame.draw import circle, rect
import random
from time import sleep

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode([600,300])
background_color = (155,155,155) 
pygame.display.set_caption("app | Build by thanhpham")
clock = pygame.time.Clock()
pygame.mixer.music.set_volume(100)
pygame.mixer.music.load("song.mp3")
pygame.mixer.music.play()

# color

# variable
circle_x, circle_y = 50, 50
x, y = 1,1
is_running = True


while is_running :
    screen.fill(background_color)
    clock.tick(60)
    # code 
    circle_color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    pygame.draw.circle(screen, circle_color, (circle_x,circle_y), 50)

    circle_x += x ; circle_y += y 
    
    if circle_x == 550 :
        x = -x
    if circle_y == 250 :
        y = -y
    if circle_x == 50 :
        x = abs(x)
    if circle_y == 50 :
        y = abs(y)

    # ---------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
    
    pygame.display.flip()

pygame.quit()

