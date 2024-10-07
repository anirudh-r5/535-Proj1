# Code Author: Anirudh Ramakrishnan (anirudh.r@csu.fullerton.edu)
# Task A: Find two products whose prices add up to 2500
def taskA_baseline(P):
    # Iterate over the list of prices and products
    for idx, (price, product) in enumerate(P):
        # For each product, iterate again starting from the current index
        for _, (comp_price, comp_prod) in enumerate(P, start=idx):
            # If the sum of the current price and compared price equals 2500, return the pair
            if price + comp_price == 2500:
                return (price, product), (comp_price, comp_prod)
    # If no such pair is found, return None
    return None

# Optimized version using a dictionary (hash map)
def taskA_optimized(P):
    # Dictionary to store price as key and product as value
    complement = {}
    # Iterate over the list of prices and products
    for price, product in P:
        # Calculate the complement needed to reach 2500
        comp = 2500 - price
        # If the complement is already in the dictionary, return the pair
        if comp in complement:
            return (comp, complement[comp]), (price, product)
        else:
            # Otherwise, store the current price and product in the dictionary
            complement[price] = product
    # If no such pair is found, return None
    return None

# Task B: Join two lists based on matching IDs
def taskB_baseline(L, R):
    # List to store the result of the join
    J = []
    # Iterate over the first list
    for idx, (id, num) in enumerate(L):
        # For each item in the first list, iterate over the second list starting from the current index
        for _, (id2, name) in enumerate(R, start=idx):
            # If the IDs match, append the result (id, num, name) to the result list
            if id == id2:
                J.append((id, num, name))
    return J

# Optimized version using a dictionary (hash map)
def taskB_optimized(L, R):
    # Create a dictionary where the key is the ID and the value is the name from the second list
    hash_set = {id: name for id, name in R}
    # List to store the result of the join
    J = []
    # Iterate over the first list
    for id, num in L:
        # If the ID exists in the dictionary, append the result (id, num, name) to the result list
        if id in hash_set:
            J.append((id, num, hash_set[id]))
    return J

# Test data for Task A
P = [(2000, 'beta'), (750, 'delta'), (300, 'eta'), (1500, 'zeta'), (500, 'sigma'), (1000, 'alpha')]

# Print the results of Task A using both baseline and optimized versions
print(f'Baseline Task A output:')
print(taskA_baseline(P))
print(f'Optimized Task A output:')
print(taskA_optimized(P))
print('\n')

# Test data for Task B
L = [(1000, 50), (1001, 75), (1002, 90), (1003, 99), (1004, 95)]
R = [(1010, 'q'), (1003, 'z'), (2005, 'a'), (388109, 'b'), (1001, 'cdef'), (999, 'xaf'), (1000, 'leap')]

# Print the results of Task B using both baseline and optimized versions
print(f'Baseline Task B output:')
print(taskB_baseline(L,R))
print(f'Optimized Task B output:')
print(taskB_optimized(L,R))
