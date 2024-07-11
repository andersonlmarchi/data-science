
def euclidean_distance(x1, x2):
    distance = 0
    for i in range(len(x1)):
        distance += (x1[i] - x2[i]) ** 2

    return distance ** 0.5

print(euclidean_distance([1, 2], [4, 0]))
print(euclidean_distance([5, 4, 3], [1, 7, 9]))

o_poderoso_chefao = [175, 1972, 6000000]
batman_cavalheiro_das_trevas = [152, 2008, 180000000]
matrix = [136, 1999, 63000000]

print(euclidean_distance(o_poderoso_chefao, batman_cavalheiro_das_trevas))
print(euclidean_distance(o_poderoso_chefao, matrix))
print(euclidean_distance(batman_cavalheiro_das_trevas, matrix))
