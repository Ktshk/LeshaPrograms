import pygame

v = 10
s = [[0] * (700 // v) for _ in range(0, 1400 // v)]
pygame.init()
screen = pygame.display.set_mode((1400, 700))
pygame.display.set_caption("Game of Life")
font = pygame.font.SysFont("Arial", 32)

p = True
g = False
a = False
while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            quit()
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_SPACE:
                p = not p
            if i.key == pygame.K_DOWN:
                g = True
        if i.type == pygame.MOUSEBUTTONUP:
            a = False
        if i.type == pygame.MOUSEMOTION and a:
            x, y = pygame.mouse.get_pos()
            x1 = x // v
            y1 = y // v
            s[x1][y1] = 1

        if i.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            x1 = x // v
            y1 = y // v
            s[x1][y1] = 1 - s[x1][y1]
            a = True
    screen.fill((255, 255, 255))
    for i in range(0, 700, v):
        pygame.draw.line(screen, (0, 0, 0), (0, i), (1400, i), 1)
    for i in range(0, 1400, v):
        pygame.draw.line(screen, (0, 0, 0), (i, 0), (i, 1400), 1)

    for i in range(0, 1400 // v):
        for j in range(0, 700 // v):
            if s[i][j] == 1:
                pygame.draw.rect(screen, (0, 255, 0), ((i) * v, (j) * v, v, v), 0)
    # pygame.draw.rect(screen, (255, 0, 0), (200, 300, 50, 50),0)

    # screen.blit(f, (0, y))
    # screen.blit(l, (x, 25))
    # x = x + 1
    # y = y + 1
    if p == False:
        t = font.render("Press SPACE to pause game", True, (255, 0, 0))
        screen.blit(t, (500, 650))
    else:
        t = font.render("Press SPACE to start game or DOWN ARROW to go step-by-step", True, (255, 0, 0))
        screen.blit(t, (300, 650))

    if p == False or g == True:
        g = False
        d = [[0] * (700 // v) for _ in range(0, 1400 // v)]
        for i in range(0, 1400 // v):
            for j in range(0, 700 // v):
                n = 0

                if j > 0:
                    if s[i][j - 1] == 1:
                        n = n + 1
                if j > 0 and i > 0:
                    if s[i - 1][j - 1] == 1:
                        n = n + 1
                if i > 0:
                    if s[i - 1][j] == 1:
                        n = n + 1
                if j + 1 < 700 // v:
                    if s[i][j + 1] == 1:
                        n = n + 1
                if j + 1 < 700 // v and i + 1 < 1400 // v:
                    if s[i + 1][j + 1] == 1:
                        n = n + 1
                if j + 1 < 700 // v and i > 0:
                    if s[i - 1][j + 1] == 1:
                        n = n + 1
                if i + 1 < 1400 // v:
                    if s[i + 1][j] == 1:
                        n = n + 1
                if i + 1 < 1400 // v and j > 0:
                    if s[i + 1][j - 1] == 1:
                        n = n + 1
                if s[i][j] == 1:
                    if n == 2 or n == 3:
                        d[i][j] = 1
                else:
                    if n == 3:
                        d[i][j] = 1
        s = d
    pygame.display.update()

    pygame.time.delay(1)
