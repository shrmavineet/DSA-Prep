class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m = len(classroom)
        n = len(classroom[0])

        # Find S and all L positions
        start = None
        litter = []

        for i in range(m):
            for j in range(n):
                if classroom[i][j] == 'S':
                    start = (i, j)
                elif classroom[i][j] == 'L':
                    litter.append((i, j))

        k = len(litter)

        # Map litter position -> bit number
        litter_index = {
            pos: i for i, pos in enumerate(litter)
        }

        # All litter collected
        target = (1 << k) - 1

        # BFS state:
        # (row, col, remaining_energy, mask)
        queue = deque()
        queue.append((start[0], start[1], energy, 0))

        # visited states
        visited = set()
        visited.add((start[0], start[1], energy, 0))

        moves = 0

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        while queue:
            for _ in range(len(queue)):
                r, c, curr_energy, mask = queue.popleft()

                # All litter collected
                if mask == target:
                    return moves

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    # Outside grid
                    if nr < 0 or nr >= m or nc < 0 or nc >= n:
                        continue

                    # Obstacle
                    if classroom[nr][nc] == 'X':
                        continue

                    # Need energy to make a move
                    if curr_energy == 0:
                        continue

                    new_energy = curr_energy - 1
                    new_mask = mask

                    # Collect litter
                    if (nr, nc) in litter_index:
                        idx = litter_index[(nr, nc)]
                        new_mask |= (1 << idx)

                    # Reset energy
                    if classroom[nr][nc] == 'R':
                        new_energy = energy

                    state = (nr, nc, new_energy, new_mask)

                    if state not in visited:
                        visited.add(state)
                        queue.append(state)

            moves += 1

        return -1