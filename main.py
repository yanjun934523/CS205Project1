from problem import Problem
from search import general_search, ucs_queueing_function, a_star_misplaced_tile, a_star_manhatten_distance
from node import print_states
import time
import matplotlib.pyplot as plt

ucs_times = []
astar_misplaced_times = []
astar_manhattan_times = []

depth_0 = (1,2,3,4,5,6,7,8,0)
depth_2 = (1,2,3,4,5,6,0,7,8)
depth_4 = (1,2,3,5,0,6,4,7,8)
depth_8 = (1,3,6,5,0,2,4,7,8)
depth_12 = (1,3,6,5,0,7,4,8,2)
depth_16 = (1,6,7,5,0,3,4,8,2)
depth_20 = (7,1,2,4,8,5,6,3,0)
depth_24 = (0,7,2,4,6,1,3,5,8)

goal_state = (1, 2, 3, 4, 5, 6, 7, 8, 0)
# initial_state = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 0, 15)
# goal_state = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0)
# initial_state = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 0, 24)
# goal_state = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 0)

for initial_state in [depth_0, depth_2, depth_4, depth_8, depth_12, depth_16, depth_20, depth_24]:
    problem = Problem(initial_state, goal_state)

    start_time = time.time()
    print("Solving 8-puzzle using Uniform Cost Search:")
    solution_ucs = general_search(problem, ucs_queueing_function)
    # print_states(solution_ucs)
    ucs_time = time.time() - start_time
    ucs_times.append(ucs_time)
    print()

    start_time = time.time()
    print("Solving 8-puzzle using A* with the Misplaced Tile heuristic:")
    solution_astar_misplaced = general_search(problem, a_star_misplaced_tile)
    # print_states(solution_astar_misplaced)
    astar_misplaced_time = time.time() - start_time
    astar_misplaced_times.append(astar_misplaced_time)
    print()

    start_time = time.time()
    print("Solving 8-puzzle using A* with the Manhattan Distance heuristic:")
    solution_astar_manhattan = general_search(problem, a_star_manhatten_distance)
    # print_states(solution_astar_manhattan)
    astar_manhattan_time = time.time() - start_time
    astar_manhattan_times.append(astar_manhattan_time)

    print("Uniform Cost Search takes:", ucs_time, "seconds")
    print("A* with Misplaced Tile heuristic takes:", astar_misplaced_time, "seconds")
    print("A* with the Manhattan Distance heuristic takes:", astar_manhattan_time, "seconds")

depths = [0, 2, 4, 8, 12, 16, 20, 24]
plt.figure(figsize=(10, 5))
plt.plot(depths, ucs_times, marker='o', label='Uniform Cost Search')
plt.plot(depths, astar_misplaced_times, marker='o', label='A* Misplaced Tile')
plt.plot(depths, astar_manhattan_times, marker='o', label='A* Manhattan Distance')
plt.xlabel('Puzzle Depth')
plt.ylabel('Time Cost (s)')
plt.title('Search Method Time Comparison')
plt.legend()
plt.show()