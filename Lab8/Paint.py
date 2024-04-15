import pygame 
pygame.init() # Initialize pygame

painting = [] # Список для хранения нарисованных фигур.

timer = pygame.time.Clock() # We need it for future use with fps

fps = 60 # Set Frames per second

activeColor = (0, 0, 0)
activeShape = 0 #(0 для прямоугольника, 1  для круга)

w = 800 # Set Window Size
h = 600

screen = pygame.display.set_mode([w, h]) # Set Screen

pygame.display.set_caption("Paint") # Set Window Title

def drawDisplay():
    pygame.draw.rect(screen, 'gray', [0, 0, w, 100]) # Draw Display
    pygame.draw.line(screen, 'black', [0, 100], [w, 100]) # Draw Line separator 
    rect = [pygame.draw.rect(screen, 'black', [10, 10, 80, 80]), 0]# Номер [0] в данном контексте относится к индексу элемента в списке rect, который представляет кнопку для выбора формы прямоугольник
    pygame.draw.rect(screen, 'white', [20, 20, 60, 60])
    circ = [pygame.draw.rect(screen, 'black', [100, 10, 80, 80]), 1]
    pygame.draw.circle(screen, 'white', [140, 50], 30)
    blue = [pygame.draw.rect(screen, (0, 0, 255), [w - 35, 10, 25, 25]), (0, 0, 255)] # Draw colors
    red = [pygame.draw.rect(screen, (255, 0, 0), [w - 35, 35, 25, 25]), (255, 0, 0)] # Draw colors
    green = [pygame.draw.rect(screen, (0, 255, 0), [w - 60, 10, 25, 25]), (0, 255, 0)] # Draw colors
    yellow = [pygame.draw.rect(screen, (255, 255, 0), [w - 60, 35, 25, 25]), (255, 255, 0)] # Draw colors
    black = [pygame.draw.rect(screen, (0, 0, 0), [w - 85, 10, 25, 25]), (0, 0, 0)] # Draw colors
    purple = [pygame.draw.rect(screen, (255, 0, 255), [w - 85, 35, 25, 25]), (255, 0, 255)] # Draw colors
    eraser = [pygame.draw.rect(screen, (255, 255, 255), [w - 150, 20, 25, 25]), (255, 255, 255)] # Draw Eraser ластик
    return [blue, red, green, yellow, black, purple, eraser], [rect, circ]

def drawPaint(paints):
    for paint in paints: # представляет собой список элементов, содержащих информацию о том, что нужно нарисовать на экране
        if paint[2] == 1:
            pygame.draw.circle(screen, paint[0] , paint[1], 15) # Draw Paint
        elif paint[2] == 0:
            pygame.draw.rect(screen, paint[0], [paint[1][0]-15, paint[1][1]-15, 30, 30]) # Draw Paint
def draw():
    global activeColor, activeShape, mouse
    if mouse[1] > 100:
        if activeShape == 0:
            pygame.draw.rect(screen, activeColor, [mouse[0]-15, mouse[1]-15, 30, 30]) # Draw
        if activeShape == 1:
            pygame.draw.circle(screen, activeColor, mouse, 15)

run = True
while run:
    timer.tick(fps) # Устанавливаем FPS
    screen.fill('white') # Заполняем экран белым цветом

    colors, shape = drawDisplay() # Рисуем интерфейс выбора цвета и формы

    mouse = pygame.mouse.get_pos() # Получаем позицию мыши
    draw() # Рисуем выбранную форму, если мышь находится в области рисования
    
    click = pygame.mouse.get_pressed()[0] # Получаем информацию о нажатии левой кнопки мыши
    if click and mouse[1] > 100: # Если левая кнопка мыши нажата и мышь находится в области рисования
        painting.append((activeColor, mouse, activeShape)) # Добавляем текущую позицию мыши и выбранную форму в список для рисования

    drawPaint(painting) # Рисуем уже нарисованные фигуры

    for event in pygame.event.get(): # Обрабатываем события
        if event.type == pygame.QUIT: # Если событие - закрытие окна
            run = False # Завершаем программу

        if event.type == pygame.KEYDOWN: # Если нажата клавиша
            if event.key == pygame.K_ESCAPE: # Если нажата клавиша ESC
                run = False # Завершаем программу

            if event.key == pygame.K_SPACE: # Если нажата клавиша SPACE
                painting = [] # Очищаем список нарисованных фигур

        if event.type == pygame.MOUSEBUTTONDOWN: # Если произошло нажатие кнопки мыши
            for i in colors: # Проверяем каждый цвет
                if i[0].collidepoint(event.pos): # Если позиция клика попадает в область кнопки цвета
                    activeColor = i[1] # Устанавливаем выбранный цвет
            for i in shape: # Проверяем каждую форму
                if i[0].collidepoint(event.pos): # Если позиция клика попадает в область кнопки формы
                    activeShape = i[1] # Устанавливаем выбранную форму

    pygame.display.flip() # Обновляем экран