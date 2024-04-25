import pygame
import sys

# Inicijalizacija Pygame-a
pygame.init()

# Postavke prozora
WIDTH, HEIGHT = 800, 600
WINDOW_SIZE = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Belot Game")

# Postavke boja
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Funkcija za crtanje teksta na ekranu
def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_surface, text_rect)

# Klasa za prikaz karata
class CardSprite(pygame.sprite.Sprite):
    def __init__(self, card, x, y):
        super().__init__()
        self.card = card
        self.image = pygame.Surface((50, 70))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.font = pygame.font.Font(None, 36)

    def update(self):
        pygame.draw.rect(screen, BLACK, self.rect)
        draw_text(str(self.card.rank), self.font, WHITE, self.rect.x + 25, self.rect.y + 35)
        draw_text(self.card.suit, self.font, WHITE, self.rect.x + 25, self.rect.y + 55)

# Funkcija za glavnu petlju igre
def game_loop():
    deck = Deck()
    deck.shuffle()

    player1 = Player("Player 1")
    player2 = Player("Player 2")

    for _ in range(5):
        player1.add_card_to_hand(deck.deal())
        player2.add_card_to_hand(deck.deal())

    all_sprites = pygame.sprite.Group()

    for i, card in enumerate(player1.hand):
        card_sprite = CardSprite(card, i * 60, 400)
        all_sprites.add(card_sprite)

    for i, card in enumerate(player2.hand):
        card_sprite = CardSprite(card, i * 60, 100)
        all_sprites.add(card_sprite)

    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)

        all_sprites.update()
        all_sprites.draw(screen)

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    game_loop()
