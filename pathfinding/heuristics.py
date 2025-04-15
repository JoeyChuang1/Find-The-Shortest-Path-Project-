# pathfinding/heuristics.py

import math

def euclidean(a, b):
    return math.sqrt((a.i - b.i) ** 2 + (a.j - b.j) ** 2)

def manhattan(a, b):
    return abs(a.i - b.i) + abs(a.j - b.j)
