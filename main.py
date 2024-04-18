import pygame
import random
from snake import Snake

# Initialize Pygame
pygame.init()

# Set up the screen
grid_width = 40
gird_height = 30
cell_size = 10

screen_width = grid_width * cell_size
screen_height = gird_height * cell_size


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
            if event.key == pygame.K_RIGHT and snake.dx != -cell_size:  
                snake.dx = cell_size
                snake.dy = 0
            elif event.key == pygame.K_LEFT and snake.dx != cell_size:  
                snake.dx = -cell_size
                snake.dy = 0
            elif event.key == pygame.K_UP and snake.dy != cell_size:  
                snake.dx = 0
                snake.dy = -cell_size
            elif event.key == pygame.K_DOWN and snake.dy != -cell_size:
                snake.dx = 0
                snake.dy = cell_size


    screen.fill(black)
    snake.move()
    green_color = (0, 255, 0)

    if snake.collision_with_food(food_pos):
        snake.add_element()
        food_pos = generate_food()

    if snake.collision_with_boundaries() or snake.collision_with_self():
        font = pygame.font.SysFont('consolas', 55)
        text = font.render(f"Game Over! Score: {snake.get_score()}", True, white)
        screen.blit(text, (screen_width // 2, screen_height // 2))
        pygame.display.update()
        pygame.time.wait(2000)
        pygame.quit()
        quit()

    pygame.draw.circle(screen, green_color, food_pos, 10,)
    snake.draw()

    pygame.display.update()
    clock.tick(15)
