import pygame
import random

# Inicijalizacija Pygame
pygame.init()

# Velicina ekrana
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Kreiranje ekrana
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Ultimate Pac-Man Game')

# Postavljanje satnice
clock = pygame.time.Clock()

# Učitavanje zvučnih efekata
move_sound = pygame.mixer.Sound('move.wav')
hit_sound = pygame.mixer.Sound('hit.wav')
powerup_sound = pygame.mixer.Sound('powerup.wav')
game_over_sound = pygame.mixer.Sound('game_over.wav')

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('player.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH // 2
        self.rect.y = SCREEN_HEIGHT // 2
        self.speed = 5
        self.lives = 3
        self.score = 0

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
            move_sound.play()
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
            move_sound.play()
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
            move_sound.play()
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed
            move_sound.play()

        self.rect.x = max(0, min(SCREEN_WIDTH - self.rect.width, self.rect.x))
        self.rect.y = max(0, min(SCREEN_HEIGHT - self.rect.height, self.rect.y))

class SmartEnemy(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.image = pygame.image.load('enemy.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.speed = random.randint(2, 4)
        self.player = player

    def update(self):
        dx = self.player.rect.x - self.rect.x
        dy = self.player.rect.y - self.rect.y
        distance = (dx**2 + dy**2)**0.5

        if distance != 0:
            self.rect.x += int(dx / distance * self.speed)
            self.rect.y += int(dy / distance * self.speed)

class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.image.load('wall.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class PowerUp(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('powerup.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Scoreboard(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.font = pygame.font.SysFont('Arial', 25)

    def update(self, score):
        self.text = f'Score: {score}'
        self.image = self.font.render(self.text, True, (255, 255, 255))

player = Player()
smart_enemy_list = pygame.sprite.Group()
wall_list = pygame.sprite.Group()
powerup_list = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
scoreboard = Scoreboard()

# Dodavanje pametnih neprijatelja
for _ in range(5):
    smart_enemy = SmartEnemy(player)
    smart_enemy_list.add(smart_enemy)
    all_sprites.add(smart_enemy)

# Dodavanje zidova
wall_positions = [
    (200, 200, 400, 20),
    (200, 400, 400, 20),
    (200, 200, 20, 200),
    (580, 200, 20, 200),
    (300, 300, 200, 20)
]

for pos in wall_positions:
    wall = Wall(*pos)
    wall_list.add(wall)
    all_sprites.add(wall)

# Dodavanje power-up objekata
for _ in range(3):
    x = random.randint(50, SCREEN_WIDTH - 50)
    y = random.randint(50, SCREEN_HEIGHT - 50)
    powerup = PowerUp(x, y)
    powerup_list.add(powerup)
    all_sprites.add(powerup)

scoreboard.update(player.score)
all_sprites.add(player, scoreboard)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if pygame.sprite.spritecollide(player, wall_list, False):
        player.rect.x = SCREEN_WIDTH // 2
        player.rect.y = SCREEN_HEIGHT // 2
        player.lives -= 1
        hit_sound.play()

    if pygame.sprite.spritecollide(player, smart_enemy_list, False):
        player.rect.x = SCREEN_WIDTH // 2
        player.rect.y = SCREEN_HEIGHT // 2
        player.lives -= 1
        hit_sound.play()

    if pygame.sprite.spritecollide(player, powerup_list, True):
        player.score += 10
        scoreboard.update(player.score)
        powerup_sound.play()

    if player.lives <= 0:
        game_over_sound.play()
        running = False

    all_sprites.update()

    screen.fill((0, 0, 0))
    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
