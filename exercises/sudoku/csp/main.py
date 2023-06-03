from csp.ac3 import AC3
from csp.contraints import DifferentValues
from csp.problem import CSP
from exercises.sudoku.csp.backtracking import *

# the letters are the columns of the board while the numbers are the rows

letters = ['A', 'B', 'C', 'D']
variables = [letter + str(i) for letter in letters for i in range(4)]

# init_vars_assigned = [('A' + str(i), val) for i, val in zip([0, 1, 3, 4, 5], [5, 6, 8, 4, 7])] \
#                      + [('B' + str(i), val) for i, val in zip([0, 2, 6], [3, 9, 6])] \
#                      + [('C' + str(i), val) for i, val in zip([2], [8])] \
#                      + [('D' + str(i), val) for i, val in zip([1, 4, 7], [1, 8, 4])] \
#                      + [('E' + str(i), val) for i, val in zip([0, 1, 3, 5, 7, 8], [7, 9, 6, 2, 1, 8])] \
#                      + [('F' + str(i), val) for i, val in zip([1, 4, 7], [5, 3, 9])] \
#                      + [('G' + str(i), val) for i, val in zip([6], [2])] \
#                      + [('H' + str(i), val) for i, val in zip([2, 6, 8], [6, 8, 7])] \
#                      + [('I' + str(i), val) for i, val in zip([3, 4, 5, 7, 8], [3, 1, 6, 5, 9])]

init_vars_assigned = [('A0', 4), ('C0', 1), ('B3', 1), ('D3', 3)]

domains = {
    var: [i for i in range(1, 5)] for var in variables
}

for x in init_vars_assigned:
    domains[x[0]] = [x[1]]

blocks = [[var for var in variables for i in range(2) for letter in letters[j:j + 2] if
           str(var).endswith(str(i)) and str(var).startswith(letter)] for j in range(0, 4, 2)] \
         + [[var for var in variables for i in range(2, 4) for letter in letters[j:j + 2] if
             str(var).endswith(str(i)) and str(var).startswith(letter)] for j in range(0, 4, 2)]
#         + [[var for var in variables for i in range(4, 6) for letter in letters[j:j + 2] if
#             str(var).endswith(str(i)) and str(var).startswith(letter)] for j in range(0, 6, 2)]

constraints = [DifferentValues([var for var in variables if str(var).startswith(letter)]) for letter in letters] \
              + [DifferentValues([var for var in variables if str(var).endswith(str(i))]) for i in range(4)] \
              + [DifferentValues(variables=block) for block in blocks]

initial_state = {}

problem = CSP(variables=variables, domains=domains, constraints=constraints)

search = BackTracking(problem=problem, var_criterion=degree_heuristic, value_criterion=least_constraining_value)
print(search.run(initial_state))
