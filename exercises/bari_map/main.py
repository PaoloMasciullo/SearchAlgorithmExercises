from exercises.bari_map.problem import BariRoadsProblem
from exercises.bari_map.strategies import *
from input.roads import *
from search.tree_search import TreeSearch

initial_state = 'Terlizzi'
goal_state = 'Bari'
roads = Roads(streets=roads_small, coordinates=roads_small_coords)

problem = BariRoadsProblem(initial_state=initial_state, goal_state=goal_state, environment=roads)

print('Uninformed Search')
strategies = [BreadthFirst(), GraphBreadthFirst(), GraphDepthFirst(), GraphDepthLimited(limit=10), UniformCost()]
for strategy in strategies:
    print(f'\n\n{strategy}')
    search = TreeSearch(problem=problem, strategy=strategy)
    # run algorithm
    result, node = search.recursive_run()

    # display the exercises
    print(f'Result: {result}')
    print(f'{node.state}')
    print(f'Sequence of actions: \n{node.path()}')
    print(f'Cost: {node.cost}')
    print(f'Depth: {node.depth}')

print('\n\nIterativeDeepening')
for l in range(100):
    print(f'Limit: {l}')
    search = TreeSearch(problem=problem, strategy=GraphDepthLimited(limit=l))
    result, node = search.recursive_run()

    # display the exercises
    print(f'Result: {result}')
    if node:
        print(f'{node.state}')
        print(f'Sequence of actions: \n{node.path()}')
        print(f'Cost: {node.cost}')
        print(f'Depth: {node.depth}')
        break


print('\n\nInformed Search')
strategies = [Greedy(problem=problem), Astar(problem=problem)]
for strategy in strategies:
    print(f'\n\n{strategy}')
    search = TreeSearch(problem=problem, strategy=strategy)
    # run algorithm
    result, node = search.recursive_run()

    # display the exercises
    print(f'Result: {result}')
    print(f'{node.state}')
    print(f'Sequence of actions: \n{node.path()}')
    print(f'Cost: {node.cost}')
    print(f'Depth: {node.depth}')
