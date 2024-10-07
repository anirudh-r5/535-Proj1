# Code Author: Anirudh Ramakrishnan (anirudh.r@csu.fullerton.edu)
# Input matrix
A1 = [[1, 0 ,1, 0, 0], [0, 0, 1, 1, 0], [0, 1, 1, 1, 1], [1, 0, 1, 0, 0]]

# List of directions to check around for neighbors
prox_coords = [(1, 0), (-1, 0), (0, 1), (0, -1)]

# Map of co-ordinates and the index of the landmass they belong to
islands = {}

# Set of "water" (1) co-ordinates that vertically/horizontally neighbor a "land" (0) co-ordinate
neighbors = set()

# Tracks current largest landmass
largest = 0

# List of "landmasses'" sizes
land_id = []

# Function to check the given co-ordinates are in bounds of the matrix
def in_bounds(matrix, i, j):
    if i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix[0]):
        return False
    return True

# Function to perform depth-first traversal to discover size/area of landmasses
def dfs_traverse(matrix, i, j):
    if not in_bounds(matrix, i, j) or matrix[i][j] == 'x':
        return 0
    # Add "water" (1) squares to the neighbors set if they neighbor a "land" square
    if matrix[i][j] == 1:
        for px, py in prox_coords:
            if in_bounds(matrix, i + px, j + py) and matrix[i + px][j + py] != 1:
                neighbors.add((i,j))
        return 0
    # Mark co-ordinate as an 'x' when being traversed for the first time
    matrix[i][j] = 'x'

    # Add the co-ordinate to the islands dict with the current land_id index as the value
    # This ensures we accurately track each distinct landmass & the "lands" (0) that are part of it
    islands[(i, j)] = len(land_id)
    # Recursively traverse the neighboring squares until fully exhausted
    size = 1 + dfs_traverse(matrix, i+1, j) + dfs_traverse(matrix, i-1, j) + dfs_traverse(matrix, i, j+1) + dfs_traverse(matrix, i, j-1)
    return size

# Iterate over each element of the matrix, call DFS traversal and track largest landmass size
for row in range(len(A1)):
    for col in range(len(A1[row])):
        land_size = dfs_traverse(A1, row, col)
        largest = max(largest, land_size)
        # Store size of currently traversed landmass in the current index & then increase the index by 1
        if land_size > 0:
            land_id.append(land_size)

# Iterate over the "water" (1) coordinates that neighbor the "land" (1 or 'x') squares
for nx, ny in neighbors:
    new_land = 1
    landmass = set()
    # Check all the vertical/horizontal adjacent squares to find additional landmasses
    for px, py in prox_coords:
        # Check if the square is valid, is a landmass, and has not already been calculated
        if in_bounds(A1, nx + px, ny + py) and (nx + px, ny + py) in islands and islands[(nx + px, ny + py)] not in landmass:
            # Add the size of the adjacent landmass
            new_land += land_id[islands[(nx+px, ny+py)]]
            # Track the landmass to make sure it isn't recounted
            landmass.add(islands[(nx+px, ny+py)])
    # Check if the new size is the largest landmass
    largest = max(largest, new_land)

print(f'Largest landmass size: {largest}')
