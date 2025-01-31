import pygame
from sys import exit

def display_score():
    global current_time
    current_time = int(pygame.time.get_ticks() / 1000) - star_time
    score_surface = font.render(f'{current_time}',False,(64,64,64))
    score_rect = score_surface.get_rect(center = (400,50))
    screen.blit(score_surface,rect_score)


pygame.init()
#Screen
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Menu")
clock = pygame.time.Clock()
#Font
font = pygame.font.Font('font/Pixeltype.ttf',50)
#Layers background
surface_sky = pygame.image.load('graphics/Sky.png').convert_alpha()
surface_ground = pygame.image.load('graphics/ground.png').convert_alpha()

#Score
surface_text = font.render('ALIENPETROCOMUNIST', False, 'White')
surface_text2 = font.render('Press space to revolution', False, 'White')
rect_text2 = surface_text2.get_rect(center = (400,350))
rect_text = surface_text.get_rect(center = (400,50))
rect_score = surface_text.get_rect(center = (550,50))

#Snail
surface_snail = pygame.image.load('graphics\snail\snail1.png').convert_alpha()
rect_snail = surface_snail.get_rect(bottomright = (600,300))

#Player
surface_player = pygame.image.load('graphics\Player\player_walk_1.png').convert_alpha()
rect_player = surface_player.get_rect(midbottom = (80,300))


surface_game_load = pygame.image.load('graphics/Player/player_stand.png').convert_alpha()
surface_game_over = pygame.transform.rotozoom(surface_game_load, 0,2)
rect_player_over = surface_game_over.get_rect(center = (400,200))





rect_player_menu = surface_player.get_rect(midbottom = (400,200))

#gravity
player_gravity = 0
star_time = 0
score = 0

#switches
game_active = False

while True:

    for event in pygame.event.get(): # Event in pygame.event search in all of them (types of events)
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and  rect_player.bottom >= 300:
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    game_active = True
                    rect_snail.left = 800
                    star_time = int(pygame.time.get_ticks()/1000)
                
    
    if game_active:
        
    
        screen.blit(surface_sky,(0,0))
        screen.blit(surface_ground,(0,300))

        display_score()
        score = current_time
        #snail
        rect_snail.x -= 6
        if rect_snail.right <= 0: rect_snail.left = 800
        screen.blit(surface_snail, rect_snail)
        if rect_snail.colliderect(rect_player): game_active = False

        #player
        player_gravity += 1
        rect_player.y += player_gravity
        if rect_player.bottom >= 300:
            rect_player.bottom = 300
        screen.blit(surface_player, rect_player)
    else:
        screen.fill("Black")
        screen.blit(surface_game_over,rect_player_over)

        score_message = font.render(f'Your score: {score}', False,'White')
        score_rectmessage = score_message.get_rect(center = (400,350))
        screen.blit(surface_text, rect_text)
        if score == 0:
            screen.blit(surface_text2,rect_text2)
        else:
            screen.blit(score_message,score_rectmessage)
    
    pygame.display.update()
    clock.tick(60)


