import time
import copy
import os

class GameOfLife:
    def __init__(self, rows, cols, initial_state=None):
        self.rows = rows
        self.cols = cols
        if initial_state:
            self.grid = copy.deepcopy(initial_state)
        else:
            self.grid = [[0 for _ in range(cols)] for _ in range(rows)]

    def display(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        for row in self.grid:
            print(' '.join(['█' if cell else ' ' for cell in row]))
        print()

    def count_live_neighbors(self, row, col):
        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),          (0, 1),
                      (1, -1),  (1, 0), (1, 1)]
        count = 0
        for dr, dc in directions:
            r, c = row + dr, col + dc
            if 0 <= r < self.rows and 0 <= c < self.cols:
                count += self.grid[r][c]
        return count

    def next_generation(self):
        new_grid = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        for r in range(self.rows):
            for c in range(self.cols):
                live_neighbors = self.count_live_neighbors(r, c)
                if self.grid[r][c] == 1:
                    if live_neighbors < 2 or live_neighbors > 3:
                        new_grid[r][c] = 0
                    else:
                        new_grid[r][c] = 1
                else:
                    if live_neighbors == 3:
                        new_grid[r][c] = 1
        self.grid = new_grid

    def is_stable(self, prev_grid):
        return self.grid == prev_grid

    def run(self, generations=100, delay=0.5):
        prev_grid = None
        for gen in range(generations):
            self.display()
            if prev_grid is not None and self.is_stable(prev_grid):
                print("Game ended: Stable state reached.")
                break
            prev_grid = copy.deepcopy(self.grid)
            self.next_generation()
            time.sleep(delay)

if __name__ == "__main__":
    # Example initial states
    # Blinker (period 2 oscillator)
    blinker = [
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,1,1,1,0],
        [0,0,0,0,0],
        [0,0,0,0,0]
    ]

    # Glider
    glider = [
        [0,0,0,0,0],
        [0,0,1,0,0],
        [0,0,0,1,0],
        [0,1,1,1,0],
        [0,0,0,0,0]
    ]

    # Block (still life)
    block = [
        [0,0,0,0],
        [0,1,1,0],
        [0,1,1,0],
        [0,0,0,0]
    ]

    print("Choose initial state: 1) Blinker 2) Glider 3) Block")
    choice = input("Enter 1, 2, or 3: ")
    if choice == '1':
        initial = blinker
    elif choice == '2':
        initial = glider
    else:
        initial = block

    rows = len(initial)
    cols = len(initial[0])
    game = GameOfLife(rows, cols, initial)
    game.run(generations=50, delay=0.3)