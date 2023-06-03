class BreadthFirst:
    def add_visited(self, state):
        pass

    def select(self, fringe, new_nodes):
        new_fringe = new_nodes + fringe  # FIFO
        return new_fringe


class GraphBreadthFirst:
    def __init__(self):
        self.visited = set()

    def add_visited(self, state):
        self.visited.add(state)

    def select(self, fringe, new_nodes):
        new_fringe = new_nodes + fringe  # FIFO
        new_fringe = [n for n in new_fringe if n.state not in self.visited]
        return new_fringe


class DepthFirst:
    def add_visited(self, state):
        pass

    def select(self, fringe, new_nodes):
        new_fringe = fringe + new_nodes  # LIFO
        return new_fringe


class GraphDepthFirst:
    def __init__(self):
        self.visited = set()

    def add_visited(self, state):
        self.visited.add(state)

    def select(self, fringe, new_nodes):
        new_fringe = fringe + new_nodes  # LIFO
        new_fringe = [n for n in new_fringe if n.state not in self.visited]
        return new_fringe


class GraphDepthLimited:
    def __init__(self, limit):
        self.visited = set()
        self.limit = limit

    def add_visited(self, state):
        self.visited.add(state)

    def select(self, fringe, new_nodes):
        new_fringe = fringe + new_nodes  # LIFO
        new_fringe = [n for n in new_fringe if n.state not in self.visited and n.depth <= self.limit]
        return new_fringe


class GraphUniformCost:
    def __init__(self):
        self.visited = set()

    def add_visited(self, state):
        self.visited.add(state)

    def select(self, fringe, new_nodes):
        new_fringe = fringe + new_nodes
        new_fringe = [n for n in new_fringe if n.state not in self.visited]
        new_fringe = sorted(new_fringe, key=lambda n: - n.cost)
        return new_fringe


class Gready:
    def __init__(self, problem):
        self.problem = problem
        self.visited = set()

    def add_visited(self, state):
        self.visited.add(state)

    def select(self, fringe, new_nodes):
        new_fringe = fringe + new_nodes
        new_fringe = [n for n in new_fringe if n.state not in self.visited]
        new_fringe = sorted(new_fringe, key=lambda n: - self.problem.h(n.state))
        return new_fringe


class Astar:
    def __init__(self, problem):
        self.problem = problem
        self.visited = set()

    def add_visited(self, state):
        self.visited.add(state)

    def select(self, fringe, new_nodes):
        new_fringe = fringe + new_nodes
        new_fringe = [n for n in new_fringe if n.state not in self.visited]
        new_fringe = sorted(new_fringe, key=lambda n: - (n.cost + self.problem.h(n.state)))
        return new_fringe
