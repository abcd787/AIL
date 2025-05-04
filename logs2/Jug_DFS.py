# Water jug DFS
def water_jug_dfs(capacity1, capacity2, target):
    visited = set()  # To track visited states
    path = []  # To store the solution path

    def dfs(jug1, jug2):
        # If we have already visited this state, return False (avoid cycles)
        if (jug1, jug2) in visited:
            return False
        
        # Mark the state as visited
        visited.add((jug1, jug2))

        # Append the current state to the path
        path.append((jug1, jug2))

        # If the target is achieved in either jug, return True
        if jug1 == target or jug2 == target:
            return True

        # Explore all possible transitions (DFS recursive calls)
        # Fill 3-liter jug
        if dfs(3, jug2):
            return True
        # Fill 5-liter jug
        if dfs(jug1, 5):
            return True
        # Empty 3-liter jug
        if dfs(0, jug2):
            return True
        # Empty 5-liter jug
        if dfs(jug1, 0):
            return True
        # Pour water from 3-liter jug into 5-liter jug
        if dfs(max(0, jug1 - (5 - jug2)), min(5, jug1 + jug2)):
            return True
        # Pour water from 5-liter jug into 3-liter jug
        if dfs(min(3, jug1 + jug2), max(0, jug2 - (3 - jug1))):
            return True

        # If none of the transitions lead to the goal, backtrack
        path.pop()
        return False

    # Start DFS from the initial state (0, 0)
    dfs(0, 0)

    # If we found a solution, return the path
    return path

# Example Usage
capacity1 = 3  # Capacity of the 3-liter jug
capacity2 = 5  # Capacity of the 5-liter jug
target = 4     # Target amount to measure

solution = water_jug_dfs(capacity1, capacity2, target)

if solution:
    print("Solution steps:")
    for step in solution:
        print(step)
else:
    print("No solution found.")
