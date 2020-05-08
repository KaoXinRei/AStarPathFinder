from heapq import heappop, heappush


def find_path(graph, start, finish):
    def heuristic(a, b):
        dx = abs(a[0] - b[0])
        dy = abs(a[1] - b[1])
        dmax = max(dx, dy)
        dmin = min(dx, dy)
        return dmin * 2 ** 0.5 - dmin + dmax

    def neighbors(a, point):
        n = {}
        x, y = point
        if x + 1 >= 0 and y + 1 >= 0:
            try:
                if a[x + 1][y + 1] and a[x][y+1] and a[x+1][y]:
                    n[(x + 1, y + 1)] = 2 ** 0.5
            except:
                pass
        if x + 1 >= 0 and y >= 0:
            try:
                if a[x + 1][y]:
                    n[(x + 1, y)] = 1
            except:
                pass
        if x >= 0 and y + 1 >= 0:
            try:
                if a[x][y + 1]:
                    n[(x, y + 1)] = 1
            except:
                pass
        if x - 1 >= 0 and y + 1 >= 0:
            try:
                if a[x - 1][y + 1] and a[x][y+1] and a[x-1][y]:
                    n[(x - 1, y + 1)] = 2 ** 0.5
            except:
                pass
        if x - 1 >= 0 and y >= 0:
            try:
                if a[x - 1][y]:
                    n[(x - 1, y)] = 1
            except:
                pass
        if x + 1 >= 0 and y - 1 >= 0:
            try:
                if a[x + 1][y - 1] and a[x][y-1] and a[x+1][y-1]:
                    n[(x + 1, y - 1)] = 2 ** 0.5
            except:
                pass
        if x >= 0 and y - 1 >= 0:
            try:
                if a[x][y - 1]:
                    n[(x, y - 1)] = 1
            except:
                pass
        if x - 1 >= 0 and y - 1 >= 0:
            try:
                if a[x - 1][y - 1] and a[x][y-1] and a[x-1][y]:
                    n[(x - 1, y - 1)] = 2 ** 0.5
            except:
                pass
        return n

    came_from = {start: []}
    queue = [(0, start)]
    coast = {start: 0}
    while len(queue) != 0:
        c = heappop(queue)[1]
        if c == finish:
            break
        n = neighbors(graph, c)
        for i in n:
            ncoast = coast[c] + n[i]
            if i not in coast or ncoast < coast[i]:
                coast[i] = ncoast
                heappush(queue, (ncoast + heuristic(start, i), i))
                came_from[i] = came_from[c] + [i]
    try:
        return came_from[finish]
    except:
        print('No such route found')

