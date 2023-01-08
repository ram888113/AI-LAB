  # Python3 program for the above approach

from typing import DefaultDict


INT_MAX = 2147483647

# Function to find the minimum
# cost path for all the paths
def findMinRoute(tsp):
	sum = 0
	counter = 0
	j = 0
	i = 0
	min = INT_MAX
	visitedRouteList = DefaultDict(int)
	
	visitedRouteList[0] = 1
	route = [0] * len(tsp)

	while i < len(tsp) and j < len(tsp[i]):
		if counter >= len(tsp[i]) - 1:
			break

		if j != i and (visitedRouteList[j] == 0):
			if tsp[i][j] < min:
				min = tsp[i][j]
				route[counter] = j + 1

		j += 1

		if j == len(tsp[i]):
			sum += min
			min = INT_MAX
			visitedRouteList[route[counter] - 1] = 1
			j = 0
			i = route[counter] - 1
			counter += 1

	i = route[counter - 1] - 1

	for j in range(len(tsp)):

		if (i != j) and tsp[i][j] < min:
			min = tsp[i][j]
			route[counter] = j + 1

	sum += min

	print("Minimum Cost is :", sum)

if __name__ == "__main__":

	tsp = [[-1, 7,11,12, 15], [7, -1, 20,10,12], [11,20,-1,13,17], [12,10,13,-1,5],[15,12,17,5,-1]]
	findMinRoute(tsp)
