import pygame
import random

pygame.init()
v = 20
sc = (50, 50, 50)
x = 900
y = 750
c = min(x, y) // v
p = c // 10
n = 0
x = x - x % c
y = y - y % c
flag_img = pygame.image.load("flag_orange.png")
mine_img = list(map(lambda x: pygame.transform.scale(x, (c, c)),
                    [pygame.image.load("mine1.png"), pygame.image.load("mine2.png"), pygame.image.load("mine3.png"),
                     pygame.image.load("mine4.png"), pygame.image.load("mine5.png")]))

s = pygame.display.set_mode([x, y])
font = pygame.font.SysFont("Arial", 16)
razmer_x = (x // (c + p)) - 2
razmer_y = (y // (c + p)) - 4

l = [[0] * razmer_y for _ in range(0, razmer_x)]
mines = [[0] * razmer_y for _ in range(0, razmer_x)]

for _ in range(75):
    i, j = random.randint(0, razmer_x - 1), random.randint(0, razmer_y - 1)
    while mines[i][j] == 1:
        i, j = random.randint(0, razmer_x - 1), random.randint(0, razmer_y - 1)
    mines[i][j] = 1


def db(co, i, j):
    pygame.draw.rect(s, co, [i * c + p * (i + 1) + c + p, j * c + p * (j + 1) + (c + p) * 4, c, c])


def nog(i, j):
    i -= c + p
    j -= (c + p) * 4
    if i >= 0 and j >= 0:
        i //= (c + p)
        j //= (c + p)
        if i < razmer_x and j < razmer_y:
            return i, j
    return -1, -1


def otkr(x, y):
    if x < 0 or y < 0:
        return True
    if l[x][y] == 0:
        if mines[x][y] == 1:
            return False
        n = 0
        if y > 0:
            if mines[x][y - 1] == 1:
                n = n + 1
        if y > 0 and x > 0:
            if mines[x - 1][y - 1] == 1:
                n = n + 1
        if x > 0:
            if mines[x - 1][y] == 1:
                n = n + 1
        if y + 1 < razmer_y:
            if mines[x][y + 1] == 1:
                n = n + 1
        if y + 1 < razmer_y and x + 1 < razmer_x:
            if mines[x + 1][y + 1] == 1:
                n = n + 1
        if y + 1 < razmer_y and x > 0:
            if mines[x - 1][y + 1] == 1:
                n = n + 1
        if x + 1 < razmer_x:
            if mines[x + 1][y] == 1:
                n = n + 1
        if x + 1 < razmer_x and y > 0:
            if mines[x + 1][y - 1] == 1:
                n = n + 1
        if n > 0:
            l[x][y] = n
            return True
        else:
            l[x][y] = -1
            if y > 0:
                otkr(x, y - 1)
            if y > 0 and x > 0:
                otkr(x - 1, y - 1)
            if x > 0:
                otkr(x - 1, y)
            if y + 1 < razmer_y:
                otkr(x, y + 1)
            if y + 1 < razmer_y and x + 1 < razmer_x:
                otkr(x + 1, y + 1)
            if y + 1 < razmer_y and x > 0:
                otkr(x - 1, y + 1)
            if x + 1 < razmer_x:
                otkr(x + 1, y)
            if x + 1 < razmer_x and y > 0:
                otkr(x + 1, y - 1)
            return True
    else:
        return True


while True:
    while True:
        s.fill((0, 0, 0))
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
            if e.type == pygame.MOUSEBUTTONUP:
                if e.button == 1:
                    k = list(e.pos)
                    g = list(nog(*k))
                    if not otkr(*g):
                        t = font.render("You loose!", 1, (255, 255, 255))
                        s.blit(t, (razmer_x // 2 - 5, 0))
                        l[g[0]][g[1]] = -3
                        n = 1
                elif e.button == 3:
                    b = nog(*e.pos)
                    if l[b[0]][b[1]] == 0:
                        l[b[0]][b[1]] = -2
                    else:
                        l[b[0]][b[1]] = 0
        for i in range(0, razmer_x):
            for j in range(0, razmer_y):
                if l[i][j] == -2 or l[i][j] == 0:
                    if (i + j) % 2 == 0:
                        co = (255, 255, 255)
                    else:
                        co = (204, 255, 255)
                    db(co, i, j)
                    if l[i][j] == -2:
                        s.blit(flag_img, (i * c + p * (i + 1) + c + p, j * c + p * (j + 1) + (c + p) * 4))
                elif l[i][j] != -1 and l[i][j] != -3:
                    t = font.render(str(l[i][j]), 1,
                                    (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255)))
                    s.blit(t, [(i * c + p * (i + 1) + c + p), (j * c + p * (j + 1) + (c + p) * 4)])
                # elif l[i][j]==-1:
                # t= font.render("*", 1, (random.randint(50,255),random.randint(50, 255),random.randint(50, 255)))
                # s.blit(t, [(i * c + p * (i + 1) + c + p),(j * c + p * (j + 1) + (c + p) * 4)])
                elif l[i][j] == -3:
                    s.blit(mine_img[random.randint(0, 4)],
                           (i * c + p * (i + 1) + c + p, j * c + p * (j + 1) + (c + p) * 4))
        pygame.display.flip()
        if n == 1:
            break
    while True:
        s.fill((0, 0, 0))
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_SPACE:
                    n = 0
        for i in range(0, razmer_x):
            for j in range(0, razmer_y):
                if l[i][j] == -2 or l[i][j] == 0:
                    if (i + j) % 2 == 0:
                        co = (255, 255, 255)
                    else:
                        co = (204, 255, 255)
                    db(co, i, j)
                    if l[i][j] == -2:
                        s.blit(flag_img, (i * c + p * (i + 1) + c + p, j * c + p * (j + 1) + (c + p) * 4))
                elif l[i][j] != -1 and l[i][j] != -3:
                    t = font.render(str(l[i][j]), 1,
                                    (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255)))
                    s.blit(t, [(i * c + p * (i + 1) + c + p), (j * c + p * (j + 1) + (c + p) * 4)])
                elif l[i][j] == -1:
                    t = font.render("*", 1, (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255)))
                    s.blit(t, [(i * c + p * (i + 1) + c + p), (j * c + p * (j + 1) + (c + p) * 4)])
                elif l[i][j] == -3:
                    s.blit(mine_img[random.randint(0, 4)],
                           (i * c + p * (i + 1) + c + p, j * c + p * (j + 1) + (c + p) * 4))
        pygame.display.flip()
        if n == 0:
            l = [[0] * razmer_y for _ in range(0, razmer_x)]
            mines = [[0] * razmer_y for _ in range(0, razmer_x)]
            for _ in range(20):
                i, j = random.randint(0, razmer_x - 1), random.randint(0, razmer_y - 1)
                while mines[i][j] == 1:
                    i, j = random.randint(0, razmer_x - 1), random.randint(0, razmer_y - 1)
                mines[i][j] = 1
            break
