import sys
import pygame


class GUI:
    def __init__(self, square, height, width):
        self.window = pygame.display.set_mode((height, width))
        self.height = height
        self.width = width
        self.square = square
        self.radius = int(square / 2 - 5)

    def draw(self, board, row, column):
        for c in range(column):
            for r in range(row):
                pygame.draw.rect(self.window, (129, 133, 137),
                                 (c * self.square, r * self.square, self.square, self.square))
                pygame.draw.circle(self.window, (255, 255, 255),
                                   (int(c * self.square + self.square / 2), int(r * self.square + self.square / 2)),
                                   self.radius)
        for c in range(column):
            for r in range(row):
                if board[r][c] == 1:
                    pygame.draw.circle(self.window, (255, 0, 0), (
                        int(c * self.square + self.square / 2), self.height - int(r * self.square + self.square / 2)),
                                       self.radius)
                elif board[r][c] == 2:
                    pygame.draw.circle(self.window, (0, 0, 255), (
                        int(c * self.square + self.square / 2), self.height - int(r * self.square + self.square / 2)),
                                       self.radius)

            pygame.display.update()

    def start(self):
        pygame.init()
        bg_img = pygame.image.load('bg.png')
        bg_img = pygame.transform.scale(bg_img, (self.width, self.height))

        font = pygame.font.SysFont('Corbel', 35)

        color = (255, 255, 255)
        color1 = (0, 0, 255)
        color2 = (255, 0, 0)

        run = True
        while run:
            self.window.blit(bg_img, (0, 0))

            mouse = pygame.mouse.get_pos()

            if self.width / 2.25 <= mouse[0] <= self.width / 3 + 250 and self.height / 3 <= mouse[1] <= self.height / 3 + self.square:
                pygame.draw.rect(self.window, (164, 219, 232), [self.width / 3, self.height / 3, 250, self.square])

                text1 = font.render('START', True, color1)
                self.window.blit(text1, (self.width / 2.25, self.height / 2.6))

            else:
                pygame.draw.rect(self.window, color1, [self.width / 3, self.height / 3, 250, self.square])

                text1 = font.render('START', True, color)
                self.window.blit(text1, (self.width / 2.25, self.height / 2.6))

            if self.width / 3 <= mouse[0] <= self.width / 3 + 250 and self.height / 2 <= mouse[1] <= self.height / 2 + self.square:
                pygame.draw.rect(self.window, (255, 127, 127), [self.width / 3, self.height / 2, 250, self.square])

                text2 = font.render('QUIT', True, color2)
                self.window.blit(text2, (self.width / 2.25, self.height / 1.80))

            else:
                pygame.draw.rect(self.window, color2, [self.width / 3, self.height / 2, 250, self.square])

                text2 = font.render('QUIT', True, color)
                self.window.blit(text2, (self.width / 2.25, self.height / 1.80))

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.width / 2.25 <= mouse[0] <= self.width / 3 + 250 and self.height / 3 <= mouse[
                    1] <= self.height / 3 + self.square:
                    return True

            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.width / 3 <= mouse[0] <= self.width / 3 + 250 and self.height / 2 <= mouse[
                    1] <= self.height / 2 + self.square:
                    sys.exit()
