import pygame
import random

class Player:
    def __init__(self, x, y, size, speed, screen_width):
        self.x = x
        self.y = y
        self.size = size
        self.speed = speed
        self.screen_width = screen_width
        self.rect = pygame.Rect(self.x, self.y, size, size)

    def move(self, dt):
        keys = pygame.key.get_pressed()
        dx = 0

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            dx -= self.speed * dt
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            dx += self.speed * dt

        self.x += dx

        if self.x < 0:
            self.x = 0
        if self.x + self.size > self.screen_width:
            self.x = self.screen_width - self.size

        self.rect.topleft = (int(self.x), int(self.y))

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 192, 203), self.rect)


class Enemy:
    def __init__(self, x, y, size, speed, screen_height):
        self.x = x
        self.y = y
        self.size = size
        self.speed = speed
        self.screen_height = screen_height
        self.rect = pygame.Rect(self.x, self.y, size, size)

    def update(self, dt):
        self.y += self.speed * dt
        self.rect.topleft = (int(self.x), int(self.y))

    def off_screen(self):
        return self.y > self.screen_height

    def draw(self, surface):
        pygame.draw.rect(surface, (200, 50, 50), self.rect)

class Game:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height

        self.bg_color = (67, 67, 67)

        self.player = Player(width // 2 - 15, height - 80, 30, 400, width)

        self.enemies = []
        self.spawn_timer = 0.0
        self.spawn_interval = 1.0

        self.score = 0
        self.level = 1

        self.font = pygame.font.Font(None, 36)
        self.game_over = False

    def reset(self):
        self.player = Player(self.width // 2 - 15, self.height - 80,
                             30, 400, self.width)
        self.enemies = []
        self.spawn_timer = 0.0
        self.spawn_interval = 1.0
        self.score = 0
        self.level = 1
        self.game_over = False

    def update(self, dt):
        if self.game_over:
            return

        self.player.move(dt)

        self.spawn_timer += dt
        if self.spawn_timer >= self.spawn_interval:
            self.spawn_timer -= self.spawn_interval
            self.spawn_enemy()

        for enemy in list(self.enemies):
            enemy.update(dt)

            if enemy.off_screen():
                self.enemies.remove(enemy)
                self.score += 1

                if self.score % 10 == 0:
                    self.level += 1
                    self.spawn_interval = max(0.25, self.spawn_interval - 0.08)

        for enemy in self.enemies:
            if enemy.rect.colliderect(self.player.rect):
                self.game_over = True

    def spawn_enemy(self):
        size = random.randint(20, 50)
        x = random.randint(0, self.width - size)
        y = -size

        base_speed = 120
        speed = base_speed + random.random() * 80 + (self.level - 1) * 20

        self.enemies.append(Enemy(x, y, size, speed, self.height))

    def draw(self):
        self.screen.fill(self.bg_color)

        self.player.draw(self.screen)

        for enemy in self.enemies:
            enemy.draw(self.screen)

        score = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        level = self.font.render(f"Level: {self.level}", True, (255, 255, 255))

        self.screen.blit(score, (10, 10))
        self.screen.blit(level, (10, 40))

        if self.game_over:
            over_font = pygame.font.Font(None, 72)
            over_text = over_font.render("Game Over", True, (255, 150, 150))

            sub = self.font.render("Press R to restart",
                                   True, (220, 220, 220))

            self.screen.blit(over_text,
                             (self.width // 2 - over_text.get_width() // 2,
                              self.height // 2 - 60))

            self.screen.blit(sub,
                             (self.width // 2 - sub.get_width() // 2,
                              self.height // 2 + 20))

def main():
    pygame.init()
    width = 600
    height = 800
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Dodge the Blocks — Mini game")

    clock = pygame.time.Clock()
    game = Game(screen, width, height)

    font = pygame.font.Font(None, 48)
    small = pygame.font.Font(None, 28)

    show_menu = True

    while True:
        if show_menu:
            screen.fill((30, 30, 30))
            title = font.render("Dodge the Blocks", True, (255, 255, 255))
            hint = small.render("Press SPACE to start, ESC to quit",
                                True, (200, 200, 200))

            screen.blit(title, (width // 2 - title.get_width() // 2,
                                height // 2 - 80))
            screen.blit(hint, (width // 2 - hint.get_width() // 2,
                               height // 2))
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        show_menu = False
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        return

            clock.tick(60)
            continue

        dt = clock.tick(60) / 1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return

                if event.key == pygame.K_r and game.game_over:
                    game.reset()

        game.update(dt)
        game.draw()
        pygame.display.flip()


if __name__ == "__main__":
    main()

