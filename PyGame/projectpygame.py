import pygame 

pygame.init()

screen = pygame.display.set_mode((600,300)) #flags = pygame.NOFRAME
pygame.display.set_caption("ADAL PRODUCTION")
icon = pygame.image.load('C:\MyPythonProjects\TSIS\PyGame/files/icon.png')
pygame.display.set_icon(icon)

square = pygame.Surface((100 , 100))
square.fill('Red')

myfont = pygame.font.Font('C:\MyPythonProjects\TSIS\PyGame/files/Ewert-Regular.ttf' , 50)
text_surface = myfont.render('Adal',True , 'Black')

player = pygame.image.load('C:\MyPythonProjects\TSIS\PyGame/files/icon.png')

running =  True

while running :
    
    screen.fill((84, 172, 209))
    screen.blit(square , (0,0))
    screen.blit(player , (200,120))
    screen.blit(text_surface , (200,120))
    
    
    pygame.draw.circle(square  , 'Green' , (50, 50),30) #screen or square
    
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        """elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                screen.fill((84, 172, 209))
                """
            
                
            
    #https://colorpicker.me/#c83737
    #https://fonts.google.com/download/next-steps