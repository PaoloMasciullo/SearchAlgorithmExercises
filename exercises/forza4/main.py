from exercises.forza4.problem import Forza4
from game.search import *

game = Forza4()
dumb = Random(game=game)
ai = Minimax(game=game)

state = game.initial_state
moves = game.play(dumb, dumb)

