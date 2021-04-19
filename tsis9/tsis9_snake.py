import sys
import pygame
import random
import json

pygame.init()

pygame.display.set_caption("~~snake~~")

FPS = 60
d = 5

RED = (255, 0, 0)
ORANGE = (255, 127, 0)
YELLOW_1 = (255, 255, 0)
YELLOW_2 = (255, 160, 0)
GREEN = (0, 255, 0)
SKY_BLUE = (51, 153, 255)
BLUE = (0, 0, 153)
PURPLE = (102, 0, 204)
BLACK = (0, 0, 0)

font = pygame.font.SysFont("Comic Sans", 60)
font_small = pygame.font.SysFont("Verdana", 20)

background = pygame.image.load("background.jpg")
game_over = pygame.image.load("game_over.png")
sss = pygame.image.load("ssssssssss.png")

# Create a white screen
size = W, H = (1200, 675)
screen = pygame.display.set_mode(size)

class Menu:
    def __init__(self, punkts = [450, 230, YELLOW_1, YELLOW_2, 0]):
        self.punkts = punkts

    def render(self, poverhnost, num_punkt):
        for i in self.punkts:
            if num_punkt == i[4]:
                pygame.draw.rect(poverhnost, i[2], [i[0], i[1], 210, 50])
            else:
                pygame.draw.rect(poverhnost, i[3], [i[0], i[1], 210, 50])

    def menu(self):
        done = True
        punkt = 0
        while done:

            screen.fill(YELLOW_1)
            mp = pygame.mouse.get_pos()
            for i in self.punkts:
                if mp[0] > i[0] and mp[0] < i[0] + 230 and mp[1] > i[1] and mp[1] < i[1] + 70:
                    punkt = i[4]
            self.render(screen, punkt)
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    sys.exit()
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        sys.exit()
                if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                    if punkt == 0:
                        done = False
                    elif punkt == 1:
                        sys.exit()
            screen.blit(pygame.image.load("start.png"), (400, 200))
            screen.blit(pygame.image.load("quit.png"), (400, 300))
            screen.blit(pygame.image.load("snake_1.png"), (250, 10))
            screen.blit(screen, (0, 0))
            pygame.display.flip()
punkts = [(460, 230, YELLOW_1, RED, 0),
          (460, 330, YELLOW_1, RED, 1)]
game = Menu(punkts)
game.menu()

class Snake(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.size = 1
        self.elements = [[x, y]]
        self.radius = 15
        self.dx = 5
        self.dy = 0
        self.is_add = False
        self.speed = 3
        self.score = 0

    def draw_1(self):
        for element in self.elements:
            pygame.draw.circle(screen, YELLOW_1, element, self.radius)

    def draw_2(self):
        for element in self.elements:
            pygame.draw.circle(screen, YELLOW_2, element, self.radius)

    def add_to_snake(self):
        self.size += 1
        self.score += 1
        self.elements.append([0, 0])
        self.is_add = False
        if self.size % 3 == 0:
            self.speed += 10

    def move(self):
        if self.is_add:
            self.add_to_snake()

        for i in range(self.size - 1, 0, -1):
            self.elements[i][0] = self.elements[i - 1][0]
            self.elements[i][1] = self.elements[i - 1][1]
        self.elements[0][0] += self.dx
        self.elements[0][1] += self.dy
        if self.elements[0] in self.elements[1:]:
            global game_over
            game_over = True

    def eat(self, food_x, food_y):
        x = self.elements[0][0]
        y = self.elements[0][1]
        if food_x <= x <= food_x + 25 and food_y <= y <= food_y + 25:
            return True
        return False

P1 = Snake(100, 100)
P2 = Snake(100, 550)

class Food(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("apple.png")
        self.x = random.randint(50, 820 - 30)
        self.y = random.randint(70, 650 - 30)

    def new(self):
        self.x = random.randint(50, 820 - 30)
        self.y = random.randint(50, 650 - 30)

    def draw(self):
        screen.blit(self.image, (self.x, self.y))

F1 = Food()

enemies_1 = pygame.sprite.Group()
enemies_1.add(P1)
enemies_2 = pygame.sprite.Group()
enemies_2.add(P2)
apples = pygame.sprite.Group()
apples.add(F1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(P2)
all_sprites.add(F1)

def Check_walls(P):
    if P.elements[0][0] - P.radius <= 20 or P.elements[0][0] + P.radius >= 820 or \
            P.elements[0][1] + P.radius >= 650 or P.elements[0][1] - P.radius <= 20:
        return True
    return False

def Game_over(P1, P2):
    if (Check_walls(P1) == True) or (Check_walls(P2) == True) or game_over == True:
        screen.fill(BLACK)
        screen.blit(game_over, (250, 150))
        if P1.score == P2.score:
            game_over_output = font.render("draw", True, YELLOW_1)
            screen.blit(game_over_output, (520, 500))
        else:
            if P1.score > P2.score:
                game_over_output = font_small.render("winner is the first gamer", True, YELLOW_1)
            if P1.score < P2.score:
                game_over_output = font_small.render("winner is the second gamer", True, YELLOW_1)
            screen.blit(game_over_output, (450, 500))

            pygame.display.update()
    pygame.display.flip()

def to_save():
    f = open("snake", "w")

    save_game = {'Elements_1' :  P1.elements, 'dx_1' : P1.dx, 'dy_1' : P1.dy,
                 'Elements_2' : P2.elements, 'dx_2' : P2.dx, 'dy_2' : P2.dy,
                }
    f.write(json.dumps(save_game))

done = False
while not done:
    pygame.time.delay(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            to_save()
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                to_save()
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
    scores_1 = font.render("score 1: " + str(P1.score), True, BLACK)
    scores_2 = font.render("score 2: " + str(P2.score), True, BLACK)
    screen.blit(sss, (800, 170))
    screen.blit(scores_1, (910, 130))
    screen.blit(scores_2, (910, 170))
    pygame.draw.rect(screen, BLACK, [20, 20, 800, 630])
    P1.draw_1()
    F1.draw()
    P2.draw_2()
    screen.blit(pygame.image.load("snake.png"), (850, 0))
    Game_over(P1, P2)
    pygame.display.flip()