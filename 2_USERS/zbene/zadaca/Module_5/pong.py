import pygame
import random

# Inicijalizacija Pygame
pygame.init()

# Boje
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
GRAY = (128, 128, 128)

# Velicina ekrana
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Kreiranje ekrana
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Advanced Pac-Man Game')

# Postavljanje satnice
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([20, 20])
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH // 2
        self.rect.y = SCREEN_HEIGHT // 2
        self.speed = 5
        self.lives = 3

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([20, 20])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - 20)
        self.rect.y = random.randint(0, SCREEN_HEIGHT - 20)
        self.speed = random.randint(2, 4)
        self.dx = self.speed
        self.dy = 0

    def update(self):
        self.rect.x += self.dx
        self.rect.y += self.dy

        if self.rect.left < 0 or self.rect.right > SCREEN_WIDTH:
            self.dx = -self.dx
        if self.rect.top < 0 or self.rect.bottom > SCREEN_HEIGHT:
            self.dy = -self.dy

class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(GRAY)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Scoreboard(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.font = pygame.font.SysFont('Arial', 25)

    def update(self):
        self.text = f'Score: {self.score}'
        self.image = self.font.render(self.text, True, WHITE)

player = Player()
enemy_list = pygame.sprite.Group()
wall_list = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
scoreboard = Scoreboard()

# Dodavanje neprijatelja
for _ in range(5):
    enemy = Enemy()
    enemy_list.add(enemy)
    all_sprites.add(enemy)

# Dodavanje zidova
wall = Wall(200, 200, 400, 20)
wall_list.add(wall)
all_sprites.add(wall)

scoreboard.update()
all_sprites.add(player, scoreboard)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Provera kolizije sa zidovima
    if pygame.sprite.spritecollide(player, wall_list, False):
        player.rect.x = SCREEN_WIDTH // 2
        player.rect.y = SCREEN_HEIGHT // 2
        player.lives -= 1

    # Provera kolizije sa neprijateljima
    if pygame.sprite.spritecollide(player, enemy_list, False):
        player.rect.x = SCREEN_WIDTH // 2
        player.rect.y = SCREEN_HEIGHT // 2
        player.lives -= 1

    # Provera života igrača
    if player.lives <= 0:
        running = False

    # Provera kolizije između neprijatelja
    for enemy in enemy_list:
        enemy_hit_list = pygame.sprite.spritecollide(enemy, wall_list, False)
        for wall in enemy_hit_list:
            if enemy.rect.x < wall.rect.x:
                enemy.rect.right = wall.rect.left
            elif enemy.rect.right > wall.rect.x:
                enemy.rect.left = wall.rect.right
            if enemy.rect.y < wall.rect.y:
                enemy.rect.bottom = wall.rect.top
            elif enemy.rect.bottom > wall.rect.y:
                enemy.rect.top = wall.rect.bottom

    # Ažuriranje svih sprite-ova
    all_sprites.update()

    # Crtanje svih sprite-ova
    screen.fill(WHITE)
    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
