# search algorithm
from exercises.sudoku.local_search.problem import Sudoku
from search.local_search import *

problem = Sudoku()

n = 2
m = 2
# Genetic(problem=problem, population=50, generations=100, p_mutation=0.1, gene_pool=list(range(n*m)))
searches = [HillClimbing(problem=problem), SimulatedAnnealing(problem=problem, max_time=10000, lam=0.1), Genetic(problem=problem, population=50, generations=100, p_mutation=0.1, gene_pool=list(range(1, n*m + 1)))]

for search in searches:
    print(f'\nRunning {search}')
    # run algorithm
    result, state = search.run()

    # display the exercises
    print(f'result: {result}')
    print(f'value function: {problem.value(state)}')
    print(f'conflicts: {problem.conflicts(state)}')
    print(f'state: {state}')
