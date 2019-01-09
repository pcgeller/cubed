cubeSequence = [0,1,0,0,1,1,1,1,1,1,1,1,1,1,0,1,1,0,0,1,1,1,0,0,1,0,1,1,1,1,1,1,0,1,0,1]
class block:
    def __init__(self, orientation):
        self.orientation = orientation
        self.currentPosition = ''
        self.previousPositions = ''
        self.currentOrientation = ''
        self.previousOrientations = ''
        self.validOrientations = ''
        self.validPositions = ''
        self.order = ''

    def __repr__(self):
        return '{}  {}'.format(self.__class__.__name__, self.order)

def initBlocks(cubeSequence):
    listOfBlocks = []
    i = 0
    for blockOrient in cubeSequence:
        newBlock = block(blockOrient)
        newBlock.order = i
        listOfBlocks.append(newBlock)
        i += 1
    return listOfBlocks

dimensionRange = range(0,3 + 1)
orientation []
allPossiblePoints = [(i,j,k) for i in dimensionRange for j in dimensionRange for k in dimensionRange]
i = 0
for startPoint in allPossiblePoints:
    listOfBlocks[i].orientation
    #set orientation for initial block
    #validity check
    #for block in cubeSequence
        #set orientation
        #validity check
        #if validity check == True
            #goto next block
        #else
        #   record invalid orientation and restart this loop
