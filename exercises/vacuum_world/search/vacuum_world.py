import math

from exercises.vacuum_world.search.problem import VacuumProblem
from exercises.vacuum_world.search.strategies import *
from search.tree_search import TreeSearch
import numpy as np


n = 2

initial_state = tuple(np.ones((n, n)).flatten())  # when a square is 1 means that it is dirt

goal_state = tuple(np.zeros((n, n)).flatten())  # when a square is 0 means that it is clean

vacuum_position = tuple((0, 0))

map_problem = VacuumProblem(initial_state=initial_state,
                            goal_state=goal_state,
                            vacuum_position=vacuum_position)

# uninformed search strategy
strategies = [GraphBreadthFirst(), GraphDepthFirst(), GraphDepthLimitedSearch(limit=10), GraphUniformCost()]
print('Uninformed search strategies')
for strategy in strategies:
    print(f'\n\n{strategy}')

    search = TreeSearch(problem=map_problem, strategy=strategy)

    # run algorithm
    result, node = search.run()

    # display the exercises
    print(result)
    if result != 'Fail':
        print(node.state.env)
        print(f'path: {node.path()}')
        print(f'depth: {node.depth}')
        print(f'cost: {node.cost}')

# iterative deepening search
print('\n\nIterative Deepening Search')
for l in range(100):
    print(f'Limit: {l}')
    strategy = GraphDepthLimitedSearch(limit=l)

    search = TreeSearch(problem=map_problem, strategy=strategy)

    # run algorithm
    result, node = search.run()

    # display the exercises
    print(result)
    if result != 'Fail':
        print(node.state.env)
        print(f'path: {node.path()}')
        print(f'depth: {node.depth}')
        print(f'cost: {node.cost}')
        break

# informed search strategy
print('Informed search strategies')
# search strategy
strategies = [Gready(problem=map_problem), A_star(problem=map_problem)]

# search algorithm (Tree Search / Graph Search)
for strategy in strategies:
    print(f'\n\n{strategy}')
    search = TreeSearch(problem=map_problem, strategy=strategy)

    # run algorithm
    result, node = search.run()

    # display the exercises
    print(result)
    if result != 'Fail':
        print(node.state.env)
        print(f'path: {node.path()}')
        print(f'depth: {node.depth}')
        print(f'cost: {node.cost}')
