import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Move the square")
clock = pygame.time.Clock()


class Player:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 50, 50)
        self.speed = 300
        self.colour = (100, 200, 255)

    def handle_input(self, keys, dt):
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed * dt
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed * dt
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed * dt
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed * dt

        self.rect.x = max(0, min(self.rect.x, 800 - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, 600 - self.rect.height))

    def draw(self, screen):
        pygame.draw.rect(screen, self.colour, self.rect)


player = Player(400, 300)
target = pygame.Rect(600, 100, 20, 20)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    dt = clock.tick(60) / 1000

    player.handle_input(keys, dt)

    if player.rect.colliderect(target):
        player.colour = (255, 0, 0)
    else:
        player.colour = (100, 200, 255)

    screen.fill((30, 30, 30))
    pygame.draw.rect(screen, (255, 80, 80), target)
    player.draw(screen)
    pygame.display.flip()

pygame.quit()