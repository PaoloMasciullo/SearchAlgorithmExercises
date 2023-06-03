from exercises.jumping_frogs_puzzle.search.problem import JumpingFrogPuzzle
from exercises.jumping_frogs_puzzle.search.strategies import *
from search.local_search import SimulatedAnnealing, HillClimbing
from search.tree_search import TreeSearch

n = 2
initial_state = tuple((n * 'L' + '.' + n * 'R'))
goal_state = tuple((n * 'R' + '.' + n * 'L'))

problem = JumpingFrogPuzzle(initial_state=initial_state, goal_state=goal_state)

# Goal-based Search
print('---------------------------------------------------------------------')
print('GOAL-BASED SEARCH')
strategies = [BreadthFirst(), GraphBreadthFirst(), DepthFirst(), GraphDepthFirst(), GraphDepthLimited(limit=120),
              Greedy(problem=problem), Astar(problem=problem)]
for strategy in strategies:
    print(f'\n\nRunning {strategy}')
    print(f'initial state: {initial_state}')
    search = TreeSearch(problem=problem, strategy=strategy)

    # run algorithm
    result, node = search.run()
    actions = node.path()
    print(f"Initial_state -->{initial_state}")
    state = tuple(initial_state)
    for action in actions:
        state = problem.result(state, action)
        print(f'Action: {action}')
        print(f"NextState -->\n{state}")
    # display the exercises
    print(result)
    print(f'reached state: {node.state}')
    print(node.path())
    print(f'Cost: {node.cost}')
    print(f'Depth: {node.depth}')
print('\n\n---------------------------------------------------------------------')
print('LOCAL SEARCH')
searches = [HillClimbing(problem=problem), SimulatedAnnealing(problem=problem)]
for search in searches:
    print(f'\n\nRunning {search}')
    result, state = search.run()
    actions = node.path()
    print(f"Initial_state -->{initial_state}")
    state = tuple(initial_state)
    for action in actions:
        state = problem.result(state, action)
        print(f'Action: {action}')
        print(f"NextState -->\n{state}")
    # display the exercises
    print(result)
    print(problem.value(state))
    print(state)
