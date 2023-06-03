from csp.contraints import *


class CSP:

    def __init__(self, variables, domains, constraints):
        self.variables = variables
        self.domains = domains
        self.constraints = constraints
        self.initial_state = dict()

    def consistent(self, state):
        """
        Given a state checks if it is admissible
        @param state: a state
        @return: True or False
        """
        return all([c.check(state) for c in self.constraints])

    def complete(self, state):
        """
        Given a state checks if it is complete
        @param state: a state
        @return: True or False
        """
        return len(state) == len(self.variables)

    def goal_test(self, state):
        """
        A state is a solution if it is complete and admissible
        @param state: a state
        @return: True or False
        """
        return self.complete(state) and self.consistent(state)

    def assign(self, state, variable, value):
        """
        Given a state, a variable and a value assigns that value to that variable obtaining a new state
        @param state: a state
        @param variable: a variable of the problem
        @param value: a possible value
        @return: a new state
        """
        if variable in self.variables and value in self.domains[variable]:
            new_state = dict(state)
            new_state[variable] = value
            return new_state
        raise ValueError

    def rollback(self, state, variable):
        """
        Given a state and a variable removes the assignment to the state
        @param state: a state
        @param variable: a variable of the problem
        @return: a new state
        """
        if variable in self.variables:
            new_state = dict(state)
            del new_state[variable]
            return new_state
        raise ValueError

    def legal_moves(self, state, variable):
        """
        Given a state and a variable returns the list of possible assignments
        @param state: a state
        @param variable: a variable of the problem
        @return: a list of the legal assignments
        """
        possible_assignment = self.domains[variable]
        return [assign for assign in possible_assignment
                if self.consistent(self.assign(state, variable, assign))]

    def count_constraints(self, first_variable, second_variable):
        """
        Given two variables return the number of constraints between the two variables
        @param first_variable: a variable of the problem
        @param second_variable: a different variable of the problem
        @return: the number of constraints
        """
        return sum([1 for c in self.constraints
                    if first_variable in c.variables
                    and second_variable in c.variables])

    def remaining_constraints(self, state, variable):
        """
        Given a state and a variable returns the sum of constraints between the variable and all the other variables
        @param state: a state
        @param variable: a variable
        @return: a number of constraints
        """
        remaining_variables = [var for var in self.variables if var not in state and var != variable]
        if remaining_variables:
            return sum([self.count_constraints(variable, rem_var) for rem_var in remaining_variables])
        else:
            return 0

    def assignable_variables(self, state):
        return [variable for variable in self.variables if variable not in state]

    def remove_inconsistent_values(self, arc, actual_state):
        """
        Given an arc constraint over the variables x_i, x_j check that the values of x_i have at least one value
        in x_j that satisfies the constraint, otherwise remove that value of x_i from its domain
        @param arc: an arc constraint
        @param actual_state: the problem state
        @return: True if some value of x_i has been removed, False otherwise
        """
        # variable of the arc x_i => x_j
        x_i, x_j = arc.variables

        # variable that checks if some value has been removed
        removed = False
        # iterate for all the possible assignments of x_i
        for value_i in self.domains[x_i]:
            # assign the value to x_i
            state = self.assign(state=actual_state,
                                variable=x_i,
                                value=value_i)
            # check the constraint validity for all the possible values of x_j
            assignments = [arc.check(self.assign(state=state,
                                                 variable=x_j,
                                                 value=value_j)) for value_j in self.domains[x_j]]
            # if there are no possible assignments
            if not any(assignments):
                # remove the value from the domain of x_i
                self.domains[x_i].remove(value_i)
                print(f'removing {value_i} from {x_i}')
                removed = True
        return removed
