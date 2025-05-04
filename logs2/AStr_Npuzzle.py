import heapq

class NPuzzleState:
    def __init__(self, board, parent=None, move=""):
        self.board = [row[:] for row in board]
        self.parent = parent
        self.move = move
        self.g = 0  # Cost from start
        if parent:
            self.g = parent.g + 1

    def __eq__(self, other):
        return self.board == other.board

    def __lt__(self, other):
        return (self.g + self.heuristic()) < (other.g + other.heuristic())

    def __hash__(self):
        return hash(tuple(tuple(row) for row in self.board))

    def find_blank(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j] == 0:
                    return i, j

    def heuristic(self):
        # Manhattan distance heuristic
        distance = 0
        n = len(self.board)
        for i in range(n):
            for j in range(n):
                if self.board[i][j] != 0:
                    x, y = divmod(self.board[i][j] - 1, n)
                    distance += abs(x - i) + abs(y - j)
        return distance

    def get_successors(self):
        successors = []
        i, j = self.find_blank()
        moves = [(0, 1, 'Right'), (0, -1, 'Left'), (1, 0, 'Down'), (-1, 0, 'Up')]

        for di, dj, move in moves:
            ni, nj = i + di, j + dj
            if 0 <= ni < len(self.board) and 0 <= nj < len(self.board[0]):
                new_board = [row[:] for row in self.board]
                new_board[i][j], new_board[ni][nj] = new_board[ni][nj], new_board[i][j]
                successors.append(NPuzzleState(new_board, self, move))
        return successors

def a_star_npuzzle(initial_board, goal_board):
    initial_state = NPuzzleState(initial_board)
    goal_state = NPuzzleState(goal_board)
    
    open_list = []
    closed_set = set()
    heapq.heappush(open_list, (initial_state.g + initial_state.heuristic(), initial_state))
    
    while open_list:
        _, current = heapq.heappop(open_list)
        
        if current.board == goal_state.board:
            path = []
            states = []
            while current.parent:
                path.append(current.move)
                states.append(current)
                current = current.parent
            states.append(current)
            states.reverse()
            path.reverse()
            return path, states
        
        closed_set.add(current)
        
        for successor in current.get_successors():
            if successor not in closed_set:
                heapq.heappush(open_list, (successor.g + successor.heuristic(), successor))
    
    return None, None

def print_board(board):
    for row in board:
        print(" ".join(str(cell) if cell != 0 else '_' for cell in row))
    print()

def main():
    print("Enter the initial board configuration (3x3, use 0 for blank):")
    initial = []
    for i in range(3):
        row = list(map(int, input(f"Row {i+1}: ").strip().split()))
        if len(row) != 3:
            print("Each row must contain 3 values.")
            return
        initial.append(row)

    goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    print("\nSolving the puzzle...\n")
    
    moves, states = a_star_npuzzle(initial, goal)
    
    if moves is None:
        print("No solution found.")
    else:
        print("Steps to reach goal:")
        for i, state in enumerate(states):
            print(f"Step {i}:", end=" ")
            if state.move:
                print(f"Move {state.move}")
            else:
                print("Start state")
            print_board(state.board)
        
        print("Puzzle solved!")
        print("Sequence of moves:", " -> ".join(moves))

if __name__ == "__main__":
    main()
