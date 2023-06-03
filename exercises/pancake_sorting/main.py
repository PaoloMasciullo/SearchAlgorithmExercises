from exercises.pancake_sorting.problem import PancakeSorting
from exercises.pancake_sorting.strategies import *
from search.tree_search import TreeSearch

initial_state = (2, 1, 4, 6, 3, 5)
goal_state = tuple(sorted(initial_state))

problem = PancakeSorting(initial_state=initial_state, goal_state=goal_state)

print('\nGraph Uniform Cost')
strategy = GraphBreadthFirst()

search = TreeSearch(problem=problem, strategy=strategy)

result, node = search.run()

print(f'result: {result}')
print(f'state: {node.state}')
print(node.path())
print(f'cost: {node.cost}')
print(f'depth: {node.depth}')

print('\nA*')
strategy = Gready(problem=problem)

search = TreeSearch(problem=problem, strategy=strategy)

result, node = search.run()

print(f'result: {result}')
print(f'state: {node.state}')
print(node.path())
print(f'cost: {node.cost}')
print(f'depth: {node.depth}')
