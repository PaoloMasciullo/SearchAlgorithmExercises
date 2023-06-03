from game.games import DummyGame
from game.search import *

game = DummyGame()
first_player = Random(game=game)
second_player = Minimax(game=game)

state = game.initial_state
moves = game.play(first_player, second_player)

game = DummyGame()
search = AlphaBeta(game=game)


print(search.next_move(game.initial_state))
