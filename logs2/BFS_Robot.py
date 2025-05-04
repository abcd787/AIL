# b. Robot Navigation problem –
import heapq

# Heuristic: Manhattan Distance
def manhattan_distance(cell, goal):
    return abs(cell[0] - goal[0]) + abs(cell[1] - goal[1])

# Best-First Search algorithm
def best_first_search_robot(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    visited = set()
    heap = []

    # Push the start node with its heuristic value
    heapq.heappush(heap, (manhattan_distance(start, goal), start, [start]))

    while heap:
        heuristic_cost, current, path = heapq.heappop(heap)

        # Check if goal reached
        if current == goal:
            return path

        # Mark the current node as visited
        if current in visited:
            continue
        visited.add(current)

        # Define directions: Right, Left, Down, Up
        directions = [(0,1), (0,-1), (1,0), (-1,0)]

        # Explore neighbors
        for dr, dc in directions:
            r, c = current[0] + dr, current[1] + dc
            neighbor = (r, c)

            # Check if neighbor is valid and not visited
            if 0 <= r < rows and 0 <= c < cols and grid[r][c] == 0 and neighbor not in visited:
                new_path = path + [neighbor]
                heapq.heappush(heap, (manhattan_distance(neighbor, goal), neighbor, new_path))

    return None  # No path found

# Sample Grid and Start/Goal
def main():
    grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]

    start = (0, 0)
    goal = (4, 4)

    print("Robot Navigation using Best-First Search\nGrid:")
    for row in grid:
        print(row)

    path = best_first_search_robot(grid, start, goal)

    if path:
        print("\nPath found:")
        for step in path:
            print(step)
        print(f"Total steps: {len(path) - 1}")
    else:
        print("\nNo path found.")

if __name__ == "__main__":
    main()
