# Advent of Code - Day 9 Solution (Part II)

visitedPositions = {(0, 0)}
rope = [[0, 0] for i in range(0, 10)]


# This function moves one segment of the rope (back) so that it catches up to the next segment (front)
# Without a way to easily draw this out, this code may be a bit difficult to follow
# Note that part 2 also uses a Cartesian coordinate system for rope locations
def move(front, back):
    if back[0] == front[0]:
        if back[1] == front[1] + 2:
            back[1] -= 1
        elif back[1] == front[1] - 2:
            back[1] += 1
    elif back[0] == front[0] + 1:
        if back[1] == front[1] + 2:
            back[1] -= 1
            back[0] -= 1
        elif back[1] == front[1] - 2:
            back[1] += 1
            back[0] -= 1
    elif back[0] == front[0] + 2:
        back[0] -= 1
        if back[1] > front[1]:
            back[1] -= 1
        elif back[1] < front[1]:
            back[1] += 1
    elif back[0] == front[0] - 1:
        if back[1] == front[1] + 2:
            back[1] -= 1
            back[0] += 1
        elif back[1] == front[1] - 2:
            back[1] += 1
            back[0] += 1
    elif back[0] == front[0] - 2:
        back[0] += 1
        if back[1] > front[1]:
            back[1] -= 1
        elif back[1] < front[1]:
            back[1] += 1


f = open("data9.txt")
movesLeft = 0
for line in f:
    movesLeft = int(line[2:])
    while movesLeft > 0:
        if line[0] == 'U':
            rope[0][1] += 1
        elif line[0] == 'L':
            rope[0][0] -= 1
        elif line[0] == 'D':
            rope[0][1] -= 1
        elif line[0] == 'R':
            rope[0][0] += 1
        for i in range(0, 9):
            move(rope[i], rope[i + 1])
        visitedPositions.add(tuple(rope[9]))
        movesLeft -= 1

f.close()
print("Part II Answer:")
print(len(visitedPositions))
