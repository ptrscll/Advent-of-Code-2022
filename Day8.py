# Advent of Code - Day 8 Solution (Parts I and II)

f = open("data8.txt")

# Initializing a 2D array to represent the visibilities of the trees
# First index is row, second index is column
visibilityMap = [[False] * 99 for i in range(0, 99)]

lines = []
lineNum = 0

# Declaring variables that will be used in the loop to save memory
i = 0
visibleHeight = 0

# Reading the file and checking the visibilities for each row
for line in f:
    lines.append(line)

    # Checking which trees can be seen from the left
    i = 0
    visibleHeight = -1
    while visibleHeight != 9 and i < 99:
        if int(line[i]) > visibleHeight:
            visibilityMap[lineNum][i] = True
            visibleHeight = int(line[i])
        i += 1
    # Checking which trees can be seen from the right
    i = 98
    visibleHeight = -1
    while visibleHeight != 9 and i >= 0:
        if int(line[i]) > visibleHeight:
            visibilityMap[lineNum][i] = True
            visibleHeight = int(line[i])
        i -= 1
    lineNum += 1

f.close()

# Checking the columns
for columnNum in range(0, 99):

    # Checking columns from the top
    i = 0
    visibleHeight = -1
    while visibleHeight != 9 and i < 99:
        if int(lines[i][columnNum]) > visibleHeight:
            visibilityMap[i][columnNum] = True
            visibleHeight = int(lines[i][columnNum])
        i += 1
    # Checking columns from the bottom
    i = 98
    visibleHeight = -1
    while visibleHeight != 9 and i >= 0:
        if int(lines[i][columnNum]) > visibleHeight:
            visibilityMap[i][columnNum] = True
            visibleHeight = int(lines[i][columnNum])
        i -= 1

# Summing the number of visible trees
total = 0

for row in visibilityMap:
    for column in row:
        # Adding to the total of visible trees (if needed)
        if column:
            total += 1

# Calculating Scenic Scores
maxScore = 0

# Declaring variables used in the loops to save memory
upVisibility = 0
downVisibility = 0
rightVisibility = 0
leftVisibility = 0
currIndex = 0
treeHeight = 0
for treeRow in range(0, 99):
    for treeColumn in range(0, 99):
        upVisibility = 0
        downVisibility = 0
        rightVisibility = 0
        leftVisibility = 0
        treeHeight = lines[treeRow][treeColumn]

        # Finding upVisibility
        currIndex = treeRow - 1
        while currIndex >= 0:
            upVisibility += 1
            if treeHeight <= lines[currIndex][treeColumn]:
                currIndex = 0
            currIndex -= 1

        # Finding leftVisibility
        currIndex = treeColumn - 1
        while currIndex >= 0:
            leftVisibility += 1
            if treeHeight <= lines[treeRow][currIndex]:
                currIndex = 0
            currIndex -= 1

        # Finding downVisibility
        currIndex = treeRow + 1
        while currIndex < 99:
            downVisibility += 1
            if treeHeight <= lines[currIndex][treeColumn]:
                currIndex = 99
            currIndex += 1

        # Finding rightVisibility
        currIndex = treeColumn + 1
        while currIndex < 99:
            rightVisibility += 1
            if treeHeight <= lines[treeRow][currIndex]:
                currIndex = 99
            currIndex += 1
        if upVisibility * leftVisibility * downVisibility * rightVisibility > maxScore:
            maxScore = upVisibility * leftVisibility * downVisibility * rightVisibility


print("Part I Answer:")
print(total)
print("Part II Answer: ")
print(maxScore)
