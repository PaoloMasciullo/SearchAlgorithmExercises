from exercises.water_pouring.problem import WaterPouring
from exercises.water_pouring.strategies import *
from search.tree_search import TreeSearch

jugs_capacity = (3, 5)
initial_state = (0, 0)
goal_state = 4

problem = WaterPouring(initial_state=initial_state,
                       goal_state=goal_state,
                       jugs_capacity=jugs_capacity)

print('\nGraph Uniform Cost')
strategy = GraphUniformCost()


search = TreeSearch(problem=problem, strategy=strategy)

result, node = search.run()
actions = node.path()
print(f"Initial_state -->{initial_state}")
state = tuple(initial_state)
for action in actions:
    state = problem.result(state, action)
    print(f'Action: {action}')
    print(f"NextState -->\n{state}")


print(f'result: {result}')
print(f'state: {node.state}')
print(f'actions path: {actions}')
print(f'cost: {node.cost}')
print(f'depth: {node.depth}')

print('\nA*')
strategy = Astar(problem)

search = TreeSearch(problem=problem, strategy=strategy)

result, node = search.run()

actions = node.path()
print(f"Initial_state -->{initial_state}")
state = tuple(initial_state)
for action in actions:
    state = problem.result(state, action)
    print(f'Action: {action}')
    print(f"NextState -->\n{state}")

print(f'result: {result}')
print(f'state: {node.state}')
print(node.path())
print(f'cost: {node.cost}')
print(f'depth: {node.depth}')
