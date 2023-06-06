import pygame
import random
import math
import time
from collections import namedtuple

pygame.init()
font = "app/fonts/Retro.ttf"
inf = math.inf
GameState = namedtuple('GameState', 'to_move, utility, board, moves')
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Tic-Tac-Toe')
icon = pygame.image.load('app/sprites/icon.png')
pygame.display.set_icon(icon)
pygame.display.update()
run = True


# _______________________________________________________________
# MINMAX
def minmax_search(state, game):
    player = game.to_move(state)

    def max_value(state):
        if game.terminal_test(state):
            return game.utility(state, player)
        v = -inf
        for a in game.actions(state):
            v = max(v, min_value(game.result(state, a)))
        return v

    def min_value(state):
        if game.terminal_test(state):
            return game.utility(state, player)
        v = inf
        for a in game.actions(state):
            v = min(v, max_value(game.result(state, a)))
        return v

    return max(game.actions(state), key=lambda a: min_value(game.result(state, a)))


def evaluate(state, game):
    board = state.board
    player = state.to_move
    size = game.k

    player = 'X'
    enemy = 'O'

    def calc(li, eval):
        s = game.k
        while s:
            if li.count(player) == s and li.count(enemy) == 0:
                eval += (10 ** (s))
            elif li.count(enemy) == s and li.count(player) == 0:
                eval -= (10 ** (s))
            s -= 1
        return eval

    eval = 0
    for i in range(size):
        li = []
        for j in range(size):
            li.append(board.get((i + 1, j + 1), '.'))
        eval = calc(li, eval)
    for j in range(size):
        li = []
        for i in range(size):
            li.append(board.get((i + 1, j + 1), '.'))
        eval = calc(li, eval)

    li = []
    for i in range(size):
        li.append(board.get((i + 1, i + 1), '.'))
    eval = calc(li, eval)

    li = []
    for i in range(size):
        for j in range(size):
            if i + j + 2 == size + 1:
                li.append(board.get((i + 1, j + 1), '.'))
    eval = calc(li, eval)

    return eval


# ______________________________________________________________________________
# Players

def query_player(game, state):
    pass


def minimax_player(game, state):
    return minmax_search(state, game)


class Game:
    def actions(self, state):
        raise NotImplementedError

    def result(self, state, move):
        raise NotImplementedError

    def utility(self, state, player):
        raise NotImplementedError

    def terminal_test(self, state):
        return not self.actions(state)

    def to_move(self, state):
        return state.to_move

    def display(self, state):
        print(state)

    def __repr__(self):
        return '<{}>'.format(self.__class__.__name__)

    def play_game(self, *players):
        state = self.initial
        run = True
        # for event in pygame.event.get():
        #         if event.type == pygame.QUIT:
        #             run = False
        while run:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONUP:
                    pass
            pygame.display.update()

            for player in players:
                time.sleep(0.1)
                run2 = True

                if player == query_player:
                    while run2:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                run2 = False
                                run = False
                            if event.type == pygame.MOUSEBUTTONUP:
                                pos = pygame.mouse.get_pos()
                                i = int(pos[0] / res)
                                j = int(pos[1] / res)
                                print(pos)
                                print(i, j)
                                coord = ((i * res + (1 / 6) * res), (j * res + (1 / 6) * res))
                                print(coord)
                                move = (j + 1, i + 1)
                                run2 = False

                else:
                    move = player(self, state)
                i = move[0] - 1
                j = move[1] - 1
                coord = ((j * res + (1 / 6) * res), (i * res + (1 / 6) * res))
                if state.to_move == 'X':
                    screen.blit(cross, coord)
                else:
                    screen.blit(circle, coord)
                state = self.result(state, move)
                self.display(state)
                print('\n')
                pygame.display.update()
                if self.terminal_test(state):
                    time.sleep(3)
                    return self.utility(state, self.to_move(self.initial))


class TicTacToe(Game):
    def __init__(self, h=3, v=3, k=3):
        self.h = h
        self.v = v
        self.k = k
        moves = [(x, y) for x in range(1, h + 1)
                 for y in range(1, v + 1)]
        self.initial = GameState(to_move='X', utility=0, board={}, moves=moves)

    def actions(self, state):
        return state.moves

    def result(self, state, move):
        if move not in state.moves:
            return state  # Illegal move has no effect
        board = state.board.copy()
        board[move] = state.to_move
        moves = list(state.moves)
        moves.remove(move)
        return GameState(to_move=('O' if state.to_move == 'X' else 'X'),
                         utility=self.compute_utility(board, move, state.to_move),
                         board=board, moves=moves)

    def utility(self, state, player):
        return state.utility if player == 'X' else -state.utility

    def terminal_test(self, state):
        return state.utility != 0 or len(state.moves) == 0

    def display(self, state):
        board = state.board
        for x in range(1, self.h + 1):
            for y in range(1, self.v + 1):
                print(board.get((x, y), '.'), end=' ')
            print()

    def compute_utility(self, board, move, player):
        if (self.k_in_row(board, move, player, (0, 1)) or
                self.k_in_row(board, move, player, (1, 0)) or
                self.k_in_row(board, move, player, (1, -1)) or
                self.k_in_row(board, move, player, (1, 1))):
            return +1 if player == 'X' else -1
        else:
            return 0

    def k_in_row(self, board, move, player, delta_x_y):
        (delta_x, delta_y) = delta_x_y
        x, y = move
        n = 0  # n is number of moves in row
        while board.get((x, y)) == player:
            n += 1
            x, y = x + delta_x, y + delta_y
        x, y = move
        while board.get((x, y)) == player:
            n += 1
            x, y = x - delta_x, y - delta_y
        n -= 1  # Because we counted move itself twice
        return n >= self.k


def text_format(message, textFont, textSize, textColor):
    newFont = pygame.font.Font(textFont, textSize)
    newText = newFont.render(message, 0, textColor)
    return newText


player1 = query_player
player2 = minimax_player
grid_size = 3

res = 96

a = grid_size
screen = pygame.display.set_mode((a * res, a * res))
pygame.display.set_caption('Tic-Tac-Toe')
square = pygame.image.load('app/sprites/square.png')
square = pygame.transform.scale(square, (res, res))
cross = pygame.image.load('app/sprites/x.png')
cross = pygame.transform.scale(cross, (int((2 / 3) * res), int((2 / 3) * res)))
circle = pygame.image.load('app/sprites/o.png')
circle = pygame.transform.scale(circle, (int((2 / 3) * res), int((2 / 3) * res)))
for i in range(grid_size):
    for j in range(grid_size):
        screen.blit(square, (i * res, j * res))
pygame.display.update()

time.sleep(0.5)


def tic_tac_toe():
    TicTacToe(grid_size, grid_size, grid_size).play_game(player1, player2)


if __name__ == "__main__":
    tic_tac_toe()