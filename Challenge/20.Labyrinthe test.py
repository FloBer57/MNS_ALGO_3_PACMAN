import random

liste_choix = ["z", "q", "s", "d"]
wall = "X"
vide = " "
player = "O"

def print_map(lab):
    for row in lab:
        print(" ".join(row))

def initialize_lab(width, height):
    return [[wall for _ in range(width)] for _ in range(height)]

def prim_maze_generation(lab):
    width, height = len(lab[0]), len(lab)
    start_x, start_y = random.randint(0, width - 1), random.randint(0, height - 1)
    lab[start_y][start_x] = vide

    visited = [[False for _ in range(width)] for _ in range(height)]
    visited[start_y][start_x] = True

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    walls = [(start_x + dx, start_y + dy, start_x, start_y) for dx, dy in directions if 0 <= start_x + dx < width and 0 <= start_y + dy < height]

    while walls:
        wall_x, wall_y, adjacent_x, adjacent_y = random.choice(walls)
        if visited[wall_y][wall_x] != visited[adjacent_y][adjacent_x]:
            lab[wall_y][wall_x] = vide
            visited[wall_y][wall_x] = True
            visited[adjacent_y][adjacent_x] = True

        walls = [(x, y, wall_x, wall_y) for x, y in [(wall_x + 1, wall_y), (wall_x - 1, wall_y), (wall_x, wall_y + 1), (wall_x, wall_y - 1)] if 0 <= x < width and 0 <= y < height and not visited[y][x]]

    return lab

lab = initialize_lab(5, 5)
lab = prim_maze_generation(lab)

# La position de commencement du joueur
player_pos = [0, 0]
lab[player_pos[0]][player_pos[1]] = player

# Je print mon tableau ( Pour chaque valeur dans le tableau, les afficher.)
print_map(lab)
