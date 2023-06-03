from input.roads import *
from search.problem import *
from search.strategies import *
from search.tree_search import TreeSearch

# load the environment
streets = Roads(streets=roads_small, coordinates=roads_small_coords)

# formulate the problem
initial_state = 'Corato'
goal_state = 'Bari'
map_problem = StreetProblem(environment=streets,
                            initial_state=initial_state,
                            goal_state=goal_state)

# search strategy
strategies = [GraphRandom()]

# search algorithm (Tree Search / Graph Search)
for strategy in strategies:
    search = TreeSearch(problem=map_problem, strategy=strategy)

    # run algorithm
    result, node = search.recursive_run()

    # display the exercises
    print(result)
    print(node)
    print(node.path())
    print(node.cost)
