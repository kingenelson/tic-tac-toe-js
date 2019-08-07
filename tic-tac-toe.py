##################################################
# README
# To use run 'python tic-atc-toe.py' in the dirtecory
# select whether you would like to go first or not
# enter your move via an index. see grid
#
# 0|1|2
# -----
# 4|5|6
# -----
# 6|7|8
#

import random

class Game:
    # 0|1|2
    # -----
    # 4|5|6
    # -----
    # 6|7|8
    def __init__(self):
        self.state = [-1, -1, -1, -1, -1, -1, -1, -1, -1] #O=0, X=1, None=-1
        self.possibleMoves = list(range(0, 9))
        self.turn = 0 #O=0, X=1
        self.done = False
        self.winner = None #O=0, X=1, CAT=-1

    def move(self, move):
        # check if it is a legal move
        if not(move in self.possibleMoves):
            print(f'error with {move} move')
            return # maybe throw exception

        # who's turn is it and make move
        if self.turn == 0:
            # print(self.turn)
            self.state[move] = 0
            self.turn = 1
        else:
            # print(self.turn)
            self.state[move] = 1
            self.turn = 0

        # remove the move from the possibleMoves
        self.possibleMoves.remove(move)

        # compute if the game is done and the winner if so
        for i in range(0, 3):
            if self.state[i] != -1 and self.state[i] == self.state[i+3] and self.state[i] == self.state[i+6]:
                self.done = True
                self.winner = self.state[i]
        for i in range(0, 3):
            i *= 3
            if self.state[i] != -1 and self.state[i] == self.state[i+1] and self.state[i] == self.state[i+2] and not(self.done):
                self.done = True
                self.winner = self.state[i]
        if self.state[0] != -1 and self.state[0] == self.state[4] and self.state[0] == self.state[8] and not(self.done):
            self.done = True
            self.winner = self.state[0]
        if self.state[2] != -1 and self.state[2] == self.state[4] and self.state[2] == self.state[6] and not(self.done):
            self.done = True
            self.winner = self.state[2]
        if len(self.possibleMoves) == 0 and not(self.done):
            self.done = True
            self.winner = -1

    def wouldEnd(self, move, turn):
        if turn == 0:
            self.state[move] = 0
        else:
            self.state[move] = 1

        # sketch(self)


        for i in range(0, 3):
            if self.state[i] != -1 and self.state[i] == self.state[i+3] and self.state[i] == self.state[i+6]:
                self.state[move] = -1
                # print(f'vert at {i}')
                return True
        for i in range(0, 3):
            i *= 3
            if self.state[i] != -1 and self.state[i] == self.state[i+1] and self.state[i] == self.state[i+2] and not(self.done):
                self.state[move] = -1
                # print(f'horz at {i}')
                return True
        if self.state[0] != -1 and self.state[0] == self.state[4] and self.state[0] == self.state[8] and not(self.done):
            self.state[move] = -1
            # print(f'left cross')
            return True
        if self.state[2] != -1 and self.state[2] == self.state[4] and self.state[2] == self.state[6] and not(self.done):
            self.state[move] = -1
            # print(f'right cross')
            return True
        if len(self.possibleMoves) == 0 and not(self.done):
            self.state[move] = -1
            return True
        self.state[move] = -1
        return False

class GameAI:
    def __init__(self, player):
        self.player = player
        self.tree = None

    def makeTree():
        print('test')

    # Does any trival moves and a random move otherwise
    def naiveRandom(self, game, seed=None):
        trival = self.trivalMove(game)
        if len(trival) != 0:
            # Check for a winning move
            for tMove in trival:
                # print(tMove)
                if tMove[0] == self.player:
                    game.move(tMove[1])
                    return tMove[1]
            # If no winning move pick the first move to stop from losing
            game.move(trival[0][1])
            return trival[0][1]
        # If no trival move pick random move
        random.seed(seed)
        move = random.choice(game.possibleMoves)
        game.move(move)
        return move

    def naive(self, game):
        print('test')


    # Returns a trivial move if there is one, None otherwise
    # Trival move = winning move, or stop other player from winning move
    # format = (the player that would end the game if this move would be made, the move)
    def trivalMove(self, game):
        trivalMoves = []
        for move in game.possibleMoves:
            p1 = game.wouldEnd(move, 0)
            p2 = game.wouldEnd(move, 1)
            # print(f'p1: {p1}\np2: {p2}')
            if p1:
                trivalMoves.append((0, move))
            if p2:
                trivalMoves.append((1, move))
        return trivalMoves

def sketch(game):
    state = []
    for i in game.state:
        # print(i)
        if i == 0:
            state.append('O')
        elif i == 1:
            state.append('X')
        else:
            state.append(' ')
    print(f'\n  {state[0]}|{state[1]}|{state[2]}')
    print('  -----')
    print(f'  {state[3]}|{state[4]}|{state[5]}')
    print('  -----')
    print(f'  {state[6]}|{state[7]}|{state[8]}\n')

def play(game):
    human = int(input('Player 1 or 2? ')) - 1
    if human == 1:
        ai = GameAI(0)
    else:
        ai = GameAI(1)
        sketch(game)

    # seed = input('Seed: ')
    # if seed == '':
    #     seed = None

    while not(game.done):
        if human == 1:
            # AI move here
            turn = game.turn + 1
            aimove = ai.naiveRandom(game)
            # Draw
            sketch(game)
            print(f'Player {turn}\'s move: {aimove}')
            # Player move here
            if not(game.done):
                turn = game.turn + 1
                stdin = input(f'Player {turn}\'s move: ')
                game.move(int(stdin))
        else:
            # Player move here
            turn = game.turn + 1
            stdin = input(f'Player {turn}\'s move: ')
            game.move(int(stdin))
            if game.winner == -1:
                sketch(game)
            # AI move here
            if not(game.done):
                turn = game.turn + 1
                aimove = ai.naiveRandom(game)
                # Draw
                sketch(game)
                print(f'Player {turn}\'s move: {aimove}')
    if game.winner == -1:
        winner = 'CAT'
    else:
        sketch(game)
        winner = f'Player {turn}'
    print(f'The winner is {winner}!')


game = Game()
play(game)


