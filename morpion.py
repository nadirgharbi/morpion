import pygame
import sys, time
import pygame_menu

from const import *

##### TODO : SCORE +1 MEME QUANDON PERD
##### TODO : MESSAGE DE VICTOIRE
##### TODO : RESULTATS NUL

class Game:
    def __init__(self):
        self.size_X = 100,100
        self.size_O = 80,80
        self.round_img = pygame.transform.scale(pygame.image.load('round.png'),self.size_O).convert_alpha()
        self.cross_img = pygame.transform.scale(pygame.image.load('cross.png'), self.size_X).convert_alpha()
        self.horizontal_line1 = (WIDTH // 3) + 15
        self.horizontal_line2 = (WIDTH - self.horizontal_line1) - 10
        self.vertical_line1 = (WIDTH // 3) + 15
        self.vertical_line2 = (WIDTH - self.vertical_line1) - 10

        self.turn = True
        self.score_O = 0
        self.score_X = 0

        self.case_1 = True
        self.case_2 = True
        self.case_3 = True
        self.case_4 = True
        self.case_5 = True
        self.case_6 = True
        self.case_7 = True
        self.case_8 = True
        self.case_9 = True

        self.cases = [
            self.case_1, self.case_2, self.case_3,
            self.case_4, self.case_5, self.case_6,
            self.case_7, self.case_8, self.case_9
        ]

        self.checkWin = [
            '-','&','é',
            '=','(','.',
            'è','_','ç'
        ]

    def menu(self):
        pass

    def draw_lines(self):
        # HORIZONTAL LINES
        pygame.draw.line(screen, DARK, (self.horizontal_line1, 50), (self.horizontal_line1, 430), width=5)
        pygame.draw.line(screen, DARK, (self.horizontal_line2, 50), (self.horizontal_line2, 430), width=5)

        # VERTICAL LINES
        pygame.draw.line(screen, DARK, (50, self.vertical_line1), (430, self.vertical_line1), width=5)
        pygame.draw.line(screen, DARK, (50, self.vertical_line2), (430, self.vertical_line2), width=5)

        # HORIZONTAL TOP / BOTTOM
        pygame.draw.line(screen, DARK, (50, 50), (430,50), width=5)
        pygame.draw.line(screen, DARK, (50, 430), (430, 430), width=5)

        # VERTICAL LEFT / RIGHT
        pygame.draw.line(screen, DARK, (50, 50), (50, 430), width=5)
        pygame.draw.line(screen, DARK, (430, 50), (430, 430), width=5)


    def round(self):
        if self.turn:
            # RANGEE DROITE
            if 330 < set_pos_mouse_x < 420:
                if (330 < set_pos_mouse_y < 420) and self.case_9: # CASE_9
                    screen.blit(self.round_img, (330,330))
                    self.case_9 = False
                    self.checkWin[8] = 'O'
                    self.turn = False
                if (190 < set_pos_mouse_y < 300) and self.case_6: # CASE_6
                    screen.blit(self.round_img, (330, 205))
                    self.case_6 = False
                    self.checkWin[5] = 'O'
                    self.turn = False
                if (50 < set_pos_mouse_y < 160) and self.case_3: # CASE_3
                    screen.blit(self.round_img, (330, 75))
                    self.case_3 = False
                    self.checkWin[2] = 'O'

                    self.turn = False
            # RANGEE MILIEU
            if 190 < set_pos_mouse_x < 300:
                if (330 < set_pos_mouse_y < 420) and self.case_8: # CASE_8
                    screen.blit(self.round_img, (205, 330))
                    self.case_8 = False
                    self.checkWin[7] = 'O'
                    self.turn = False
                if (190 < set_pos_mouse_y < 300) and self.case_5: # CASE_5
                    screen.blit(self.round_img, (205, 205))
                    self.case_5 = False
                    self.checkWin[4] = 'O'
                    self.turn = False
                if (50 < set_pos_mouse_y < 160) and self.case_2: # CASE_2
                    screen.blit(self.round_img, (205, 75))
                    self.case_2 = False
                    self.checkWin[1] = 'O'
                    self.turn = False

            # RANGEE GAUCHE
            if 50 < set_pos_mouse_x < 160:
                if (330 < set_pos_mouse_y < 420) and self.case_7: # CASE_7
                    screen.blit(self.round_img, (75, 330))
                    self.case_7 = False
                    self.checkWin[6] = 'O'
                    self.turn = False
                if (190 < set_pos_mouse_y < 300) and self.case_4: # CASE_4
                    screen.blit(self.round_img, (75, 205))
                    self.case_4 = False
                    self.checkWin[3] = 'O'
                    self.turn = False
                if (50 < set_pos_mouse_y < 160) and self.case_1: # CASE_1
                    screen.blit(self.round_img, (75, 75))
                    self.case_1 = False
                    self.checkWin[0] = 'O'
                    self.turn = False

    def cross(self):
        if not self.turn:
            # RANGEE DROITE
            if 330 < set_pos_mouse_x < 420:
                if (330 < set_pos_mouse_y < 420) and self.case_9:  # CASE_9
                    screen.blit(self.cross_img, (320,320))
                    self.case_9 = False
                    self.checkWin[8] = 'X'
                    self.turn = True
                if (190 < set_pos_mouse_y < 300) and self.case_6:  # CASE_6
                    screen.blit(self.cross_img, (320,200))
                    self.case_6 = False
                    self.checkWin[5] = 'X'
                    self.turn = True
                if (50 < set_pos_mouse_y < 160) and self.case_3:  # CASE_3
                    screen.blit(self.cross_img, (320, 70))
                    self.case_3 = False
                    self.checkWin[2] = 'X'
                    self.turn = True

            # RANGEE MILIEU
            if 190 < set_pos_mouse_x < 300:
                if (330 < set_pos_mouse_y < 420) and self.case_8:  # CASE_8
                    screen.blit(self.cross_img, (200,320))
                    self.case_8 = False
                    self.checkWin[7] = 'X'
                    self.turn = True
                if (190 < set_pos_mouse_y < 300) and self.case_5:  # CASE_5
                    screen.blit(self.cross_img, (200, 200))
                    self.case_5 = False
                    self.checkWin[4] = 'X'
                    self.turn = True
                if (50 < set_pos_mouse_y < 160) and self.case_2:  # CASE_2
                    screen.blit(self.cross_img, (200, 70))
                    self.case_2 = False
                    self.checkWin[1] = 'X'
                    self.turn = True

            # RANGEE GAUCHE
            if 50 < set_pos_mouse_x < 160:
                if (330 < set_pos_mouse_y < 420) and self.case_7:  # CASE_7
                    screen.blit(self.cross_img, (70, 320))
                    self.case_7 = False
                    self.checkWin[6] = 'X'
                    self.turn = True
                if (190 < set_pos_mouse_y < 300) and self.case_4:  # CASE_4
                    screen.blit(self.cross_img, (70, 200))
                    self.case_4 = False
                    self.checkWin[3] = 'X'
                    self.turn = True
                if (50 < set_pos_mouse_y < 160) and self.case_1:  # CASE_1
                    screen.blit(self.cross_img, (70, 70))
                    self.case_1 = False
                    self.checkWin[0] = 'X'
                    self.turn = True

    def win(self):
        # VERTICAL
        if self.checkWin[0] == self.checkWin[3] == self.checkWin[6]:
            return True
        if self.checkWin[1] == self.checkWin[4] == self.checkWin[7]:
            return True
        if self.checkWin[2] == self.checkWin[5] == self.checkWin[8]:
            return True

        # DIAGONAL
        if self.checkWin[0] == self.checkWin[4] == self.checkWin[8]:
            return True
        if self.checkWin[2] == self.checkWin[4] == self.checkWin[6]:
            return True

        # HORIZONTAL
        if self.checkWin[0] == self.checkWin[1] == self.checkWin[2]:
            return True
        if self.checkWin[3] == self.checkWin[4] == self.checkWin[5]:
            return True
        if self.checkWin[6] == self.checkWin[7] == self.checkWin[8]:
            return True

    def update_score(self):
        if self.win():
            # CIRCLE SCORE VERTICAL
            if (self.checkWin[0] and self.checkWin[3] and self.checkWin[6]) == 'O':
                self.score_O += 1
            if (self.checkWin[1] and self.checkWin[4] and self.checkWin[7]) == 'O':
                self.score_O += 1
            if (self.checkWin[2] and self.checkWin[5] and self.checkWin[8]) == 'O':
                self.score_O += 1

            # CIRCLE SCORE DIAGONAL
            if (self.checkWin[0] == self.checkWin[4] == self.checkWin[8]) == 'O':
                self.score_O += 1
            if self.checkWin[2] == self.checkWin[4] == self.checkWin[6]:
                self.score_O += 1

            # CIRCLE SCORE HORIZONTAL
            if (self.checkWin[0] and self.checkWin[1] and self.checkWin[2]) == 'O':
                self.score_O += 1
            if (self.checkWin[3] and self.checkWin[4] and self.checkWin[5]) == 'O':
                self.score_O += 1
            if (self.checkWin[6] and self.checkWin[7] and self.checkWin[8]) == 'O':
                self.score_O += 1

             # CROSS SCORE VERTICAL
            if (self.checkWin[0] and self.checkWin[3] and self.checkWin[6]) == 'X':
                self.score_X += 1
            if (self.checkWin[1] and self.checkWin[4] and self.checkWin[7]) == 'X':
                self.score_X += 1
            if (self.checkWin[2] and self.checkWin[5] and self.checkWin[8]) == 'X':
                self.score_X += 1

            # CROSS SCORE DIAGONAL
            if (self.checkWin[0] == self.checkWin[4] == self.checkWin[8]) == 'X':
                self.score_X += 1
            if self.checkWin[2] == self.checkWin[4] == self.checkWin[6]:
                self.score_X += 1

            # CROSS SCORE HORIZONTAL
            if (self.checkWin[0] and self.checkWin[1] and self.checkWin[2]) == 'X':
                self.score_X+= 1
            if (self.checkWin[3] and self.checkWin[4] and self.checkWin[5]) == 'X':
                self.score_X += 1
            if (self.checkWin[6] and self.checkWin[7] and self.checkWin[8]) == 'X':
                self.score_X += 1



    def reset_stats(self):

        self.case_1 = True
        self.case_2 = True
        self.case_3 = True
        self.case_4 = True
        self.case_5 = True
        self.case_6 = True
        self.case_7 = True
        self.case_8 = True
        self.case_9 = True

        self.checkWin = [
            '-', '&', 'é',
            '=', '(', '.',
            'è', '_', 'ç'
        ]

    def end_game(self):
        if self.win():
            self.reset_stats()

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode(SIZE)
screen.fill(LIGHT)

game = Game()

font = pygame.font.Font('freesansbold.ttf',16)
game.draw_lines()

while True:

    clock.tick()

    player_X = font.render(f'PLAYER X : {game.score_X}', True, DARK, LIGHT)
    player_O = font.render(f'PLAYER O : {game.score_O}', True, DARK, LIGHT)

    pos_mouse = pygame.mouse.get_pos()
    set_pos_mouse_x = pos_mouse[0]
    set_pos_mouse_y = pos_mouse[1]

    keypress = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if keypress[pygame.K_SPACE]:
            game.menu()
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        if event.type == pygame.MOUSEBUTTONDOWN:
            for case in game.cases:
                if case:
                    game.round()
                    game.cross()

        if game.win():
            game.update_score()
            game.win()
            game.end_game()
            screen.fill(LIGHT)
            game.draw_lines()

    screen.blit(player_X, (80,20))
    screen.blit(player_O, (300,20))
    pygame.display.flip()
