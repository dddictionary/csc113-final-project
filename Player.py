class Player:
    def __init__(self, playerName):
        self.playerName = playerName
        # idk why i put playerName idrc

    def moveLeft(self):
        left = True
        for i in range(4):
            new_pos = 0
            for j in range(4):
                if self.board[i][j] != 0:
                    self.merge_tile(i,j,left)
                    self.board[i][new_pos] = self.board[i][j]
                    if j != new_pos:
                        self.board[i][j] = 0
            new_pos += 1
            left = False

    def moveRight(self):
        right = True
        for i in range(4):
            new_pos = 3
            for j in range(4):
                if self.board[i][j] != 0:
                    self.merge_tile(i,j,right)
                    self.board[i][new_pos] = self.board[i][j]
                    if j != new_pos:
                        self.board[i][j] = 0
            new_pos -= 1
            right = False

    def moveUp(self):
        up = True
        for j in range(4):
            new_pos = 0
            for i in range(4):
                if self.board[i][j] != 0:
                    self.merge_tile(i,j,up)
                    self.board[new_pos][j] = self.board[i][j]
                    if i != new_pos:
                        self.board[i][j] = 0
            new_pos += 1
            up = False
            
    def moveDown(self):
        down = True
        for j in range(4):
            new_pos = 3
            for i in range(4):
                if self.board[i][j] != 0:
                    self.merge_tile(i,j,down)
                    self.board[new_pos][j] = self.board[i][j]
                    if i != new_pos:
                        self.board[i][j] = 0
            new_pos -= 1
            down = False
