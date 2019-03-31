import pygame
import random


class Board():
    def __init__(self):
        pygame.init()
        print('Введите размер поля (в клетках, через пробел) и количество мин:')
        a = input().split()
        self.x = (int(a[0]) * 22) - 2
        self.y = (int(a[1]) * 22) - 2
        b = int(input())
        self.mines = b
        self.screen = pygame.display.set_mode((self.x, self.y))
        self.a = []
        for i in range(0, self.y + 2, 22):
            self.a.append([])
            for j in range(0, self.x + 2, 22):
                self.a[-1].append([(j, i), 0])
        g = []
        for i in range(self.mines):
            x = random.randint(-1, 9)
            y = random.randint(-1, 14)
            while (x, y) in g:
                x = random.randint(-1, 9)
                y = random.randint(-1, 14)
            g.append((x, y))
            self.a[y][x][1] = 10
            if y != 0:
                if self.a[y - 1][x][1] != 10:
                    self.a[y - 1][x][1] += 1
                if x != 0:
                    if self.a[y - 1][x - 1][1] != 10:
                        self.a[y - 1][x - 1][1] += 1
                if x != ((self.x + 2) / 22) - 1:
                    if self.a[y - 1][x + 1][1] != 10:
                        self.a[y - 1][x + 1][1] += 1
            if y != ((self.y + 2) / 22) - 1:
                if self.a[y + 1][x][1] != 10:
                    self.a[y + 1][x][1] += 1
                if x != 0:
                    if self.a[y + 1][x - 1][1] != 10:
                        self.a[y + 1][x - 1][1] += 1
                if x != ((self.x + 2) / 22) - 1:
                    if self.a[y + 1][x + 1][1] != 10:
                        self.a[y + 1][x + 1][1] += 1
            if x != 0:
                if self.a[y][x - 1][1] != 10:
                    self.a[y][x - 1][1] += 1
            if x != ((self.x + 2) / 22) - 1:
                if self.a[y][x + 1][1] != 10:
                    self.a[y][x + 1][1] += 1


class Minesweeper(Board):
    def open_cell(self):
        run = True
        ind = False
        numbers = []
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    ind = True
                    x, y = event.pos
            self.screen.fill(pygame.Color('white'))
            for i in self.a:
                for j in i:
                    col = 'black'
                    if j[1] == 10:
                        col = 'red'
                    pygame.draw.rect(self.screen, pygame.Color(col), [j[0], (20, 20)], 0)
                    if ind:
                        if 0 < x - j[0][0] < 20 and 0 < y - j[0][1] < 20 and j[1] != 10:
                            numbers.append((j[0], j[1]))
            for i in numbers:
                font = pygame.font.Font(None, 20)
                text = font.render(str(i[1]), 1, (100, 255, 100))
                self.screen.blit(text, i[0])
                pygame.draw.rect(self.screen, pygame.Color('black'), [i[0], (20, 20)], 1)
            pygame.display.flip()
        pygame.quit()


mn = Minesweeper()
mn.open_cell()
