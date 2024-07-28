import pygame
import sys
import random

# Initializing Pygame
pygame.init()

# Setting up the game window
width, height = 800, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Dino Run")

# Setting up colors
white = (255, 255, 255)
black = (0, 0, 0)

# Setting up the dinosaur
dino_size = 25
dino_x = width // 2
dino_y = height - dino_size
dino_velocity = 0
gravity = 1
jump_height = -12
is_jumping = False

# Setting up the ground
ground_height = 20

# Setting up the obstacles (cacti)
obstacle_size = 30
obstacle_velocity = 10
obstacle_frequency = 30
min_distance_between_obstacles = 125
obstacles = []

# Setting up the game clock
clock = pygame.time.Clock()

def draw_obstacles():
    for obstacle in obstacles:
        pygame.draw.rect(screen, (0, 255, 0), obstacle)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not is_jumping:
                dino_velocity = jump_height
                is_jumping = True

    # Generate random obstacles
    if random.randrange(0, obstacle_frequency) == 1:
        if not obstacles or width - obstacles[-1].x > min_distance_between_obstacles:
            obstacle_x = width
            obstacle_y = height - ground_height - obstacle_size
            obstacles.append(pygame.Rect(obstacle_x, obstacle_y, obstacle_size, obstacle_size))

    # Updating dinosaur position and velocity
    dino_y += dino_velocity
    dino_velocity += gravity

    # Checking for ground collision
    if dino_y > height - dino_size - ground_height:
        dino_y = height - dino_size - ground_height
        is_jumping = False

    # Updating obstacle positions
    for obstacle in obstacles:
        obstacle.x -= obstacle_velocity

    # Removing obstacles that are off the screen
    obstacles = [obstacle for obstacle in obstacles if obstacle.x + obstacle.width > 0]

    # Checking for collisions with obstacles
    for obstacle in obstacles:
        if obstacle.colliderect(pygame.Rect(dino_x, dino_y, dino_size, dino_size)):
            print("Game Over!")
            pygame.quit()
            sys.exit()

    # Clear screen
    screen.fill(white)

    # Ground
    pygame.draw.rect(screen, black, (0, height - ground_height, width, ground_height))

    # Dinosaur
    pygame.draw.rect(screen, (255, 0, 0), (dino_x, dino_y, dino_size, dino_size))

    # Obstacles
    draw_obstacles()

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(30)
