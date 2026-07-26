import pygame
import random
import math

# Game Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYER_SPEED = 5
BULLET_SPEED = 7
ENEMY_SPEED = 2
ENEMY_SIZE = 40
BULLET_SIZE = 10
POWERUP_SIZE = 30
SHOOT_COOLDOWN = 1500  # Time in milliseconds between shots (1.5 seconds)
WALL_SIZE = 60  # Size of the wall block

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)  # Soda (Speed Boost)
ORANGE = (255, 165, 0)  # Gun (Bullet Speed)
PURPLE = (128, 0, 128)  # Ball of Death (Game Speed)
BROWN = (139, 69, 19)  # Wall color

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("2D Shooter Game with Power-Ups")

# Clock to control frame rate
clock = pygame.time.Clock()

# Player class
class Player:
    def __init__(self):
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT - 50
        self.width = 50
        self.height = 50
        self.color = BLUE
        self.speed = PLAYER_SPEED
        self.bullet_speed = BULLET_SPEED
        self.speed_count = 0  # Tracks how many "soda" power-ups the player has
        self.bullet_speed_count = 0  # Tracks how many "gun" power-ups the player has
        self.game_speed_count = 0  # Tracks how many "ball_of_death" power-ups the player has
        self.last_shot_time = 0  # Tracks the time of the last shot

    def move(self, keys, walls):
        # Move player while checking collisions with walls
        new_x = self.x
        new_y = self.y

        if keys[pygame.K_LEFT]:
            new_x -= self.speed
        if keys[pygame.K_RIGHT]:
            new_x += self.speed
        if keys[pygame.K_UP]:
            new_y -= self.speed
        if keys[pygame.K_DOWN]:
            new_y += self.speed

        # Check collision with walls before updating position
        if not self.check_collision_with_walls(new_x, new_y, walls):
            self.x = new_x
            self.y = new_y

    def render(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def can_shoot(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_shot_time >= SHOOT_COOLDOWN:
            self.last_shot_time = current_time
            return True
        return False

    def check_collision_with_walls(self, new_x, new_y, walls):
        for wall in walls:
            if (new_x < wall.x + wall.width and new_x + self.width > wall.x and
                new_y < wall.y + wall.height and new_y + self.height > wall.y):
                return True  # Collision with a wall
        return False

    def activate_power_up(self, power_up):
        global ENEMY_SPEED, BULLET_SPEED  # Declare these variables as global
        if power_up.type == 'soda':
            self.speed_count += 1  # Increase speed count for soda power-ups
            self.speed = PLAYER_SPEED + self.speed_count * 2  # Increase speed based on stack count
        elif power_up.type == 'gun':
            self.bullet_speed_count += 1  # Increase bullet speed count
            self.bullet_speed = BULLET_SPEED + self.bullet_speed_count * 3  # Increase bullet speed based on stack count
        elif power_up.type == 'ball_of_death':
            self.game_speed_count += 1  # Increase game speed count
            ENEMY_SPEED = 2 + self.game_speed_count  # Increase enemy speed
            BULLET_SPEED = 7 + self.game_speed_count * 2  # Increase bullet speed

# Bullet class
class Bullet:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.width = BULLET_SIZE
        self.height = BULLET_SIZE
        self.color = WHITE
        self.speed = speed

    def move(self):
        self.y -= self.speed

    def render(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

# Enemy class
class Enemy:
    def __init__(self):
        self.x = random.randint(0, SCREEN_WIDTH - ENEMY_SIZE)
        self.y = -ENEMY_SIZE
        self.width = ENEMY_SIZE
        self.height = ENEMY_SIZE
        self.color = RED
        self.speed = ENEMY_SPEED

    def move(self, player):
        # Move towards the player
        angle = math.atan2(player.y - self.y, player.x - self.x)
        self.x += math.cos(angle) * self.speed
        self.y += math.sin(angle) * self.speed

    def render(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

# PowerUp class
class PowerUp:
    def __init__(self, power_up_type):
        self.x = random.randint(50, SCREEN_WIDTH - POWERUP_SIZE - 50)  # Random X position within bounds
        self.y = -POWERUP_SIZE  # Start above the screen to fall down
        self.width = POWERUP_SIZE
        self.height = POWERUP_SIZE
        self.type = power_up_type  # 'soda', 'gun', or 'ball_of_death'
        self.speed = random.randint(2, 5)  # Random falling speed for each power-up
        
        if power_up_type == 'soda':
            self.color = YELLOW
        elif power_up_type == 'gun':
            self.color = ORANGE
        elif power_up_type == 'ball_of_death':
            self.color = PURPLE

    def move(self):
        self.y += self.speed  # Move the power-up down the screen

    def render(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

# Wall class (Moving wall)
class Wall:
    def __init__(self):
        self.x = random.randint(50, SCREEN_WIDTH - WALL_SIZE - 50)  # Random X position
        self.y = -WALL_SIZE  # Start at the top of the screen
        self.width = WALL_SIZE
        self.height = WALL_SIZE
        self.color = BROWN
        self.speed = random.randint(2, 4)  # Random downward speed

    def move(self):
        self.y += self.speed  # Move the wall downward

    def render(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

# Main Game Loop
def main():
    global ENEMY_SPEED, BULLET_SPEED  # Declare these as global
    player = Player()
    bullets = []
    enemies = []
    power_ups = []
    walls = [Wall() for _ in range(3)]  # Create some moving walls
    running = True
    score = 0
    last_power_up_time = pygame.time.get_ticks()

    while running:
        screen.fill(BLACK)
        keys = pygame.key.get_pressed()

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player.can_shoot():
                    # Create a new bullet
                    bullet = Bullet(player.x + player.width // 2 - BULLET_SIZE // 2, player.y, player.bullet_speed)
                    bullets.append(bullet)

        # Spawn power-ups periodically
        if pygame.time.get_ticks() - last_power_up_time > 10000:  # Every 10 seconds
            last_power_up_time = pygame.time.get_ticks()
            power_up_type = random.choice(['soda', 'gun', 'ball_of_death'])
            power_up = PowerUp(power_up_type)
            power_ups.append(power_up)

        # Power-Up collisions
        for power_up in power_ups[:]:
            if (player.x < power_up.x + power_up.width and player.x + player.width > power_up.x and
                player.y < power_up.y + power_up.height and player.y + player.height > power_up.y):
                player.activate_power_up(power_up)
                power_ups.remove(power_up)

        # Player movement
        player.move(keys, walls)

        # Update and render bullets
        for bullet in bullets[:]:
            bullet.move()
            if bullet.y < 0:  # Remove off-screen bullets
                bullets.remove(bullet)
            bullet.render(screen)

        # Spawn enemies randomly
        if random.random() < 0.02:
            enemies.append(Enemy())

        # Update and render enemies
        for enemy in enemies[:]:
            enemy.move(player)  # Enemies move towards the player
            if enemy.y > SCREEN_HEIGHT:  # Remove enemies that go off screen
                enemies.remove(enemy)
            enemy.render(screen)

        # Update and render power-ups
        for power_up in power_ups[:]:
            power_up.move()
            if power_up.y > SCREEN_HEIGHT:  # Remove power-ups that go off the screen
                power_ups.remove(power_up)
            power_up.render(screen)

        # Update and render walls (moving obstacles)
        for wall in walls[:]:
            wall.move()
            if wall.y > SCREEN_HEIGHT:  # Remove walls that go off the screen
                walls.remove(wall)
                walls.append(Wall())  # Add a new wall
            wall.render(screen)

        # Collision detection for bullets and enemies
        for bullet in bullets[:]:
            for enemy in enemies[:]:
                if (bullet.x < enemy.x + enemy.width and bullet.x + bullet.width > enemy.x and
                        bullet.y < enemy.y + enemy.height and bullet.y + bullet.height > enemy.y):
                    # Bullet hit enemy, remove both
                    bullets.remove(bullet)
                    enemies.remove(enemy)
                    score += 1
                    break

        # Check if any enemy hits the player
        for enemy in enemies:
            if (player.x < enemy.x + enemy.width and player.x + player.width > enemy.x and
                    player.y < enemy.y + enemy.height and player.y + player.height > enemy.y):
                print(f"Game Over! Final Score: {score}")
                running = False
                break

        # Check if player collides with any wall
        for wall in walls:
            if (player.x < wall.x + wall.width and player.x + player.width > wall.x and
                    player.y < wall.y + wall.height and player.y + player.height > wall.y):
                print(f"Game Over! Final Score: {score}")
                running = False
                break

        # Render player
        player.render(screen)

        # Display score
        font = pygame.font.SysFont(None, 36)
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(60)  # 60 FPS

    pygame.quit()

if __name__ == "__main__":
    main()
