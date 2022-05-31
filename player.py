
class Player:
    def __init__(self, intitalRow, initialColumn):
        self.rowPosition = intitalRow
        self.columnPosition = initialColumn

    # TODO
    
    def moveUp(self,x,y):
        self.columnPosition +=  [x,y]

    # TODO
    
    def moveDown(self, x,y):
        self.columnPosition += [x,y]

    # TODO
    
    def moveLeft(self, x,y):
        self.rowPosition += [x,y]

    # TODO
    
    def moveRight(self, x,y):
        self.rowPosition += [x,y]
