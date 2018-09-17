from subclass.Node import Node

file = open("resources/mymaze.txt", 'r').readlines()
stack = []
rowSize = 10
colSize = 10
mazeArray = ['O'] * colSize
completePath = []

for i in range(rowSize):
    mazeArray[i] = ['O'] * colSize

index = 0
for i in range(rowSize):
    for j in range(colSize):
        mazeArray[i][j] = file[index].strip()
        index += 1


def createNode(location, path):
    node = {
        'location': location,
        'data': 'P',
        'path': path
    }
    return node


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
    if node.location in completePath:
        return True
    else:
        return False


def run():
    nodeid = findEntry()
    completePath.append(nodeid)
    node = Node(nodeid, getData(nodeid), completePath)
    stack.append(node)

    if not isGoal(stack.pop()):
        children = checkForChildren(node)
        for child in children:
            if child not in completePath:
                completePath.append(child)
                newNode = Node(child, getData(child), completePath, node)
                stack.append(newNode)

    try:
        newNode
    except NameError:
        currentNode = node
    else:
        currentNode = newNode

    while not isGoal(currentNode):

        children = checkForChildren(currentNode)
        index = 0
        for child in children:
            if child not in completePath:
                completePath.append(child)
                newNode = Node(child, getData(child), completePath, currentNode)
                stack.append(newNode)
            else:
                try:
                    currentNode = currentNode.siblings.index(index)
                except ValueError:
                    '''do nothing'''
            index += 1

        try:
            newNode
        except NameError:
            currentNode = stack.pop()
            if currentNode.location not in completePath:
                completePath.append(currentNode.location)
        else:
            if currentNode.location == newNode.location:
                currentNode = stack.pop()
                if currentNode.location not in completePath:
                    completePath.append(currentNode.location)
            else:
                currentNode = newNode
        print(currentNode.location)

    print()
    print(completePath)
    print('\033[4mhello\033[0m')
    for row in mazeArray:
        print(' '.join([str(elem) for elem in row]))

