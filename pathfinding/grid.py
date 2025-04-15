# pathfinding/grid.py

class Spot:
    def __init__(self, x, y):
        self.i = x
        self.j = y
        self.f = 0
        self.g = 0
        self.h = 0
        self.neighbors = []
        self.previous = None
        self.obs = False
        self.closed = False
        self.value = 1

    def add_neighbors(self, grid, cols, rows):
        i, j = self.i, self.j
        if i < cols - 1 and not grid[i + 1][j].obs:
            self.neighbors.append(grid[i + 1][j])
        if i > 0 and not grid[i - 1][j].obs:
            self.neighbors.append(grid[i - 1][j])
        if j < rows - 1 and not grid[i][j + 1].obs:
            self.neighbors.append(grid[i][j + 1])
        if j > 0 and not grid[i][j - 1].obs:
            self.neighbors.append(grid[i][j - 1])

class Grid:
    def __init__(self, cols, rows):
        self.cols = cols
        self.rows = rows
        self.grid = [[Spot(i, j) for j in range(rows)] for i in range(cols)]

    def add_all_neighbors(self):
        for i in range(self.cols):
            for j in range(self.rows):
                self.grid[i][j].add_neighbors(self.grid, self.cols, self.rows)
