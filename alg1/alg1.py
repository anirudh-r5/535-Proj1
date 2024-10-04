def taskA_baseline(P):
    for idx, (price, product) in enumerate(P):
        for _, (comp_price, comp_prod) in enumerate(P, start=idx):
            if price + comp_price == 2500:
                return (price,product), (comp_price, comp_prod)
    return(None)

def taskA_optimized(P):
    complement = {}
    for price, product in P:
        comp = 2500 - price
        if comp in complement:
            return (comp, complement[comp]), (price, product)
        else:
            complement[price] = product
    return None

def taskB_baseline(L, R):
    J = []
    for idx, (id, num) in enumerate(L):
        for _, (id2, name) in enumerate(R, start=idx):
            if id == id2:
                J.append((id, num, name))
    return J

def taskB_optimized(L, R):
    hash_set = {id: name for id, name in R}
    J = []
    for id, num in L:
        if id in hash_set:
            J.append((id, num, hash_set[id]))
    return J

P = [(2000, 'beta'), (750, 'delta'), (300, 'eta'), (1500, 'zeta'), (500, 'sigma'), (1000, 'alpha')]
print(f'Baseline Task A output:')
print(taskA_baseline(P))
print(f'Optimized Task A output:')
print(taskA_optimized(P))
print('\n')

L = [(1000, 50), (1001, 75), (1002, 90), (1003, 99), (1004, 95)]
R = [(1010, 'q'), (1003, 'z'), (2005, 'a'), (388109, 'b'), (1001, 'cdef'), (999, 'xaf'), (1000, 'leap')]
print(f'Baseline Task B output:')
print(taskB_baseline(L,R))
print(f'Optimized Task B output:')
print(taskB_optimized(L,R))
