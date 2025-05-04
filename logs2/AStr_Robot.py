import heapq
import math

class RobotState:
    def __init__(self, position, parent=None, action=None):
        self.position = position
        self.parent = parent
        self.action = action
        self.g = 0  # cost from start
        if parent:
            self.g = parent.g + 1

    def __eq__(self, other):
        return isinstance(other, RobotState) and self.position == other.position

    def __lt__(self, other):
        # Compare based on f = g + h
        return (self.g + self.heuristic(RobotState.goal)) < (other.g + other.heuristic(RobotState.goal))

    def __hash__(self):
        return hash(self.position)

    def heuristic(self, goal_position):
        # Euclidean distance heuristic
        return math.hypot(self.position[0] - goal_position[0], self.position[1] - goal_position[1])

    def get_successors(self, grid):
        successors = []
        rows, cols = len(grid), len(grid[0])
        x, y = self.position
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] != 1:
                successors.append(RobotState((nx, ny), self))
        return successors


def a_star_robot(grid, start, goal):
    # Attach goal for heuristic
    RobotState.goal = goal
    open_list = []
    closed_set = set()
    start_state = RobotState(start)
    heapq.heappush(open_list, (start_state.g + start_state.heuristic(goal), start_state))

    while open_list:
        _, current = heapq.heappop(open_list)
        if current.position == goal:
            # Reconstruct the path of states
            path_states = []
            while current:
                path_states.append(current)
                current = current.parent
            return list(reversed(path_states))

        closed_set.add(current)
        for successor in current.get_successors(grid):
            if successor not in closed_set:
                heapq.heappush(open_list, (successor.g + successor.heuristic(goal), successor))

    return None


def main():
    # Hardcoded grid, start, and goal
    grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    start = (0, 0)
    goal = (4, 4)

    print("Robot Navigation using A* Search")
    print("Grid:")
    for row in grid:
        print(row)

    path = a_star_robot(grid, start, goal)

    if path:
        print("\nPath found:")
        for state in path:
            print(state.position)
        print(f"Total steps: {len(path) - 1}")
    else:
        print("\nNo path found from start to goal.")

if __name__ == "__main__":
    main()
