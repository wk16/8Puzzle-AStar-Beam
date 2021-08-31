from random import randrange


class EightPuzzle:
    def __init__(self):
        self.goalState = [['b', '1', '2'],
                          ['3', '4', '5'],
                          ['6', '7', '8']]
        self.state = self.goalState
        self.rowSize = 3
        self.currentCost = 0
        self.blank = (0, 0)

    def setGoalState(self, n):
        state = []
        rowSize = int((n + 1) ** .5)
        self.rowSize = rowSize
        for i in range(rowSize):
            row = []
            for j in range(rowSize):
                row.append(str(i * rowSize + j))
            state.append(row)
        state[0][0] = 'b'
        self.goalState = state

    def setState(self, s, rowSize=3):
        state = []
        for i in range(rowSize):
            row = []
            for j in range(rowSize):
                row.append(s[i * rowSize + j])
            state.append(row)
        self.blank = self.findBlank()
        self.state = state

    def printState(self):
        print(self.state)

    def findBlank(self):
        for i in range(self.rowSize):
            for j in range(self.rowSize):
                if self.state[i][j] == 'b':
                    return i, j

    def validMove(self, i, j, dir):
        if 0 <= i < self.rowSize and 0 <= j < self.rowSize:
            if dir == 'up':
                if i != 0:
                    return True
            elif dir == 'down':
                if i != self.rowSize - 1:
                    return True
            elif dir == 'right':
                if j != self.rowSize - 1:
                    return True
            elif dir == 'left':
                if j != 0:
                    return True
            return False
        return False

    def move(self, dir):
        i, j = self.findBlank()
        if not self.validMove(i, j, dir):
            print("invalid move")
        else:
            if dir == 'up':
                self.state[i][j], self.state[i + 1][j] = self.state[i + 1][j], self.state[i][j]
            elif dir == 'down':
                self.state[i][j], self.state[i - 1][j] = self.state[i - 1][j], self.state[i][j]
            elif dir == 'right':
                self.state[i][j], self.state[i][j + 1] = self.state[i][j + 1], self.state[i][j]
            elif dir == 'left':
                self.state[i][j], self.state[i][j - 1] = self.state[i][j - 1], self.state[i][j]
            else:
                return False
            return True

    def randomizeState(self, n):
        if not self.state:
            print("No set state")
        dirs = ['up', 'down', 'left', 'right']
        i, j = self.findBlank()
        while n != 0:
            randNum = randrange(4)
            dir = dirs[randNum]
            if self.move(dir):
                if dir == 'up':
                    i += 1
                elif dir == 'down':
                    i -= 1
                elif dir == 'right':
                    j += 1
                elif dir == 'left':
                    j -= 1
                n -= 1

    def solveAStar(self, heuristic):
        pass

    def solveBeam(self, k):
        pass

    def maxNodes(self, n):
        pass

    def readText(self):
        pass
