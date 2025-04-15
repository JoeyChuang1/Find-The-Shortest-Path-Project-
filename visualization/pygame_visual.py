# visualization/pygame_visual.py

import pygame
from pathfinding.grid import Grid
from pathfinding.a_star import a_star
from pathfinding.heuristics import euclidean

class PygameVisualizer:
    def __init__(self, grid_size, start, end, show_steps):
        pygame.init()
        self.cols, self.rows = grid_size
        self.width = 800
        self.height = 800
        self.w = self.width / self.cols
        self.h = self.height / self.rows
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.grid = Grid(self.cols, self.rows)
        self.grid.add_all_neighbors()
        self.start = self.grid.grid[start[0]][start[1]]
        self.end = self.grid.grid[end[0]][end[1]]
        self.show_steps = show_steps

    def draw_grid(self):
        for i in range(self.cols):
            for j in range(self.rows):
                color = (255, 255, 255)
                pygame.draw.rect(self.screen, color, (i * self.w, j * self.h, self.w, self.h), 1)
        pygame.display.update()

    def run(self):
        self.draw_grid()
        path = a_star(self.start, self.end, self.grid.grid, euclidean
::contentReference[oaicite:10]{index=10}
 
