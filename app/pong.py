import pygame, sys, random

pygame.mixer.init()
pong_sound = pygame.mixer.Sound(f'assets/music/pickupCoin.wav')

def pong():
    pygame.init()

    WIDTH, HEIGHT = 1280, 700

    FONT = pygame.font.SysFont("Consolas", int(WIDTH / 20))

    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pong")

    CLOCK = pygame.time.Clock()

    # Paddles

    player = pygame.Rect(0, 0, 15, 100)
    player.center = (WIDTH - 100, HEIGHT / 2)

    opponent = pygame.Rect(0, 0, 15, 100)
    opponent.center = (100, HEIGHT / 2)

    player_score, opponent_score = 0, 0

    # Ball

    ball = pygame.Rect(0, 0, 20, 20)
    ball.center = (WIDTH / 2, HEIGHT / 2)

    x_speed, y_speed = 1, 1

    while True:
        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_UP]:
            if player.top > 0:
                player.top -= 2
        if keys_pressed[pygame.K_DOWN]:
            if player.bottom < HEIGHT:
                player.bottom += 2

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # pygame.quit()
                sys.exit()

        if ball.y >= HEIGHT:
            y_speed = -1
        if ball.y <= 0:
            y_speed = 1
        if ball.x <= 0:
            player_score += 1
            ball.center = (WIDTH / 2, HEIGHT / 2)
            x_speed, y_speed = random.choice([1, -1]), random.choice([1, -1])
        if ball.x >= WIDTH:
            opponent_score += 1
            ball.center = (WIDTH / 2, HEIGHT / 2)
            x_speed, y_speed = random.choice([1, -1]), random.choice([1, -1])
        if player.x - ball.width <= ball.x <= player.right and ball.y in range(player.top - ball.width,
                                                                               player.bottom + ball.width):
            x_speed = -1
            pong_sound.play()

        if opponent.x - ball.width <= ball.x <= opponent.right and ball.y in range(opponent.top - ball.width,
                                                                                   opponent.bottom + ball.width):
            x_speed = 1
            pong_sound.play()

        player_score_text = FONT.render(str(player_score), True, "#E9C46A")
        opponent_score_text = FONT.render(str(opponent_score), True, "#E9C46A")
        separator_score_text = FONT.render(str(":"), True, "#E9C46A")

        if opponent.y < ball.y:
            opponent.top += 1.5
        if opponent.bottom > ball.y:
            opponent.bottom -= 1.5

        ball.x += x_speed * 2
        ball.y += y_speed * 2

        SCREEN.fill("#264653")

        pygame.draw.rect(SCREEN, "#E9C46A", player)
        pygame.draw.rect(SCREEN, "#E9C46A", opponent)
        pygame.draw.circle(SCREEN, "#E76F51", ball.center, 10)

        SCREEN.blit(player_score_text, (WIDTH / 2 + 50, 50))
        SCREEN.blit(separator_score_text, (WIDTH / 2, 50))
        SCREEN.blit(opponent_score_text, (WIDTH / 2 - 50, 50))

        pygame.display.update()
        CLOCK.tick(300)


if __name__ == "__main__":
    pong()