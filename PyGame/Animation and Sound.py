import pygame 

clock = pygame.time.Clock()
pygame.init()

screen = pygame.display.set_mode((1056,594))
pygame.display.set_caption("Adventure")

pygame.display.set_icon(pygame.image.load('C:\MyPythonProjects\TSIS\PyGame/files/icon.png'))

bg = pygame.image.load('C:\MyPythonProjects\TSIS\PyGame/files/bg.png')
player = pygame.image.load('C:\MyPythonProjects\TSIS\PyGame/files/1.png')

bear = pygame.image.load('C:\MyPythonProjects\TSIS\PyGame/files/Mushroom-icon.png')
bear_x = 1058
walk_right = [
    pygame.image.load('C:\MyPythonProjects\TSIS\PyGame/files/1.png'),
    pygame.image.load('C:\MyPythonProjects\TSIS\PyGame/files/2.png'),
    pygame.image.load('C:\MyPythonProjects\TSIS\PyGame/files/3.png'),
    pygame.image.load('C:\MyPythonProjects\TSIS\PyGame/files/4.png'),
]

walk_left = [
    pygame.image.load('C:\MyPythonProjects\TSIS\PyGame/files/1l.png'),
    pygame.image.load('C:\MyPythonProjects\TSIS\PyGame/files/2l.png'),
    pygame.image.load('C:\MyPythonProjects\TSIS\PyGame/files/3l.png'),
    pygame.image.load('C:\MyPythonProjects\TSIS\PyGame/files/4l.png'),
]

player_anim_count = 0
bg_x = 0

player_speed = 5
player_x = 200
player_y = 400

is_jump = False
jump_count = 7

bg_sound = pygame.mixer.Sound('C:\MyPythonProjects\TSIS\PyGame/files/song.mp3')
bg_sound.play()
 
running = True   
while running :
    screen.blit(bg,(bg_x,0))
    screen.blit(bg,(bg_x + 800 ,0))
    screen.blit(bear,(bear_x,420))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
     screen.blit(walk_left[player_anim_count],(player_x,player_y))
    else:
     screen.blit(walk_right[player_anim_count],(player_x,player_y))
     
    if keys[pygame.K_LEFT] and player_x > 50:
        player_x -= player_speed
    elif keys[pygame.K_RIGHT] and player_x < 980 :
        player_x += player_speed
        
    if not  is_jump:
        if keys[pygame.K_SPACE]:
            is_jump = True
    else:
        if jump_count >= - 7:
            if jump_count > 0:
                player_y -= (jump_count ** 2) / 2
            else:
                player_y += (jump_count ** 2) / 2
            jump_count -=1
        else:
            is_jump = False 
            jump_count = 7
            
    if player_anim_count == 3:
        player_anim_count =0
    else:
        player_anim_count +=1
        
    bg_x -= 2
    if bg_x == -800:
        bg_x = 0
    
    bear_x -=10
    pygame.display.update()
    
    clock.tick(8) # the number of frams in second
    
    for event in pygame.event.get():
     if event.type == pygame.QUIT:
        running = False 
        pygame.quit(
            
        )
        
        
        
        #spritesheet