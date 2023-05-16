import math

class Problem:
    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.operators = [
            move_up,
            move_down,
            move_left,
            move_right
        ]

    def goal_test(self, state):
        return state == self.goal_state

def move_up(state):
    dim = int(math.sqrt(len(state)))
    state = list(state)
    i = state.index(0)
    # Locate
    row = i // dim
    col = i % dim
    new_row, new_col = row - 1, col
    if 0 <= new_row < dim and 0 <= new_col < dim:
        new_i = new_row * dim + new_col
        state[i], state[new_i] = state[new_i], state[i]
        return tuple(state)
    # Can't move out of boundary.
    else:
        return None

def move_down(state):
    dim = int(math.sqrt(len(state)))
    state = list(state)
    i = state.index(0)
    row = i // dim
    col = i % dim
    new_row, new_col = row + 1, col
    if 0 <= new_row < dim and 0 <= new_col < dim:
        new_i = new_row * dim + new_col
        state[i], state[new_i] = state[new_i], state[i]
        return tuple(state)
    # Can't move out of boundary.
    else:
        return None

def move_left(state):
    dim = int(math.sqrt(len(state)))
    state = list(state)
    i = state.index(0)
    row = i // dim
    col = i % dim
    new_row, new_col = row, col - 1
    if 0 <= new_row < dim and 0 <= new_col < dim:
        new_i = new_row * dim + new_col
        state[i], state[new_i] = state[new_i], state[i]
        return tuple(state)
    # Can't move out of boundary.
    else:
        return None

def move_right(state):
    dim = int(math.sqrt(len(state)))
    state = list(state)
    i = state.index(0)
    row = i // dim
    col = i % dim
    new_row, new_col = row, col + 1
    if 0 <= new_row < dim and 0 <= new_col < dim:
        new_i = new_row * dim + new_col
        state[i], state[new_i] = state[new_i], state[i]
        return tuple(state)
    # Can't move out of boundary.
    else:
        return None