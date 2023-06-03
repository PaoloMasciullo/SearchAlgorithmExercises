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

