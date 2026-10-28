class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # visit islands, and use BFS to visit the whole island and mark those points visited
        count = 0
        visited = {}
        m = len(grid)
        n = len(grid[0])
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and ((i, j) not in visited):
                    # a new island, do BFS
                    count += 1
                    q = [(i, j)]
                    traj = {}
                    while q:
                        new_q = []
                        for point in q:
                            px = point[0]
                            py = point[1]
                            traj[(px, py)] = 0
                            visited[(px, py)] = 0
                            for step in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                                new_px = step[0] + px
                                new_py = step[1] + py
                                if (0 <= new_px < m) and (0 <= new_py < n) and ((new_px, new_py) not in traj) and (grid[new_px][new_py] == "1"):
                                    traj[(new_px, new_py)] = 0
                                    visited[(new_px, new_py)] = 0
                                    new_q.append((new_px, new_py))
                        q = new_q
                        
        return count



        

