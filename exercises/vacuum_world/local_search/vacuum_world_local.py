import numpy as np

from exercises.vacuum_world.local_search.problem import VacuumProblem
from search.local_search import HillClimbing, SimulatedAnnealing, Genetic

n = 2

initial_state = tuple(np.ones((n, n)).flatten())
goal_state = tuple(np.zeros((n, n)).flatten())
vacuum_position = tuple((0, 0))

problem = VacuumProblem(initial_state, vacuum_position, goal_state)

print('Hill Climbing')
# search algorithm
search = HillClimbing(problem=problem)

# run algorithm
result, state = search.run()

# display the exercises
print(result)
print(problem.value(state))
print(state.env)

print('\n\n Simulated Annealing')
search = SimulatedAnnealing(problem=problem, max_time=1000, lam=0.01)

# run algorithm
result, state = search.run()

# display the exercises
print(result)
print(problem.value(state))
print(state.env)

print('\n\n Genetic')
search = Genetic(problem=problem, population=50, generations=100, p_mutation=0.1, gene_pool=list(range(n)))

# run algorithm
result, state = search.run()

# display the exercises
print(result)
print(problem.value(state))
print(state)
