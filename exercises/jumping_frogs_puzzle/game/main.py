from exercises.jumping_frogs_puzzle.game.problem import JumpingFrogGame
from game.search import Random, Minimax, AlphaBeta

n = 4
initial_state = tuple((n * 'L' + '.' + n * 'R'))

game = JumpingFrogGame(initial_state=initial_state)
first_player = Random(game=game)
second_player = Minimax(game=game)

state = game.initial_state
moves = game.play(first_player, second_player)

game = JumpingFrogGame(initial_state=initial_state)
search = AlphaBeta(game=game)
state = game.initial_state
moves = game.play(first_player, second_player)
