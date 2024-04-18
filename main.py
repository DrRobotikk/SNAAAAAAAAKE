import pygame
import random
from snake import Snake

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)



def generate_food():
    return [random.randrange(1, (screen_width // 10)) * 10, random.randrange(1, (screen_height // 10)) * 10]


food_pos = generate_food()
snake = Snake()
snake.set_hight_and_width(screen_width, screen_height)
snake.set_screen(screen)
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and snake.dx != -10:  # Prevent going left if moving right
                snake.dx = 10
                snake.dy = 0
            elif event.key == pygame.K_LEFT and snake.dx != 10:  # Prevent going right if moving left
                snake.dx = -10
                snake.dy = 0
            elif event.key == pygame.K_UP and snake.dy != 10:  # Prevent going down if moving up
                snake.dx = 0
                snake.dy = -10
            elif event.key == pygame.K_DOWN and snake.dy != -10:  # Prevent going up if moving down
                snake.dx = 0
                snake.dy = 10


    screen.fill(black)
    snake.move()

    if snake.collision_with_food(food_pos):
        snake.add_element()
        food_pos = generate_food()

    if snake.collision_with_boundaries() or snake.collision_with_self():
        font = pygame.font.SysFont(None, 55)
        text = font.render(f"Game Over! Score: {snake.get_score()}", True, white)
        screen.blit(text, (screen_width // 6, screen_height // 3))
        pygame.display.update()
        pygame.time.wait(3000)
        pygame.quit()
        quit()

    pygame.draw.circle(screen, (255, 0, 0), food_pos, 10)
    snake.draw()

    pygame.display.update()
    clock.tick(20)
