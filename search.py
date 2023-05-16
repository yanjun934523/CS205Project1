import queue
from node import Node

def make_queue(node):
    priority_queue = queue.PriorityQueue()
    priority_queue.put((node.path_cost, node))
    return priority_queue

def expand(parent, operators):
    children = []
    for operator in operators:
        child = operator(parent.state)
        if child is not None:
            children.append(Node(child, parent, parent.path_cost + 1))
    parent.children.extend(children)
    return children

def ucs_queueing_function(nodes, children, goal_state):
    for child in children:
        nodes.put((child.path_cost, child))
    return nodes

def a_star_misplaced_tile(nodes, children, goal_state):
    def misplaced_tile(state, goal):
        misplaced_count = 0
        for s, g in zip(state, goal):
            if s != g:
                misplaced_count += 1
        return misplaced_count

    for child in children:
        heuristic = misplaced_tile(child.state, goal_state)
        priority = child.path_cost + heuristic
        nodes.put((priority, child))
    return nodes

def a_star_manhatten_distance(nodes, children, goal_state):
    def manhattan_distance(state, goal):
        distance = 0
        for i in range(1, 9):
            s = divmod(state.index(i), 3)
            g = divmod(goal.index(i), 3)
            distance += abs(s[0] - g[0]) + abs(s[1] - g[1])
        return distance

    for child in children:
        heuristic = manhattan_distance(child.state, goal_state)
        priority = child.path_cost + heuristic
        nodes.put((priority, child))
    return nodes

def general_search(problem, queueing_function):
    nodes = make_queue(Node(problem.initial_state))
    closed_set = set()

    while True:
        if nodes.empty():
            return "failure"
        
        node = nodes.get()[1]

        if problem.goal_test(node.state):
            return node

        if node.state not in closed_set:
            closed_set.add(node.state)
            nodes = queueing_function(nodes, expand(node, problem.operators), problem.goal_state)
    
