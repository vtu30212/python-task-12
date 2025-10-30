import pygame
import random

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 255, 0)

window_width = 600
window_height = 500
brick_width = 60
brick_height = 20

fps = 60

window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Breakout Game")

paddle = pygame.Rect(window_width // 2 - 50, window_height - 30, 100, 10)
paddle_speed = 7

ball = pygame.Rect(window_width // 2 - 10, window_height // 2 - 10, 20, 20)
ball_speed_x = 5 * random.choice((1, -1))
ball_speed_y = -5

brick_rows = 5
brick_columns = 10
bricks = []
for row in range(brick_rows):
    brick_row = []
    for col in range(brick_columns):
        brick = pygame.Rect(col * (brick_width + 10) + 35, row * (brick_height + 5) + 35, brick_width, brick_height)
        brick_row.append(brick)
    bricks.append(brick_row)

def draw_bricks():
    for row in bricks:
        for brick in row:
            pygame.draw.rect(window, blue, brick)

def move_ball():
    global ball_speed_x, ball_speed_y

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.left <= 0 or ball.right >= window_width:
        ball_speed_x *= -1
    if ball.top <= 0:
        ball_speed_y *= -1

    if ball.colliderect(paddle):
        ball_speed_y *= -1

    for row in bricks:
        for brick in row:
            if ball.colliderect(brick):
                row.remove(brick)
                ball_speed_y *= -1
                break

    if ball.bottom >= window_height:
        return False
    return True

def display_text(text, size, color, x, y):
    font = pygame.font.SysFont("comicsansms", size)
    text_surface = font.render(text, True, color)
    window.blit(text_surface, (x, y))

def breakout_game():
    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and paddle.left > 0:
            paddle.x -= paddle_speed
        if keys[pygame.K_RIGHT] and paddle.right < window_width:
            paddle.x += paddle_speed

        if not move_ball():
            display_text("Game Over!", 50, red, window_width // 2 - 130, window_height // 2)
            pygame.display.flip()
            pygame.time.delay(2000)
            running = False

        if all(len(row) == 0 for row in bricks):
            display_text("You Win!", 50, green, window_width // 2 - 130, window_height // 2)
            pygame.display.flip()
            pygame.time.delay(2000)
            running = False

        window.fill(black)

        pygame.draw.rect(window, white, paddle)
        pygame.draw.ellipse(window, red, ball)
        draw_bricks()

        pygame.display.update()
        clock.tick(fps)

    pygame.quit()

breakout_game()
