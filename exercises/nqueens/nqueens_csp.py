from csp.ac3 import AC3
from csp.backtracking import BackTracking, least_constraining_value, degree_heuristic, least_constraining_value
from csp.contraints import Constraint, DifferentValues
from csp.problem import CSP


# uso la constraint DifferentValues per imporre che le regine non devono trovarsi sulla stessa riga.
# definisco DiagonalConstraint che estende la classe Constraint per imporre che non ci siano conflitti sulle diagonali
class DiagonalConstraint(Constraint):
    def conflicts(self, state):
        board = [state['x_' + str(i)] for i in range(len(state)) if 'x_' + str(i) in state.keys()]
        conflicts = 0
        for col1 in range(len(board)):
            queen1 = board[col1]
            for col2 in range(col1 + 1, len(board)):
                queen2 = board[col2]
                if queen1 - col1 == queen2 - col2 or queen1 + col1 == queen2 + col2:
                    conflicts += 1
        return conflicts

    def check(self, state):
        if self.conflicts(state) == 0:
            return True
        else:
            return False


def print_chess(state):
    print('\t', end='')
    for number in range(1, n + 1):
        print(f"|  {number}  ", end='')
    print('|', end='')
    print('\n\t_________________________________________________')

    for row, letter in zip(range(n), ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                                      'Q', 'R', 'S', 'T', 'U', 'V', 'Z']):
        print(letter + '\t', end='')
        print('|', end='')

        for queen in state:
            if queen == row:
                print('  Q  ', end='')
            else:
                print('     ', end='')
            print('|', end='')
        print('\n', end='')
        print('\t_________________________________________________')


# modello il problema assumendo che le regine si trovino ognuna su una colonna diversa della scacchiera, mentre
# le righe in cui si trovano le regine vengono rappresentate dalle variabili (una per ogni riga)
# in questo modo modello il problema come un CSP e posso adottate l'algoritmo di Backtracking per assegnare le variabili
# (righe in cui posizionare le regine)

n = 8
map_variables = ['x_' + str(i) for i in range(n)]

map_domains = {}
for i in range(n):
    map_domains[map_variables[i]] = [i for i in range(n)]

initial_state = {}

map_constraints = [
    DifferentValues(variables=map_variables),  # constraint sulle righe
    DiagonalConstraint(variables=map_variables)  # constraint sulle diagonali
]

problem = CSP(variables=map_variables, domains=map_domains, constraints=map_constraints)

# effettuo un preprocessing sui domini adottando l'algoritmo AC3 che impone l'arc consistency sui domini delle variabili
# coinvolte in una constraint, alla fine del preprocessing si spera di avere dei domini ridotti rispetto alla situazione
# di partenza
optimizer = AC3(csp=problem)
optimizer.run(initial_state)

search = BackTracking(problem=problem, value_criterion=least_constraining_value, var_criterion=least_remaining_values)
# effettuo il run dell'algoritmo con l'utilizzo del forward checking, che contestualmente all'assegnazione di una
# variabile va ad imporre l'arc consistency sui domini delle variabili coinvolte in una o più constraint con la
# variabile appena assegnata
s = search.run(initial_state)

print_chess(s.values())
