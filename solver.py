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
    

def initBlocks(cubeSequence):
    for block in cubeSequence:
        #set orientation
    return listOfBlocks

initPosition = [0,0,0]
maxPosition = [3,3,3]

dimensionRange = range(0,3 + 1)

allPossiblePoints = [(i,j,k) for i in dimensionRange for j in dimensionRange for k in dimensionRange]

for startPoint in allPossiblePoints:
    #set orientation for initial block
    #validity check
    #for block in cubeSequence
        #set orientation
        #validity check
        #if validity check == True
            #goto next block
        #else
        #   record invalid orientation and restart this loop
