# Water jug BFS

from collections import deque

def water_jug_bfs(capacity1, capacity2, target):
    visited = set()  # To track visited states
    queue = deque()  # Queue for BFS
    parent = {}  # To store the path
    
    # Start BFS from the initial state (0, 0)
    queue.append((0, 0))
    visited.add((0, 0))
    parent[(0, 0)] = None
    
    while queue:
        jug1, jug2 = queue.popleft()
        
        # If the target is reached, construct the path
        if jug1 == target or jug2 == target:
            path = []
            current_state = (jug1, jug2)
            while current_state is not None:
                path.append(current_state)
                current_state = parent[current_state]
            return path[::-1]
        
        # Possible next states
        next_states = [
            (capacity1, jug2),  # Fill 3-liter jug
            (jug1, capacity2),  # Fill 5-liter jug
            (0, jug2),  # Empty 3-liter jug
            (jug1, 0),  # Empty 5-liter jug
            (max(0, jug1 - (capacity2 - jug2)), min(capacity2, jug1 + jug2)),  # Pour from 3L to 5L
            (min(capacity1, jug1 + jug2), max(0, jug2 - (capacity1 - jug1)))   # Pour from 5L to 3L
        ]
        
        # Process each possible state
        for state in next_states:
            if state not in visited:
                queue.append(state)
                visited.add(state)
                parent[state] = (jug1, jug2)
    
    return None  # No solution found

# Example Usage
capacity1 = 3  # Capacity of the 3-liter jug
capacity2 = 5  # Capacity of the 5-liter jug
target = 4     # Target amount to measure

solution = water_jug_bfs(capacity1, capacity2, target)

if solution:
    print("Solution steps:")
    for step in solution:
        print(step)
else: 
    print("No solution found.")
