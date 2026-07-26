import pygame

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)

# Create Game Window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Class-Based Pygame")

# Player Class
class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 50
        self.color = (165, 255, 35)
        self.speed = 15

    def move(self, keys):
        if keys[pygame.K_LEFT]:  # Move left
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:  # Move right
            self.x += self.speed
        if keys[pygame.K_UP]:  # Move up
            self.y -= self.speed
        if keys[pygame.K_DOWN]:  # Move down
            self.y += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

# Game Loop
player = Player(375, 275)
running = True
while running:
    pygame.time.delay(30)  # Slow down loop

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    player.move(keys)

    screen.fill(WHITE)
    player.draw(screen)
    pygame.display.update()

pygame.quit()
