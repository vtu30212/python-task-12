import pygame
import time
pygame.init()
WIDTH, HEIGHT = 540, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (128, 128, 128)
BLUE = (0, 0, 255)
font = pygame.font.SysFont("comicsans", 40)
small_font = pygame.font.SysFont("comicsans", 20)
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]
def draw_grid():
    gap = WIDTH // 9
    for i in range(10):
        if i % 3 == 0:
            thick = 4
        else:
            thick = 1
        pygame.draw.line(win, BLACK, (0, i * gap), (WIDTH, i * gap), thick)
        pygame.draw.line(win, BLACK, (i * gap, 0), (i * gap, WIDTH), thick)
def draw_numbers(board):
    gap = WIDTH // 9
    for i in range(9):
        for j in range(9):
            if board[i][j] != 0:
                text = font.render(str(board[i][j]), True, BLACK)
                win.blit(text, (j * gap + 15, i * gap + 15))
def draw_selected(row, col):
    gap = WIDTH // 9
    pygame.draw.rect(win, BLUE, (col * gap, row * gap, gap, gap), 4)
def main():
    key = None
    row = -1
    col = -1
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    key = 1
                if event.key == pygame.K_2:
                    key = 2
                if event.key == pygame.K_3:
                    key = 3
                if event.key == pygame.K_4:
                    key = 4
                if event.key == pygame.K_5:
                    key = 5
                if event.key == pygame.K_6:
                    key = 6
                if event.key == pygame.K_7:
                    key = 7
                if event.key == pygame.K_8:
                    key = 8
                if event.key == pygame.K_9:
                    key = 9
                if event.key == pygame.K_DELETE:
                    board[row][col] = 0
                    key = None
                if event.key == pygame.K_RETURN:
                    key = None
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row = pos[1] // (WIDTH // 9)
                col = pos[0] // (WIDTH // 9)
        win.fill(WHITE)
        draw_grid()
        draw_numbers(board)
        if row >= 0 and col >= 0:
            draw_selected(row, col)
        if key is not None and row >= 0 and col >= 0:
            board[row][col] = key
        pygame.display.update()
main()
pygame.quit()
