import pygame
import math

pygame.init()

BLACK = (0, 0, 0)
pi = 3.14

size = width, height = (1050, 750)
screen = pygame.display.set_mode(size)

# title
pygame.display.set_caption('TSIS7 IBRAGIM DANA')

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill((255, 255, 255))
    for i in range(7):
        x = 100 + i * 900 / 6
        # lines
        pygame.draw.line(screen, BLACK, (x, 50 - 25), (x, 650 + 25), 1)

        # short lines
        pygame.draw.line(screen, BLACK, (x + 900 / 12, 25), (x + 900 / 12, 40), 1)
        pygame.draw.line(screen, BLACK, (x + 900 / 12, 675 - 15), (x + 900 / 12, 675), 1)
    for i in range(14):
        # x meanings
        x = 100 + i * 900 / 6 / 2
        font = pygame.font.Font(None, 25)
        a = -3 + i * 1 / 2
        text = font.render(str(a) + "п", True, (0, 0, 0))
        screen.blit(text, (x - 20, 680))

    for i in range(9):
        y = 50 + i * 600 / 8
        # lines
        pygame.draw.line(screen, BLACK, (100 - 25, y), (1000 + 25, y), 1)

        # short lines
        if i < 8:
            pygame.draw.line(screen, BLACK, (100 - 25, y + 600 / 16), (100 - 10, y + 600 / 16), 1)
            pygame.draw.line(screen, BLACK, (1025 - 15, y + 600 / 16), (1025, y + 600 / 16), 1)

        # y meanings
        font = pygame.font.Font(None, 25)
        a = 1.00 - i * 0.25
        text = font.render(str(a), True, (0, 0, 0))
        screen.blit(text, (20, y - 10))
    # rectangle and x and y axes
    pygame.draw.rect(screen, BLACK, (100 - 25, 50 - 25, 950, 650), 3)
    pygame.draw.line(screen, BLACK, (100 - 25, 350), (1000 + 25, 350), 3)
    pygame.draw.line(screen, BLACK, (550, 50 - 25), (550, 650 + 25), 3)

    # cos and sin lines
    for x in range(100, 1000, 3):
        cos_y1 = 300 * math.cos((x - 100) / 100 * 3.14 / 1.5)
        cos_y2 = 300 * math.cos((x - 99) / 100 * 3.14 / 1.5)
        pygame.draw.aalines(screen, (0, 0, 255), False, [(x, 350 + cos_y1), ((x + 1), 350 + cos_y2)], 2)
    for x in range(100, 1000):
        sin_y1 = 300 * math.sin((x - 100) / 100 * 3.14 / 1.5)
        sin_y2 = 300 * math.sin((x - 99) / 100 * 3.14 / 1.5)
        pygame.draw.line(screen, (255, 0, 0), (x, 350 + sin_y1), ((x + 1), 350 + sin_y2), 2)

    # shorter lines on x aces
    for i in range(7 * 3 + 3):
        x = 100 + i * 900 / 6 / 4
        pygame.draw.line(screen, BLACK, (x + 900 / 6 / 4, 25), (x + 900 / 6 / 4, 35), 1)
        pygame.draw.line(screen, BLACK, (x + 900 / 6 / 4, 675 - 10), (x + 900 / 6 / 4, 675), 1)
    # shortest lines on x aces
    for i in range(7 * 6 + 5):
        x = 100 + i * 900 / 6 / 4 / 2
        pygame.draw.line(screen, BLACK, (x + 900 / 6 / 4 / 2, 25), (x + 900 / 6 / 4 / 2, 30), 1)
        pygame.draw.line(screen, BLACK, (x + 900 / 6 / 4 / 2, 675 - 5), (x + 900 / 6 / 4 / 2, 675), 1)

    # shorter lines on y aces
    for i in range(9 * 3 + 4):
        y = 50 + i * 600 / 8 / 4
        pygame.draw.line(screen, BLACK, (100 - 25, y + 600 / 8 / 4), (100 - 15, y + 600 / 8 / 4), 1)
        pygame.draw.line(screen, BLACK, (1025, y + 600 / 8 / 4), (1025 - 10, y + 600 / 8 / 4), 1)

    # text
    font = pygame.font.Font(None, 50)
    text = font.render("X", True, BLACK)
    screen.blit(text, (540, 700))
    # meaning of red and blue lines in white rect
    pygame.draw.rect(screen, (255, 255, 255), (670, 51, 130, 74))
    font = pygame.font.Font(None, 30)
    text = font.render("sin x", True, BLACK)
    screen.blit(text, (690, 60))
    pygame.draw.line(screen, (255, 0, 0), [750, 70], [810, 70], 2)
    text = font.render("cos x", True, BLACK)
    screen.blit(text, (688, 100))
    for i in range(3):
        x_1 = 750 + i * 20
        x_2 = 765 + i * 20
        pygame.draw.line(screen, (0, 0, 255), (x_1, 110), (x_2, 110), 2)
    pygame.display.flip()
pygame.quit()