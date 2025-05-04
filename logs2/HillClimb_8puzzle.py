import copy

N = 3  # 3x3 Puzzle

# Goal State
goal = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]  # 0 represents the blank space
]

def calculate_misplaced_tiles(puzzle):
    misplaced = 0
    for i in range(N):
        for j in range(N):
            if puzzle[i][j] != 0 and puzzle[i][j] != goal[i][j]:
                misplaced += 1
    return misplaced

def find_blank(puzzle):
    for i in range(N):
        for j in range(N):
            if puzzle[i][j] == 0:
                return i, j

def print_puzzle(puzzle):
    for row in puzzle:
        print(" ".join(f"{num:2}" if num != 0 else "  " for num in row))
    print()

# Possible moves: (row change, column change)
moves = [
    (1, 0),   # Down
    (-1, 0),  # Up
    (0, 1),   # Right
    (0, -1)   # Left
]

def hill_climbing(puzzle):
    current = copy.deepcopy(puzzle)
    move_count = 0
    
    while True:
        blank_row, blank_col = find_blank(current)
        current_heuristic = calculate_misplaced_tiles(current)
        best_heuristic = current_heuristic
        best_move = None
        
        for move in moves:
            new_row, new_col = blank_row + move[0], blank_col + move[1]
            
            if 0 <= new_row < N and 0 <= new_col < N:
                new_puzzle = copy.deepcopy(current)
                new_puzzle[blank_row][blank_col], new_puzzle[new_row][new_col] = new_puzzle[new_row][new_col], new_puzzle[blank_row][blank_col]
                
                new_heuristic = calculate_misplaced_tiles(new_puzzle)
                if new_heuristic < best_heuristic:
                    best_heuristic = new_heuristic
                    best_move = (new_row, new_col)
        
        if best_move is None:
            print("Local Optima Reached! No better move found.")
            print(f"Total moves taken: {move_count}")
            break
        
        blank_row, blank_col = best_move
        current[find_blank(current)[0]][find_blank(current)[1]], current[blank_row][blank_col] = current[blank_row][blank_col], current[find_blank(current)[0]][find_blank(current)[1]]
        
        move_count += 1
        print(f"Move {move_count}:")
        print_puzzle(current)
        
        if best_heuristic == 0:
            print("Goal State Reached!")
            print(f"Total moves taken: {move_count}")
            break

if __name__ == "__main__":
    puzzle = [
        [1, 2, 3],
        [5, 6, 0],
        [4, 7, 8]
    ]
    print("Initial State:")
    print_puzzle(puzzle)
    print("Solving using Hill Climbing with Misplaced Tile Heuristic...")
    hill_climbing(puzzle)