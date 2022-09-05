import pygame
import random

pygame.init()

deno_x = 40
deno_y = 40
if deno_y % 2 == 1:
    print("Error: make height even")
    exit()
deno_small = False
screen = pygame.display.set_mode((1000, 700))
img_ball = pygame.image.load("deno4.png")
img_ball = pygame.transform.scale(img_ball, (deno_x, deno_y))
deno = pygame.image.load("deno_small.png")
deno = pygame.transform.scale(deno, (deno_x, deno_y // 2))
pre1 = pygame.image.load("pre1.png")
pre2 = pygame.image.load("pre2.png")
pre3 = pygame.image.load("pre3.png")
pre1 = pygame.transform.scale(pre1, (40, 39))
pre2 = pygame.transform.scale(pre2, (80, 39))
pre3 = pygame.transform.scale(pre3, (120, 39))

font = pygame.font.SysFont("Arial", 24)
x = 100
n = 0
while True:
    y = 700 // 2
    ys = -10
    yu = 0.4
    xs = 4
    xu = 0.002
    sys = ys
    yes = False
    prome = 0
    x_and_y = []
    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                exit()
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_SPACE:
                    if not yes:
                        yes = True
                        ys = sys
                elif e.key == pygame.K_DOWN:
                    deno_y = deno_y / 2
                    deno_small = True
                    yu *= 2
            elif e.type == pygame.KEYUP:
                if e.key == pygame.K_DOWN:
                    deno_y = deno_y * 2
                    deno_small = False
                    # yu //= 2
        screen.fill((0, 0, 0))
        pygame.draw.line(screen, (255, 255, 255), (0, 700 // 2), (1000, 700 // 2), 1)

        t = font.render("Press SPACE to jump", True, (255, 0, 0))
        screen.blit(t, (400, 600))

        if not deno_small:
            screen.blit(img_ball, (x, y - deno_y))
        else:
            screen.blit(deno, (x, y - deno_y))
        if prome == 0:
            x_and_y.append([1000, 350, random.randint(1, 3)])
            prome = random.randint(85, 125)
        for i in reversed(range(0, len(x_and_y))):
            if x_and_y[i][0] <= -120:
                x_and_y.pop(i)
                continue
            x_and_y[i][0] = x_and_y[i][0] - xs
            if x_and_y[i][2] == 1:
                screen.blit(pre1, (x_and_y[i][0], x_and_y[i][1] - 39))
            elif x_and_y[i][2] == 2:
                screen.blit(pre2, (x_and_y[i][0], x_and_y[i][1] - 39))
            else:
                screen.blit(pre3, (x_and_y[i][0], x_and_y[i][1] - 39))
            head_rect = pygame.Rect(x, y, deno_x, deno_y)
            candy_rect = pygame.Rect(x_and_y[i][0], x_and_y[i][1], 40 * x_and_y[i][2], 39)

            if head_rect.colliderect(candy_rect):
                n = 1
        xs += xu
        prome -= 1
        if yes:
            y = y + ys
            ys = ys + yu
            # x = x + xs
        if (y >= 700 // 2):
            y = 700 // 2
            ys = sys
            yes = False
        pygame.display.flip()
        pygame.time.delay(20)
        if n == 1:
            break
    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                exit()
            elif e.type == pygame.KEYUP:
                if e.key == pygame.K_SPACE:
                    n = 0
        if n == 0:
            break
