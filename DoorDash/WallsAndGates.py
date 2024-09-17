class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        self.empty = 2147483647
        self.wall = -1
        self.gate = 0

        # BFS
        # Breadth first search from all gates to empty rooms
        # Guarantees shortest path since it's BFS
        # Get each gate and start searching its nearby neighbor
        # Populate value with the steps if current steps (BFS) has a smaller value than what is in the room
        queue = []
        for row in range(len(rooms)):
            for col in range(len(rooms[0])):
                if rooms[row][col] == self.gate:
                    queue.append((row,col,0))

        while queue:
            row,col,steps = queue.pop(0)
            # print(row,col,steps)
            if row < 0 or row >= len(rooms) or col < 0 or col >= len(rooms[0]):
                continue

            # print('here')
            if steps <= rooms[row][col]:
                rooms[row][col] = steps
                queue.append((row+1,col,steps+1))
                queue.append((row-1,col,steps+1))
                queue.append((row,col+1,steps+1))
                queue.append((row,col-1,steps+1))
            # print(queue)




