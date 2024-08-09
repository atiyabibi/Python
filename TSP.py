from itertools import permutations
def calculate_Distance(tour,distances):
    total_distance=0
    for i in range(len(tour)-1):
        total_distance+=distances[tour[i]][tour[i+1]]
    total_distance+=distances[tour[-1]][tour[0]]
    return total_distance
def TSP(distances):
    cities=range(len(distances))
    optimal_tour=None
    min_distance=float('inf')
    for tour in permutations(cities):
        print(tour)
        distance=calculate_Distance(tour,distances)
        if distance<min_distance:
            min_distance=distance
            optimal_tour=tour
    return optimal_tour,min_distance
distance_matrix=[
    [0,10,15,20],
    [10,0,35,25],
    [15,35,0,30],
    [20,25,30,0]]
optimal_tour,min_distance=TSP(distance_matrix)
print("Optimal Tour:",optimal_tour)
print("Minimum Distance",min_distance)
