import pygame
import random

pygame.init()

pygame.display.set_caption("~~snake~~")

FPS = 60
d = 5

RED = (255, 0, 0)
ORANGE = (255, 127, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
SKY_BLUE = (51, 153, 255)
BLUE = (0, 0, 153)
PURPLE = (102, 0, 204)

font = pygame.font.SysFont("Comic Sans", 60)
font_small = pygame.font.SysFont("Verdana", 20)

background = pygame.image.load("background.jpg")

# Create a white screen
size = W, H = (1200, 675)
screen = pygame.display.set_mode(size)

class Snake:
    def __init__(self, x, y):
        self.size = 1
        self.elements = [[x, y]]
        self.radius = 15
        self.dx = 5
        self.dy = 0
        self.is_add = False
        self.speed = 3

    def draw(self):
        for element in self.elements:
            pygame.draw.circle(screen, (255, 0, 0), element, self.radius)

    def add_to_snake(self):
        self.size += 1
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
        if food_x <= x <= food_x + 10 and food_y <= y <= food_y + 10:
            return True
        return False

class Food:
    def __init__(self):
        self.image = pygame.image.load("apple.jpg")
        self.surf = pygame.Surface((10, 10))
        self.rect = self.surf.get_rect(center=(random.randint(5, W - 40), 0))
        self.x = random.randint(0, W)
        self.y = random.randint(0, H)

    def new(self):
        self.x = random.randint(0, W)
        self.y = random.randint(0, H)

P1 = Snake(random.randint(0, W), random.randint(0, H))
P2 = Snake(random.randint(0, W), random.randint(0, H))
F1 = Food()

done = False

snake_1 = pygame.sprite.Group()
snake_1.add(P1)

def Move_on_the_screen(P, key):
    if key == pygame.K_RIGHT and P.dx != -d:
        P.dx = d
        P.dy = 0
    if key == pygame.K_LEFT and P.dx != d:
        P.dx = -d
        P.dy = 0
    if key == pygame.K_UP and P.dy != d:
        P.dx = 0
        P.dy = -d
    if key == pygame.K_DOWN and P.dy != -d:
        P.dx = 0
        P.dy = d
    if event.key == pygame.K_d and P.dx != -d:
        P.dx = d
        P.dy = 0
    if event.key == pygame.K_a and P.dx != d:
        P.dx = -d
        P.dy = 0
    if event.key == pygame.K_w and P.dy != d:
        P.dx = 0
        P.dy = -d
    if event.key == pygame.K_s and P.dy != -d:
        P.dx = 0
        P.dy = d

while not done:
    pygame.time.delay(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:
            done = True
        if event.type == pygame.KEYDOWN:
            Move_on_the_screen(P1, event.type)
            Move_on_the_screen(P2, event.type)

    if P1.eat(F1.x, F1.y):
        P1.is_add = True
        F1.new()

    if P2.eat(F1.x, F1.y):
        P2.is_add = True
        F1.new()

    screen.fill((0, 0, 0))
    P1.move()

    pygame.display.update()