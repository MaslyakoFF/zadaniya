import pygame

pygame.init()
screen = pygame.display.set_mode((300, 300))
screen2 = pygame.Surface(screen.get_size())
run = True
ind = False
x, y = 100, 50
screen.fill(pygame.Color('black'))
pygame.draw.rect(screen, pygame.Color('green'), [(x, y), (100, 100)], 0)
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x1, y1 = event.pos
            x2, y2 = event.pos
            ind = True
            screen2.blit(screen, (0, 0))
        if event.type == pygame.MOUSEMOTION:
            if ind:
                x2, y2 = event.pos
        if event.type == pygame.MOUSEBUTTONUP:
            ind = False
            if x + (x2 - x1) > 0 and x + (x2 - x1) < 200:
                x += x2 - x1
            if y + (y2 - y1) > 0 and y + (y2 - y1) < 200:
                y += y2 - y1
    if ind:
        screen2.fill(pygame.Color('black'))
        screen.blit(screen2, (0, 0))
        pygame.draw.rect(screen, pygame.Color('green'), [(x + x2 - x1, y + y2 - y1), (100, 100)], 0)
    pygame.display.flip()
pygame.quit()
