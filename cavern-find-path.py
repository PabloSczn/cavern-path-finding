import heapq
import math
import sys

# Define a class to represent a cavern with its properties
class Cavern:
    def __init__(self, index, x, y):
        # Unique identifier for the cavern
        self.index = index
        # X-coordinate of the cavern
        self.x = x
        # Y-coordinate of the cavern
        self.y = y
        # Cost from the start node to this cavern (initially set to infinity)
        self.g = math.inf
        # Heuristic estimate of cost from this cavern to the goal
        self.h = math.inf
        # The parent cavern in the path
        self.parent = None

    def __lt__(self, other):
        # Define how instances of Cavern should be compared for the heapq
        return (self.g + self.h) < (other.g + other.h)

# Calculate the Euclidean distance between two caverns
def euclidean_distance(cavern1, cavern2):
    return math.sqrt((cavern1.x - cavern2.x) ** 2 + (cavern1.y - cavern2.y) ** 2)

def a_star_search(connectivity_matrix, caverns):
    # Initialize start and end caverns
    start_cavern = caverns[0]
    end_cavern = caverns[-1]

    # Initialize open set, closed set, and a map to check if a cavern is in the open set
    open_set = []
    heapq.heapify(open_set)
    closed_set = set()
    open_set_map = {}

    # Set initial values for the start cavern
    start_cavern.g = 0
    start_cavern.h = euclidean_distance(start_cavern, end_cavern)
    heapq.heappush(open_set, start_cavern)
    open_set_map[start_cavern] = True

    path = []
    while open_set:
        current = heapq.heappop(open_set)

        # Clear the path as it will be reconstructed
        path.clear()

        if current == end_cavern:
            # Reconstruct the path if the goal cavern is reached
            while current:
                path.append(current.index)
                current = current.parent
            path.reverse()
            return path

        closed_set.add(current)

        # Explore neighbors of the current cavern
        for neighbor_index in range(len(connectivity_matrix[current.index - 1])):
            if connectivity_matrix[current.index - 1][neighbor_index] == 1:
                neighbor = caverns[neighbor_index]
                if neighbor in closed_set:
                    continue
                tentative_g = current.g + euclidean_distance(current, neighbor)
                if tentative_g < neighbor.g:
                    # Remove the old entry from the heap if it exists
                    if neighbor in open_set_map:
                        open_set.remove(neighbor)
                        heapq.heapify(open_set)
                        del open_set_map[neighbor]

                    # Update values for the neighbor cavern
                    neighbor.parent = current
                    neighbor.g = tentative_g
                    neighbor.h = euclidean_distance(neighbor, end_cavern)
                    heapq.heappush(open_set, neighbor)
                    open_set_map[neighbor] = True

    return [0]

# Transpose a square matrix
def transpose_matrix(matrix):
    if len(matrix) != len(matrix[0]):
        return "Input matrix is not square"

    transposed = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

    return transposed

# Read cavern data from a file and return coordinates and connectivity matrix
def read_cav_file(file_path):
    with open(file_path, 'r') as file:
        data = file.read().split(',')

    n = int(data[0])  # Number of caverns
    # Extract coordinates
    coordinates = [(int(data[i]), int(data[i + 1])) for i in range(1, 2 * n + 1, 2)]
    connectivity_data = data[2 * n + 1:]
    connectivity_matrix = [list(map(int, connectivity_data[i:i + n])) for i in range(0, n * n, n)]

    return coordinates, transpose_matrix(connectivity_matrix)

# Find the shortest route in a cavern system given a file path
def find_shortest_route(file_path):
    cavern_coordinates, connectivity_matrix = read_cav_file(file_path)
    caverns = [Cavern(index, x, y) for index, (x, y) in enumerate(cavern_coordinates, start=1)]
    path = a_star_search(connectivity_matrix, caverns)

    if path[0] == 0:
        return path, 0  # No route found, length is 0

    total_length = 0
    for i in range(1, len(path)):
        current_cavern = caverns[path[i] - 1]
        previous_cavern = caverns[path[i - 1] - 1]
        total_length += euclidean_distance(current_cavern, previous_cavern)

    return path, total_length

# Specify file
valid_files = ["test_files/input1.cav", "test_files/input2.cav", "test_files/input3.cav", "test_files/input4.cav"]
default_file = "test_files/input1.cav"

if len(sys.argv) > 1:
    file_choice = sys.argv[1]
    if file_choice in valid_files:
        file_path = file_choice
    else:
        print(f"Invalid file choice. Please choose from: {', '.join(valid_files)}")
        sys.exit(1)
else:
    file_path = default_file
    print(f"No file choice given. Using default file: {file_path}")

shortest_route, route_length = find_shortest_route(file_path)
print(shortest_route)
print("Route Length:", route_length)

with open('output.txt', 'a') as f:
    f.write(str(shortest_route))
