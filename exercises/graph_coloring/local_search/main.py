from exercises.graph_coloring.local_search.problem import GraphColoringProblem
from search.local_search import *

nodes = ['WA', 'NT', 'Q', 'NSW', 'V', 'SA', 'T']
colors = ['r', 'g', 'b']

map_adjacent_nodes = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'Q': ['NT', 'SA', 'NSW'],
    'NSW': ['Q', 'V', 'SA'],
    'V': ['NSW', 'SA'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'T': []
}


problem = GraphColoringProblem(initial_state={}, nodes=nodes, colors=colors, map_adjacent_nodes=map_adjacent_nodes)

print()
# search algorithm
search = HillClimbing(problem=problem)
# run algorithm
print(f'\n{search}')
result, state = search.run()

# display the exercises
print(f'result: {result}')
print(f'value function: {problem.value(state)}')
print(state)

search = SimulatedAnnealing(problem=problem, max_time=1000, lam=0.01)
# search = Genetic(problem=problem, population=50, generations=100, p_mutation=0.1, gene_pool=list(range(8)))

# run algorithm
print(f'\n{search}')
result, state = search.run()

# display the exercises
print(f'result: {result}')
print(f'value function: {problem.value(state)}')
print(state)
