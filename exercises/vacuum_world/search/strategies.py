from exercises.vacuum_world.search.problem import VacuumState


# Uninformed Search
class BreadthFirst:

    def __init__(self):
        self.visited = set()

    def add_visited(self, state: VacuumState):
        pass

    def select(self, fringe, new_nodes):
        new_fringe = new_nodes + fringe  # FIFO
        return new_fringe

    def __repr__(self):
        return 'Breadth Search'

class GraphBreadthFirst:

    def __init__(self):
        self.visited = set()

    def add_visited(self, state: VacuumState):
        self.visited.add(tuple((state.env, state.vacuum_position)))

    def select(self, fringe, new_nodes):
        new_fringe = new_nodes + fringe  # FIFO
        new_fringe = [n for n in new_fringe if tuple((n.state.env, n.state.vacuum_position)) not in self.visited]
        return new_fringe

    def __repr__(self):
        return 'Graph Breadth Search'

class DepthFirst:

    def __init__(self):
        self.visited = set()

    def add_visited(self, state: VacuumState):
        pass

    def select(self, fringe, new_nodes):
        new_fringe = fringe + new_nodes  # LIFO
        return new_fringe

    def __repr__(self):
        return 'Depth Search'

class GraphDepthFirst:

    def __init__(self):
        self.visited = set()

    def add_visited(self, state: VacuumState):
        self.visited.add(tuple((state.env, state.vacuum_position)))

    def select(self, fringe, new_nodes):
        new_fringe = fringe + new_nodes  # LIFO
        new_fringe = [n for n in new_fringe if tuple((n.state.env, n.state.vacuum_position)) not in self.visited]
        return new_fringe

    def __repr__(self):
        return 'Graph Depth Search'


class GraphDepthLimitedSearch:
    def __init__(self, limit):
        self.visited = set()
        self.limit = limit

    def add_visited(self, state: VacuumState):
        self.visited.add(tuple((state.env, state.vacuum_position)))

    def select(self, fringe, new_nodes):
        new_fringe = fringe + new_nodes  # LIFO
        new_fringe = [n for n in new_fringe if tuple((n.state.env, n.state.vacuum_position)) not in self.visited and n.depth <= self.limit]
        return new_fringe

    def __repr__(self):
        return 'Graph Depth Limited Search'

class GraphUniformCost:
    def __init__(self):
        self.visited = set()

    def add_visited(self, state: VacuumState):
        self.visited.add(tuple((state.env, state.vacuum_position)))

    def select(self, fringe, new_nodes):
        new_fringe = fringe + new_nodes
        new_fringe = [n for n in new_fringe if tuple((n.state.env, n.state.vacuum_position)) not in self.visited]
        new_fringe = sorted(new_fringe, key=lambda n: -n.cost)
        return new_fringe

    def __repr__(self):
        return 'Graph Uniform Cost'


# Informed Search
class Gready:
    def __init__(self, problem):
        self.visited = set()
        self.problem = problem

    def add_visited(self, state: VacuumState):
        self.visited.add(tuple((state.env, state.vacuum_position)))

    def select(self, fringe, new_nodes):
        new_fringe = fringe + new_nodes
        new_fringe = [n for n in new_fringe if tuple((n.state.env, n.state.vacuum_position)) not in self.visited]
        new_fringe = sorted(new_fringe, key=lambda n: - self.problem.h(state=n.state))
        return new_fringe

    def __repr__(self):
        return 'Gready'


class A_star:
    def __init__(self, problem):
        self.visited = set()
        self.problem = problem

    def add_visited(self, state: VacuumState):
        self.visited.add(tuple((state.env, state.vacuum_position)))

    def select(self, fringe, new_nodes):
        new_fringe = fringe + new_nodes
        new_fringe = [n for n in new_fringe if tuple((n.state.env, n.state.vacuum_position)) not in self.visited]
        new_fringe = sorted(new_fringe, key=lambda n: - (n.cost + self.problem.h(state=n.state)))
        return new_fringe

    def __repr__(self):
        return 'A*'
