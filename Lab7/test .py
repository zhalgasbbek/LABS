import pygame

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((500, 500))  # Измените размер экрана на 500x500
pygame.display.set_caption("ADAL PRODUCTION")
icon = pygame.image.load('C:/MyPythonProjects/TSIS/PyGame/files/icon.png')
pygame.display.set_icon(icon)

ball_x = 500 // 2
ball_y = 500 // 2

running = True
while running:
    screen.fill('White')

    pygame.draw.circle(screen, 'Red', (ball_x, ball_y), 25)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_UP] and y-25>0:
        y -= 20
    if pressed_keys[pygame.K_DOWN] and y+25<800:
        y += 20
    if pressed_keys[pygame.K_LEFT] and x-25>0:
        x -= 20
    if pressed_keys[pygame.K_RIGHT] and x+25<800:
        x += 20
clock.tick(120)