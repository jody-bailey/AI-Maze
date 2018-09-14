from _collections import deque

file = open("resources/maze.txt", 'r').readlines()
queue = deque([])
rowSize = 10
colSize = 10
mazeArray = ['O'] * colSize

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
                location = str(i) + '0'
                return createNode(location, location)


def isGoal(node):
    if node['data'] == 'X':
        return True
    else:
        return False


def checkForChildren(node):
    children = []
    location = node['location']
    row = int(location[0])
    col = int(location[1])

    if mazeArray[row + 1][col] == 'P' and row != 0:
        children.append(str(row + 1) + str(col))

    if mazeArray[row][col - 1] == 'P' and col != 0:
        children.append(str(row) + str(col - 1))

    if mazeArray[row - 1][col] == 'P' and row != 9:
        children.append(str(row - 1) + str(col))

    if mazeArray[row][col + 1] == 'P' and col != 9:
        children.append(str(row) + str(col + 1))

    return children


myNode = findEntry()
queue.append(myNode)

while not isGoal(queue.pop()):
    children = checkForChildren(myNode)
    for child in children:
        newNode = createNode((str(child)), '{}, {}'.format(myNode['path'], child))
    del myNode
    myNode = newNode
    queue.append(newNode)
print(myNode)

print()
print('\033[4mhello\033[0m')
for row in mazeArray:
    print(' '.join([str(elem) for elem in row]))
