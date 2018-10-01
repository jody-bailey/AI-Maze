# Jody Bailey
# 09/21/2018
# Intro to Algorithms
# This is the Depth Search class that contains on the methods needed
# to perform the depth first search.

from subpkg.Node import Node


class DepthSearch:

    # Constructor
    def __init__(self, maze=None):

        # Maze is an optional value
        # if no value is passed in then initialize to an empty list
        if maze is None:
            maze = []

        # Initialize the stack
        self.stack = []

        # Set row and column size to 10
        self.rowSize = 10
        self.colSize = 10

        # Lists to keep track of where the agent has traveled.
        self.completedNodes = []
        self.completePath = []

        self.mazeArray = maze

        # This if statement is used in case a maze was not passed into the constructor.
        # this will build the mazeArray from the maze.txt file that is in this project.
        if len(self.mazeArray) == 0:
            self.file = open("resources/maze.txt", 'r').readlines()
            self.mazeArray = ['O'] * self.colSize
            self.completedNodes = []
            self.completePath = []

            for i in range(self.rowSize):
                self.mazeArray[i] = ['O'] * self.colSize

            index = 0
            for i in range(self.rowSize):
                for j in range(self.colSize):
                    self.mazeArray[i][j] = self.file[index].strip()
                    index += 1

    # This method is used to travers the left side of the maze to find the
    # entrance and return a tuple of that location
    def findEntry(self):
        for i in range(self.colSize):
            for j in range(self.rowSize):
                if self.mazeArray[i][0] == 'E':
                    return str(i) + '0'

    # This method is used to determine if we have reached the goal. It looks
    # at the node passed in and checks if the data contains the value 'X'.
    # if not then we have not reached the goal.
    def isGoal(self, node):
        if node.data == 'X':
            return True
        else:
            return False

    # This method is used to check all four perpendicular locations around the current
    # node for children containing the data value of 'P' or 'X'. It then returns a list
    # of all the children that the node has.
    def checkForChildren(self, node):
        children = []
        location = node.location
        row = int(location[0])
        col = int(location[1])

        if (self.mazeArray[row + 1][col] == 'P' or self.mazeArray[row + 1][col] == 'X') and row != 0:
            children.append(str(row + 1) + str(col))

        if (self.mazeArray[row][col - 1] == 'P' or self.mazeArray[row][col - 1] == 'X') and col != 0:
            children.append(str(row) + str(col - 1))

        if (self.mazeArray[row - 1][col] == 'P' or self.mazeArray[row - 1][col] == 'X') and row != 9:
            children.append(str(row - 1) + str(col))

        if (self.mazeArray[row][col + 1] == 'P' or self.mazeArray[row][col + 1] == 'X') and col != 9:
            children.append(str(row) + str(col + 1))

        return children

    # This method takes in a location in string form and returns the
    # data for that location
    def getData(self, location):
        row = location[0]
        col = location[1]
        return self.mazeArray[int(row)][int(col)]

    # This method is used to check if a node has been visited by passing in
    # that node and checking to see if it's location has been placed in the
    # completed nodes list. returns a boolean
    def checkVisited(self, node):
        if node.location in self.completedNodes:
            return True
        else:
            return False

    # This method is used to mark the path of the agent that it traveled
    # as it traversed the maze. It uses a nested for loop to go through
    # the 2D list and replace the letter at that location with a '*'
    def markPath(self, list, path):
        for i in range(self.colSize):
            for j in range(self.rowSize):
                loc = str(i) + str(j)
                if loc in path:
                    list[i][j] = '*'

    # This method is used to run the program by calling the methods above to bring
    # the program together with the algorithm and make it all work as one.
    # If there is any confusion with what is going on with anything in this method,
    # please refer to the individual methods above that are being used.
    def run(self):
        nodeid = self.findEntry()
        self.completedNodes.append(nodeid)
        self.completePath.append(nodeid)
        node = Node(nodeid, self.getData(nodeid), self.completedNodes)
        self.stack.append(node)

        if not self.isGoal(self.stack.pop()):
            children = self.checkForChildren(node)
            for child in children:
                if child not in self.completedNodes:
                    self.completedNodes.append(child)
                    newNode = Node(child, self.getData(child), self.completePath, node)
                    self.stack.append(newNode)

        try:
            newNode
        except NameError:
            currentNode = node
        else:
            currentNode = self.stack.pop()
            self.completePath.append(currentNode.location)

        while not self.isGoal(currentNode):

            children = self.checkForChildren(currentNode)
            index = 0
            for child in children:
                if child not in self.completedNodes:
                    self.completedNodes.append(child)
                    newNode = Node(child, self.getData(child), self.completePath, currentNode)
                    self.stack.append(newNode)
                else:
                    try:
                        if len(children) == 1:
                            currentNode = currentNode.parent
                    except ValueError:
                        '''do nothing'''
                index += 1

            try:
                currentNode = self.stack.pop()
                self.completePath.append(currentNode.location)
            except IndexError:
                print('There is not a valid path.')
                return

        finalPath = []

        for myNode in currentNode.path:
            finalPath.append(myNode.location)

        self.markPath(self.mazeArray, finalPath)

        for row in self.mazeArray:
            print(' '.join([str(elem) for elem in row]))

        print()
        print('Traveled Path: {}'.format(finalPath))
