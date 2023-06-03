import random


class GraphRandom:

    def __init__(self):
        self.visited = set()

    def add_visited(self, state):
        self.visited.add(state)

    def select(self, fringe, new_nodes):
        new_fringe = new_nodes + fringe
        new_fringe = [n for n in new_fringe if n.state not in self.visited]
        random.shuffle(new_fringe)
        return new_fringe

    def __repr__(self):
        return type(self).__name__


class BreadthFirst:

    def __init__(self):
        self.visited = set()

    def __repr__(self):
        return type(self).__name__

    def add_visited(self, state):
        pass

    def select(self, fringe, new_nodes):
        new_fringe = new_nodes + fringe  # FIFO
        return new_fringe

    def __repr__(self):
        return type(self).__name__


class GraphBreadthFirst:

    def __init__(self):
        self.visited = set()

    def add_visited(self, state):
        self.visited.add(state)

    def select(self, fringe, new_nodes):
        new_fringe = new_nodes + fringe  # FIFO
        new_fringe = [n for n in new_fringe if n.state not in self.visited]
        return new_fringe

    def __repr__(self):
        return type(self).__name__


class DepthFirst:

    def __init__(self):
        self.visited = set()

    def add_visited(self, state):
        pass

    def select(self, fringe, new_nodes):
        new_fringe = fringe + new_nodes  # LIFO
        return new_fringe

    def __repr__(self):
        return type(self).__name__


class GraphDepthFirst:

    def __init__(self):
        self.visited = set()

    def add_visited(self, state):
        self.visited.add(state)

    def select(self, fringe, new_nodes):
        new_fringe = fringe + new_nodes  # LIFO
        new_fringe = [n for n in new_fringe if n.state not in self.visited]
        return new_fringe

    def __repr__(self):
        return type(self).__name__


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

    def __repr__(self):
        return type(self).__name__


class UniformCost:
    def __init__(self):
        self.visited = set()

    def add_visited(self, state):
        self.visited.add(state)

    def select(self, fringe, new_nodes):
        fringe = fringe + new_nodes
        fringe = [n for n in fringe if n.state not in self.visited]
        # sort fringe following the heuristic function
        fringe = sorted(fringe, key=lambda x: -x.cost)
        return fringe

    def __repr__(self):
        return type(self).__name__


class Greedy:
    def __init__(self, problem):
        self.visited = set()
        self.problem = problem

    def add_visited(self, state):
        self.visited.add(state)

    def select(self, fringe, new_nodes):
        fringe = fringe + new_nodes
        fringe = [n for n in fringe if n.state not in self.visited]
        # sort fringe following the heuristic function
        fringe = sorted(fringe, key=lambda x: -self.problem.h(x.state))
        return fringe

    def __repr__(self):
        return type(self).__name__


class Astar:
    def __init__(self, problem):
        self.visited = set()
        self.problem = problem

    def add_visited(self, state):
        self.visited.add(state)

    def select(self, fringe, new_nodes):
        fringe = fringe + new_nodes
        fringe = [n for n in fringe if n.state not in self.visited]
        # sort fringe following the heuristic function
        fringe = sorted(fringe, key=lambda x: -(x.cost + self.problem.h(x.state)))
        return fringe

    def __repr__(self):
        return type(self).__name__
