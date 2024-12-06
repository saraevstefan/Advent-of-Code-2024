from time import time

import numpy as np
from numba import jit

with open("6.txt", "r") as f:
    data = f.read()

data = data.split("\n")

L = len(data[0])
C = len(data)


@jit
def out_of_bounds(x, y):
    return x < 0 or y < 0 or x >= L or y >= C

@jit
def get_next_pos(x: int, y: int, direction: int) -> tuple[int, int]:
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    dx, dy = directions[direction]
    return x + dx, y + dy


# obstacle is 1, no obstacle is 0
ObstacleMatrix = np.zeros((L, C), np.uint8)

initial_pos = (0, 0)

for i in range(L):
    for j in range(C):
        if data[i][j] == "#":
            ObstacleMatrix[i][j] = 1
        elif data[i][j] == "^":
            initial_pos = (i, j)

pos = initial_pos


@jit
def get_path(initial_pos, ObstacleMatrix):
    pos = initial_pos
    direction = 0
    path = []
    loop = False
    while True:
        x, y = pos
        if (x, y, direction) in path:
            loop = True
            break
        path.append((x, y, direction))
        nx, ny = get_next_pos(x, y, direction)
        if out_of_bounds(nx, ny):
            # if out of bounds, finish
            break
        elif ObstacleMatrix[nx][ny] == 0:
            # if no obstacle, move
            pos = nx, ny
        elif ObstacleMatrix[nx][ny] == 1:
            # if obstacle, turn right
            direction = (direction + 1) % 4
    return path, loop


@jit
def get_number_visited(initial_pos, ObstacleMatrix):
    path, _ = get_path(initial_pos, ObstacleMatrix)
    visited_pos = [(x, y) for x, y, _ in path]
    return len(set(visited_pos))


@jit
def get_possible_positions_for_obstacle(path):
    possible_positions = [(x, y) for x, y, _ in path[1:]]
    return list(set(possible_positions))


@jit
def check_loop(initial_pos, possible_obstacle, ObstacleMatrix):
    ObstacleMatrix[possible_obstacle[0]][possible_obstacle[1]] = 1
    _, loop = get_path(initial_pos, ObstacleMatrix)
    ObstacleMatrix[possible_obstacle[0]][possible_obstacle[1]] = 0
    return loop


def get_number_position_loop(initial_pos, ObstacleMatrix):
    path, _ = get_path(initial_pos, ObstacleMatrix)
    possible_positions = get_possible_positions_for_obstacle(path)
    count = 0
    start_time = time()
    for i, pos in enumerate(possible_positions):
        elapsed_time = time() - start_time
        remaining_time = elapsed_time / (i + 1) * (len(possible_positions) - i - 1)
        print(
            f"Checking position {i + 1: 4}/{len(possible_positions)}. "
            f"E: {elapsed_time:.2f}s, R: {remaining_time:.2f}s",
            end="\r",
        )
        count += check_loop(initial_pos, pos, ObstacleMatrix)
    return count


print(get_number_position_loop(initial_pos, ObstacleMatrix))
