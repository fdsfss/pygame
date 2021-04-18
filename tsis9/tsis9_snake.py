import pygame
from pygame.locals import *
import random, time

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

class Snake(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        x = random.randint(0, W)
        y = random.randint(0, H)
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

class Food(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("apple.jpg")
        self.surf = pygame.Surface((10, 10))
        self.rect = self.surf.get_rect(center=(random.randint(5, W - 5), 0))
        self.x = random.randint(0, W)
        self.y = random.randint(0, H)

    def new(self):
        self.x = random.randint(0, W)
        self.y = random.randint(0, H)

P1 = Snake()
P2 = Snake()
F1 = Food()

apples = pygame.sprite.Group()
apples.add(F1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(P2)
all_sprites.add(F1)

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

done = False

while not done:
    pygame.time.delay(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:
            done = True
        if event.type == pygame.KEYDOWN:
            Move_on_the_screen(P1, event.type)
        if event.type == pygame.KEYDOWN:
            Move_on_the_screen(P2, event.type)

    if P1.eat(F1.x, F1.y):
        P1.is_add = True
        F1.new()

    if P2.eat(F1.x, F1.y):
        P2.is_add = True
        F1.new()
    P1.move()
    P2.move()
    screen.fill((0, 0, 0))
    P1.draw()
    P2.draw()
    pygame.display.flip()
    '''
        if pygame.sprite.spritecollideany(P1, apples):
            pygame.mixer.Sound('crash.wav').play()
            time.sleep(1)

            screen.fill(RED)

            pygame.display.update()
            for i in all_sprites:
                i.kill()
            time.sleep(2)
            pygame.quit()
    '''
pygame.display.update()