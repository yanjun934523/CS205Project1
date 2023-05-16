import math

class Node:
    def __init__(self, state, parent=None, path_cost=0):
        self.state = state
        self.parent = parent
        self.path_cost = path_cost
        self.children = []

    def __lt__(self, other):
        return self.path_cost < other.path_cost

def print_states(node):
    if node.parent:
        print_states(node.parent)

        dim = int(math.sqrt(len(node.state)))
        for i in range(dim):
            for j in range(dim):
                if node.state[i*dim+j] != 0:
                    print(str(node.state[i*dim+j]).ljust(2), end=' ')
                else:
                    print(str(0).ljust(2), end=' ')
            print()
        print()