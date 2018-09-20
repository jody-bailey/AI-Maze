from _collections import deque

from subclass.Node import Node

file = open("resources/mymaze.txt", 'r').readlines()
queue = deque([])
rowSize = 10
colSize = 10
mazeArray = ['O'] * colSize
completedNodes = []
completePath = []

for i in range(rowSize):
    mazeArray[i] = ['O'] * colSize

index = 0
for i in range(rowSize):
    for j in range(colSize):
        mazeArray[i][j] = file[index].strip()
        index += 1


def findEntry():
    for i in range(colSize):
        for j in range(rowSize):
            if mazeArray[i][0] == 'E':
                return str(i) + '0'


def isGoal(node):
    if node.data == 'X':
        return True
    else:
        return False


def checkForChildren(node):
    children = []
    location = node.location
    row = int(location[0])
    col = int(location[1])

    if (mazeArray[row + 1][col] == 'P' or mazeArray[row + 1][col] == 'X') and row != 0:
        children.append(str(row + 1) + str(col))

    if (mazeArray[row][col - 1] == 'P' or mazeArray[row][col - 1] == 'X') and col != 0:
        children.append(str(row) + str(col - 1))

    if (mazeArray[row - 1][col] == 'P' or mazeArray[row - 1][col] == 'X') and row != 9:
        children.append(str(row - 1) + str(col))

    if (mazeArray[row][col + 1] == 'P' or mazeArray[row][col + 1] == 'X') and col != 9:
        children.append(str(row) + str(col + 1))

    return children


def getData(id):
    row = id[0]
    col = id[1]
    return mazeArray[int(row)][int(col)]


def checkVisited(node):
    if node.location in completedNodes:
        return True
    else:
        return False


def underline(list, path):
    for i in range(colSize):
        for j in range(rowSize):
            loc = str(i) + str(j)
            if loc in path:
                letter = list[i][j]
                list[i][j] = '\033[4m{}\033[0m'.format(letter)


def run():
    nodeid = findEntry()
    completedNodes.append(nodeid)
    completePath.append(nodeid)
    node = Node(nodeid, getData(nodeid), completedNodes)
    queue.append(node)

    if not isGoal(queue.popleft()):
        children = checkForChildren(node)
        for child in children:
            if child not in completedNodes:
                completedNodes.append(child)
                newNode = Node(child, getData(child), completePath, node)
                queue.append(newNode)

    try:
        newNode
    except NameError:
        currentNode = node
    else:
        currentNode = queue.popleft()
        completePath.append(currentNode.location)

    while not isGoal(currentNode):

        children = checkForChildren(currentNode)
        index = 0
        for child in children:
            if child not in completedNodes:
                completedNodes.append(child)
                newNode = Node(child, getData(child), completePath, currentNode)
                queue.append(newNode)
            else:
                try:
                    if len(children) == 1:
                        currentNode = currentNode.parent
                except ValueError:
                    '''do nothing'''
            index += 1

        try:
            currentNode = queue.popleft()
            completePath.append(currentNode.location)
        except IndexError:
            print('There is not a valid path.')
            return

        # for node in currentNode.path:
        #     print(node.location)

    finalPath = []

    for myNode in currentNode.path:
        finalPath.append(myNode.location)

    underline(mazeArray, finalPath)

    for row in mazeArray:
        print(' '.join([str(elem) for elem in row]))

    print()
    print(finalPath)
