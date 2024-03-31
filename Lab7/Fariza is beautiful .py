import pygame
import random

# Инициализация Pygame
pygame.init()

# Определение размеров экрана
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Определение цветов
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Определение размеров блока змейки и еды
BLOCK_SIZE = 20

# Создание окна
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Змейка")

# Функция отрисовки змейки и еды
def draw_block(color, x, y):
    pygame.draw.rect(screen, color, (x, y, BLOCK_SIZE, BLOCK_SIZE))

# Основная функция игры
def game():
    # Начальные координаты змейки
    snake = [[100, 50], [90, 50], [80, 50]]
    # Начальное направление движения
    direction = "RIGHT"
    # Координаты еды
    food_pos = [random.randrange(1, (SCREEN_WIDTH//BLOCK_SIZE)) * BLOCK_SIZE,
                random.randrange(1, (SCREEN_HEIGHT//BLOCK_SIZE)) * BLOCK_SIZE]
    # Счет
    score = 0

    # Основной цикл игры
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direction = "LEFT"
                elif event.key == pygame.K_RIGHT:
                    direction = "RIGHT"
                elif event.key == pygame.K_UP:
                    direction = "UP"
                elif event.key == pygame.K_DOWN:
                    direction = "DOWN"

        # Изменение координат змейки в зависимости от направления
        if direction == "RIGHT":
            snake[0][0] += BLOCK_SIZE
        elif direction == "LEFT":
            snake[0][0] -= BLOCK_SIZE
        elif direction == "UP":
            snake[0][1] -= BLOCK_SIZE
        elif direction == "DOWN":
            snake[0][1] += BLOCK_SIZE

        # Проверка на столкновение с краями экрана
        if (snake[0][0] >= SCREEN_WIDTH or snake[0][0] < 0 or
                snake[0][1] >= SCREEN_HEIGHT or snake[0][1] < 0):
            game()

        # Проверка на столкновение с собой
        for block in snake[1:]:
            if snake[0][0] == block[0] and snake[0][1] == block[1]:
                game()

        # Проверка на поедание еды
        if snake[0][0] == food_pos[0] and snake[0][1] == food_pos[1]:
            snake.append([food_pos[0], food_pos[1]])
            food_pos = [random.randrange(1, (SCREEN_WIDTH//BLOCK_SIZE)) * BLOCK_SIZE,
                        random.randrange(1, (SCREEN_HEIGHT//BLOCK_SIZE)) * BLOCK_SIZE]
            score += 1

        screen.fill(WHITE)

        # Отрисовка змейки
        for segment in snake:
            draw_block(GREEN, segment[0], segment[1])

        # Отрисовка еды
        draw_block(RED, food_pos[0], food_pos[1])

        # Отображение счета
        font = pygame.font.SysFont(None, 25)
        text = font.render("Счет: " + str(score), True, "BLACK")
        screen.blit(text, [0, 0])

        # Обновление экрана
        pygame.display.update()

        # Установка скорости игры
        pygame.time.Clock().tick(10)

# Запуск игры
game()
