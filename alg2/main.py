A1 = [[1, 0 ,1, 0, 0], [0, 0, 1, 1, 0], [0, 1, 1, 1, 1], [1, 0, 1, 0, 0]]
prox_coords = [(1, 0), (-1, 0), (0, 1), (0, -1)]
islands = {}
neighbors = set()
largest = 0
land_id = []

def in_bounds(matrix, i, j):
    if i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix[0]):
        return False
    return True

def dfs_traverse(matrix, i, j):
    if not in_bounds(matrix, i, j) or matrix[i][j] == 'x':
        return 0
    if matrix[i][j] == 1:
        for px, py in prox_coords:
            if in_bounds(matrix, i + px, j + py) and matrix[i + px][j + py] != 1:
                neighbors.add((i,j))
        return 0

    matrix[i][j] = 'x'
    islands[(i, j)] = len(land_id)
    size = 1 + dfs_traverse(matrix, i+1, j) + dfs_traverse(matrix, i-1, j) + dfs_traverse(matrix, i, j+1) + dfs_traverse(matrix, i, j-1)
    return size

def track_landmass(matrix):
    global largest
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            land_size = dfs_traverse(matrix, row, col)
            largest = max(largest, land_size)
            if land_size > 0:
                land_id.append(land_size)

track_landmass(A1)
print(islands)
print(land_id)
for nx, ny in neighbors:
    new_land = 1
    landmass = set()
    for px, py in prox_coords:
        if in_bounds(A1, nx + px, ny + py) and (nx + px, ny + py) in islands and islands[(nx + px, ny + py)] not in landmass:
            new_land += land_id[islands[(nx+px, ny+py)]]
            landmass.add(islands[(nx+px, ny+py)])
    largest = max(largest, new_land)

print(largest)
