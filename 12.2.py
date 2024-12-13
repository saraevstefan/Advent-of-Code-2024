from collections import deque

import numpy as np

np.set_printoptions(threshold=np.inf, linewidth=np.inf)


def letter_to_int(c):
    return ord(c) - ord("A")


def in_bounds(i, j, Map):
    L, C = Map.shape
    return 0 <= i < L and 0 <= j < C


def flood_fill(i, j, Visited, Map):
    q = deque()
    New_Visited = np.zeros_like(Map)

    q.append((i, j))
    Visited[i][j] = 1
    New_Visited[i][j] = 1

    while len(q) > 0:
        i, j = q.popleft()
        for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            x, y = i + di, j + dj
            if in_bounds(x, y, Map) and Map[x][y] == Map[i][j] and Visited[x][y] == 0:
                Visited[x][y] = 1
                New_Visited[x][y] = 1
                q.append((x, y))
    # endwhile
    return New_Visited


def scale_area(area, scale_factor):
    L, C = area.shape

    new_area = np.zeros((L * scale_factor, C * scale_factor), dtype=np.uint8)

    for i in range(L):
        for j in range(C):
            if area[i][j] == 1:
                new_area[i * scale_factor + 1][j * scale_factor + 1] = 1
                prev_i_ok = False
                prev_j_ok = False
                if in_bounds(i - 1, j, area) and area[i - 1][j] == 1:
                    prev_i_ok = True
                    for ni in range((i - 1) * scale_factor + 1, i * scale_factor + 1):
                        new_area[ni][j * scale_factor + 1] = 1
                if in_bounds(i, j - 1, area) and area[i][j - 1] == 1:
                    prev_j_ok = True
                    for nj in range((j - 1) * scale_factor + 1, j * scale_factor + 1):
                        new_area[i * scale_factor + 1][nj] = 1
                if (
                    prev_i_ok
                    and prev_j_ok
                    and in_bounds(i - 1, j - 1, area)
                    and area[i - 1][j - 1] == 1
                ):
                    for ni in range((i - 1) * scale_factor + 1, i * scale_factor + 1):
                        for nj in range(
                            (j - 1) * scale_factor + 1, j * scale_factor + 1
                        ):
                            new_area[ni][nj] = 1
    return new_area


def enlarge_area(area, N):
    L, C = area.shape

    for _ in range(N):
        new_area = np.zeros_like(area)
        for i in range(L):
            for j in range(C):
                if area[i][j] == 1:
                    new_area[i][j] = 1
                    for di, dj in [
                        [0, 1],
                        [0, -1],
                        [1, 0],
                        [-1, 0],
                        [1, 1],
                        [1, -1],
                        [-1, 1],
                        [-1, -1],
                    ]:
                        x, y = i + di, j + dj
                        if in_bounds(x, y, area):
                            new_area[x][y] = 1
        area = new_area
    return area


def cut_unnecessary_area(area):
    L, C = area.shape
    xs, ys = 0, 0
    xe, ye = L, C

    for i in range(0, xe):
        if np.count_nonzero(area[i]) == 0:
            xs += 1
        else:
            break
    for j in range(0, ye):
        if np.count_nonzero(area[:, j]) == 0:
            ys += 1
        else:
            break

    for i in range(L - 1, 0, -1):
        if np.count_nonzero(area[i]) == 0:
            xe -= 1
        else:
            break
    for j in range(C - 1, 0, -1):
        if np.count_nonzero(area[:, j]) == 0:
            ye -= 1
        else:
            break

    return area[xs:xe, ys:ye]


def get_outer_border_of_area(area: np.ndarray):
    enlarged_area = enlarge_area(area, 1)
    outer_border_area = enlarged_area.copy() - area
    return outer_border_area


def get_area_perimeter(Visited):
    area = np.count_nonzero(Visited)
    perimeter = 0

    L, C = Visited.shape

    for i in range(L):
        for j in range(C):
            if Visited[i][j] == 1:
                for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                    if not in_bounds(i + di, j + dj, Visited):
                        perimeter += 1
                    elif Visited[i + di][j + dj] == 0:
                        perimeter += 1

    return area, perimeter


def get_area_sides(Visited):
    area = np.count_nonzero(Visited)
    sides = 0

    Directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    Scaled_Visited = scale_area(Visited, 3)

    Border = get_outer_border_of_area(Scaled_Visited)
    Border_Visited = np.zeros_like(Border)

    L, C = Border.shape

    while np.count_nonzero(Border) != np.count_nonzero(Border_Visited):
        # walk on the border and count number of direction changes
        si, sj = -1, -1

        # first, find a border edge to start counting
        for i in range(L):
            for j in range(C):
                if Border[i][j] == 1 and Border_Visited[i][j] == 0:
                    si, sj = i, j
                    Border_Visited[i][j] = 1
                    break
            if si != -1:
                break

        # found the border
        i, j = si, sj
        found_direction = False
        for Direction, (di, dj) in enumerate(Directions):
            if in_bounds(i + di, j + dj, Border) and Border[i + di][j + dj] == 1:
                found_direction = True
                break

        # if did not find direction, we have one single cell, which means that the number of sides == 4
        if found_direction == False:
            sides += 4
            continue

        # if we found a direction, we increase the number of sides with 1 because we changed direction from (0,0) to the found one
        sides += 1
        start_sides = sides

        # walk on the border
        while (i != si or j != sj) or sides == start_sides:
            # check left, forward, right -- order does not matter, we are ensured that the border is a hamiltonian cycle
            for New_Direction in [
                (Direction + 3) % 4,
                Direction,
                (Direction + 1) % 4,
            ]:
                di, dj = Directions[New_Direction]
                if not in_bounds(i + di, j + dj, Border):
                    continue

                if Border[i + di][j + dj] == 1:
                    i, j = i + di, j + dj
                    Border_Visited[i][j] = 1
                    # if direction change, increase the number of sides
                    if New_Direction != Direction:
                        sides += 1
                        Direction = New_Direction
                    break
                # end if
            # end for
        # end while
    return area, sides


with open("12.txt", "r") as f:
    data = f.read().strip()

Map = np.array(
    [[letter_to_int(x) for x in line] for line in data.split("\n")], dtype=np.uint8
)

Visited = np.zeros_like(Map)

L, C = Map.shape

S = 0

for i in range(L):
    for j in range(C):
        if Visited[i][j] == 0:
            Currently_Visited = flood_fill(i, j, Visited, Map)

            # reduce the area processed to only the bounding box of the filled area -- increase in performance
            Smaller_Currently_Visited = cut_unnecessary_area(Currently_Visited)
            area, sides = get_area_sides(Smaller_Currently_Visited)
            S += area * sides

print(S)
