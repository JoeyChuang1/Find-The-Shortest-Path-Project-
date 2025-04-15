# pathfinding/a_star.py

def a_star(start, end, grid, heuristic):
    open_set = [start]
    closed_set = []
    path = []
    while open_set:
        current = min(open_set, key=lambda spot: spot.f)
        if current == end:
            temp = current
            while temp.previous:
                path.append(temp)
                temp = temp.previous
            return path[::-1]
        open_set.remove(current)
        closed_set.append(current)
        for neighbor in current.neighbors:
            if neighbor in closed_set or neighbor.obs:
                continue
            temp_g = current.g + neighbor.value
            if neighbor not in open_set:
                open_set.append(neighbor)
            elif temp_g >= neighbor.g:
                continue
            neighbor.g = temp_g
            neighbor.h = heuristic(neighbor, end)
            neighbor.f = neighbor.g + neighbor.h
            neighbor.previous = current
    return None
