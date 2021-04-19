import pygame
from pygame.locals import *
import random, time

pygame.init()

pygame.display.set_caption("~~snake~~")

FPS = 60
d = 5
SCORE_APPLES_1 = SCORE_APPLES_2 = 0

RED = (255, 0, 0)
ORANGE = (255, 127, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
SKY_BLUE = (51, 153, 255)
BLUE = (0, 0, 153)
PURPLE = (102, 0, 204)
BLACK = (0, 0, 0)

font = pygame.font.SysFont("Comic Sans", 60)
font_small = pygame.font.SysFont("Verdana", 20)

background = pygame.image.load("background.jpg")

# Create a white screen
size = W, H = (1200, 675)
screen = pygame.display.set_mode(size)

class Snake(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        x = random.randint(20, 820)
        y = random.randint(20, 650)
        self.size = 1
        self.elements = [[x, y]]
        self.radius = 15
        self.dx = 5
        self.dy = 0
        self.is_add = False
        self.speed = 3
        self.score = 0

    def draw(self):
        for element in self.elements:
            pygame.draw.circle(screen, (255, 0, 0), element, self.radius)

    def add_to_snake(self):
        self.size += 1
        self.score += 1
        self.elements.append([0, 0])
        self.is_add = False
        if self.size % 7 == 0:
            self.speed += 10

    def move(self):
        if self.is_add:
            self.add_to_snake()

        for i in range(self.size - 1, 0, -1):
            self.elements[i][0] = self.elements[i - 1][0]
            self.elements[i][1] = self.elements[i - 1][1]

        self.elements[0][0] += self.dx
        self.elements[0][1] += self.dy

    def eat(self, food_x, food_y):
        x = self.elements[0][0]
        y = self.elements[0][1]
        if food_x <= x <= food_x + 25 and food_y <= y <= food_y + 25:
            return True
        return False

P1 = Snake()
P2 = Snake()

class Food(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("apple.png")
        self.x = random.randint(20, 820)
        self.y = random.randint(20, 650)

    def new(self):
        self.x = random.randint(20, 820)
        self.y = random.randint(20, 650)

    def draw(self):
        screen.blit(self.image, (self.x, self.y))

F1 = Food()

apples = pygame.sprite.Group()
apples.add(F1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(P2)
all_sprites.add(F1)

done = False

while not done:
    pygame.time.delay(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True
            if event.key == pygame.K_RIGHT and P1.dx != -d:
                P1.dx = d
                P1.dy = 0
            if event.key == pygame.K_LEFT and P1.dx != d:
                P1.dx = -d
                P1.dy = 0
            if event.key == pygame.K_UP and P1.dy != d:
                P1.dx = 0
                P1.dy = -d
            if event.key == pygame.K_DOWN and P1.dy != -d:
                P1.dx = 0
                P1.dy = d
            if event.key == pygame.K_d and P2.dx != -d:
                P2.dx = d
                P2.dy = 0
            if event.key == pygame.K_a and P2.dx != d:
                P2.dx = -d
                P2.dy = 0
            if event.key == pygame.K_w and P2.dy != d:
                P2.dx = 0
                P2.dy = -d
            if event.key == pygame.K_s and P2.dy != -d:
                P2.dx = 0
                P2.dy = d
    if P1.eat(F1.x, F1.y):
        P1.is_add = True
        F1.new()
    if P2.eat(F1.x, F1.y):
        P2.is_add = True
        F1.new()
    P1.move()
    P2.move()
    screen.blit(background, (0, 0))
    pygame.draw.rect(screen, BLACK, [20, 20, 800, 630])
    F1.draw()
    P1.draw()
    P2.draw()
    pygame.display.flip()
pygame.display.update()