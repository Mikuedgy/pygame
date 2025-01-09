import pygame
from sys import exit

pygame.init()
#Screen
screen = pygame.display.set_mode((0,0))
clock = pygame.time.Clock()
height, width = screen.get_size()

#Texto y colores
font = pygame.font.Font('fonts/Pixeltype.ttf',90)

black = (23, 32, 42)
white = (253, 254, 254)

#Cielo
surface_load_background = pygame.image.load('grapichs\Sky.jpg')
surface_background = pygame.transform.scale(surface_load_background,(height, width))
rect_background = surface_background.get_rect(topleft = (0,0))

surface_load_cloud = pygame.image.load('grapichs/nube.png')
rect_cloud = surface_load_cloud.get_rect(topleft = (0,0))

#Facultad
surface_load_plaza = pygame.image.load('grapichs\plaza.png')
surface_plaza = pygame.transform.scale(surface_load_plaza,(height, width))
rect_plaza = surface_plaza.get_rect(midbottom = (height//2, width))

#Titulo
surface_title = font.render('Unusual food at National comedor', False, 'white')
rect_title = surface_title.get_rect(center = (height//2,width//4))

#Jugar
surface_play = font.render('Jugar', False, white)
rect_play = surface_play.get_rect(center = (height//2,width//2))

#Salir
surface_exit = font.render('Salir', False, white)
rect_exit = surface_exit.get_rect(center = (height//2, width//1.5))




while True:
    #Loop events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if rect_exit.collidepoint(event.pos):
                pygame.quit()
                exit()
            if rect_play.collidepoint(event.pos):
                print('JUGANDO')
    

    #Background
    screen.blit(surface_background, rect_background)
    screen.blit(surface_load_cloud, rect_cloud)
    screen.blit(surface_plaza, rect_plaza)

    #text
    screen.blit(surface_title, rect_title)
    screen.blit(surface_play, rect_play)
    screen.blit(surface_exit, rect_exit)

    #Animation
    rect_cloud.x += 4
    if rect_cloud.right > width + 400: rect_cloud.left = -400

    pygame.display.update()
    clock.tick(60)



