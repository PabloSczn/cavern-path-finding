# Caverns Routing Application

## Description

This application implements an advanced A* search algorithm to navigate through a series of underground caverns connected by straight tunnels. The (conceptual) robot is given a map of the caverns and tunnels, represented by the coordinates of the center of each cavern and a binary matrix showing which caverns can be reached from which other caverns. The task is to find the shortest route from the first cavern to the last cavern.

## Features

- **A* Search Algorithm**: Efficiently finds the shortest path from the start cavern to the end cavern using the A* search algorithm, which combines the benefits of Dijkstra's algorithm and best-first search.
- **Euclidean Distance Calculation**: Accurately computes the Euclidean distance between caverns to determine the shortest path.
- **Matrix Transposition**: Handles the transposition of the connectivity matrix to ensure accurate pathfinding even if the matrix is not initially in the correct format.
- **Dynamic File Handling**: Reads cavern data from specified files and writes the solution to an output file, ensuring flexibility and ease of use.
- **Command Line Arguments**: Accepts file paths as console parameters, validating them to ensure only specific files are processed. Defaults to a specified file if no parameter is given.

## Files

- **cavern-find-path.py**: The main script containing the implementation.
- **test_files/input1.cav**: Example cavern map file.
- **test_files/input2.cav**: Example cavern map file.
- **test_files/input3.cav**: Example cavern map file.
- **test_files/input4.cav**: Example cavern map file.
- **output.txt**: The file where the output route is appended.

## Requirements

- Python 3.x
- Standard Python libraries: `heapq`, `math`, `sys`

## Usage

1. **Command Line Execution**:
    - To run the program, navigate to the directory containing `cavern-find-path.py` and the `test_files` directory.
    - Use the following command to execute the script:
      ```bash
      python cavern-find-path.py <file_name>
      ```
    - `<file_name>` should be one of the following: `test_files/input1.cav`, `test_files/input2.cav`, `test_files/input3.cav`, `test_files/input4.cav`.
    - Example:
      ```bash
      python cavern-find-path.py test_files/input1.cav
      ```

2. **Default Execution**:
    - If no file name is provided, the program defaults to `test_files/input1.cav`.
    - Example:
      ```bash
      python cavern-find-path.py
      ```

## How It Works

### A* Search Algorithm

The A* search algorithm is used to find the shortest path between the start and end caverns. It uses both the actual distance from the start and the heuristic estimate of the distance to the goal to prioritize paths. This ensures an optimal and efficient search.

### Euclidean Distance Calculation

The Euclidean distance between two caverns is computed to determine the shortest path. This distance is used as part of the heuristic in the A* algorithm.

### Matrix Transposition

The connectivity matrix is transposed if necessary to ensure it correctly represents the connections between caverns. This is important for accurate pathfinding.

### File Handling

The program reads cavern data from a specified `.cav` file, processes it to find the shortest route, and writes the solution to an output file. It accepts the file name as a command line argument, validating it to ensure only specified files are processed. If no file is specified, it defaults to `test_files/input1.cav`.

## Example

To find the shortest route using `test_files/input1.cav`, run:
```bash
python cavern-find-path.py test_files/input1.cav
```

If no file is specified, the program will default to `test_files/input1.cav`:
```bash
python cavern-find-path.py
```

The output route will be printed to the console and appended to `output.txt`.
