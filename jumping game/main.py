import pygame
import sys
import random

# Define constants
WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PURPLE = (128, 0, 128)
BLACK = (0, 0, 0)
GROUND_HEIGHT = 50
PLAYER_SIZE = 50
OBSTACLE_WIDTH = 50
OBSTACLE_HEIGHT = 50
JUMP_HEIGHT = 15
GRAVITY = 0.8
LIFE = 3
SCORE = 0

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Define classes
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((PLAYER_SIZE, PLAYER_SIZE))
        self.image.fill(PURPLE)
        self.rect = self.image.get_rect()
        self.rect.bottom = HEIGHT - GROUND_HEIGHT
        self.rect.left = WIDTH // 2
        self.vel_y = 0
        self.on_ground = True

    def update(self):
        # Apply gravity
        if not self.on_ground:
            self.vel_y += GRAVITY
        self.rect.y += self.vel_y

        # Check if player is on the ground
        if self.rect.bottom >= HEIGHT - GROUND_HEIGHT:
            self.rect.bottom = HEIGHT - GROUND_HEIGHT
            self.on_ground = True
            self.vel_y = 0

    def jump(self):
        if self.on_ground:
            self.vel_y = -JUMP_HEIGHT
            self.on_ground = False

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x):
        super().__init__()
        self.image = pygame.Surface((OBSTACLE_WIDTH, OBSTACLE_HEIGHT))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.bottom = HEIGHT - GROUND_HEIGHT
        self.rect.left = x
        self.speed = 5

    def update(self):
        self.rect.x -= self.speed

# Create sprite groups
all_sprites = pygame.sprite.Group()
obstacles = pygame.sprite.Group()

# Create player
player = Player()
all_sprites.add(player)

# Function to generate obstacles
def spawn_obstacle():
    x = WIDTH + random.randint(100, 300)  # Randomize x position
    obstacle = Obstacle(x)
    all_sprites.add(obstacle)
    obstacles.add(obstacle)

# Game loop
running = True
obstacle_timer = 0
obstacle_interval = random.randint(50,200)
collided_obstacle = set()
while running:
    collisions = pygame.sprite.spritecollide(player, obstacles, False)
    for obstacle in collisions:
        if obstacle not in collided_obstacle:
            LIFE -= 1
            collided_obstacle.add(obstacle)
            if LIFE <= 0:
                running = False
    for obstacle in obstacles:
        if obstacle.rect.right < player.rect.left and obstacle not in collided_obstacle:
            SCORE += 1
            collided_obstacle.add(obstacle)

    
    if pygame.time.get_ticks() % 1000 == 0:
        collided_obstacle.clear()

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.jump()

    # Update
    all_sprites.update()

    # Spawn obstacles
    obstacle_timer += 1
    if obstacle_timer >= obstacle_interval:
        spawn_obstacle()
        obstacle_timer = 0


    screen.fill(BLACK)
    pygame.font.init()
    font = pygame.font.SysFont('consolas', 40)  
    life_text = font.render(f"LIFE: {LIFE}", True, WHITE)
    score_text = font.render(f"SCORE: {SCORE}", True, WHITE)
    score_rect = score_text.get_rect(center=(WIDTH // 2, 10))
    life_rect = life_text.get_rect(center=(WIDTH // 2, 50))  
    screen.blit(life_text, life_rect)
    screen.blit(score_text, score_rect)
    # Draw
    all_sprites.draw(screen)
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

pygame.quit()
sys.exit()
