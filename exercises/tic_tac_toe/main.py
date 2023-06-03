from exercises.tic_tac_toe.problem import TicTacToe
from game.search import *

game = TicTacToe()
dumb = Random(game=game)
ai = Minimax(game=game)

state = game.initial_state
moves = game.play(ai, ai)

game = TicTacToe()
