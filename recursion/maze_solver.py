from typing import List

def hasPath(maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
    """Solve a maze without hitting the wall

    Returns:
        bool: possible to get to the destination from the start
    """
    visited = set()
    nrow, ncol = len(maze), len(maze[0])
    
    # directions: up, down, left, right
    directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    
    def dfs(x,y) -> bool:
        if x==destination[0] and y == destination[1]:
            return True
        elif (x,y) in visited:
            return False
        
        visited.add((x, y))  # mark the cell as visited

        # try each direction
        for dx, dy in directions:
            nx, ny = x, y
            # keep moving in the direction (dx, dy) until you hit a wall
            while 0 <= nx+dx < nrow and 0 <= ny+dy < ncol and maze[nx+dx][ny+dy] == 0:
                nx += dx
                ny += dy
            if dfs(nx, ny):
                return True

        return False

    return dfs(start[0], start[1])


maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]]
start = [0,4]
destination = [4,4]
assert hasPath(maze, start, destination) == True