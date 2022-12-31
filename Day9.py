# Advent of Code - Day 9 Solution (Part I)

visitedPositions = {(0, 0)}
H = [0, 0]
T = [0, 0]


def t_to_h():
    T[0] = H[0]
    T[1] = H[1]
    visitedPositions.add(tuple(T))


f = open("data9.txt")
movesLeft = 0
for line in f:
    movesLeft = int(line[2:])
    if line[0] == 'U':
        while movesLeft > 0:
            movesLeft -= 1
            if T[1] == H[1] - 1:
                t_to_h()
            H[1] += 1
    elif line[0] == 'L':
        while movesLeft > 0:
            movesLeft -= 1
            if T[0] == H[0] + 1:
                t_to_h()
            H[0] -= 1
    elif line[0] == 'D':
        while movesLeft > 0:
            movesLeft -= 1
            if T[1] == H[1] + 1:
                t_to_h()
            H[1] -= 1
    elif line[0] == 'R':
        while movesLeft > 0:
            movesLeft -= 1
            if T[0] == H[0] - 1:
                t_to_h()
            H[0] += 1

print("Part I Answer:")
print(len(visitedPositions))
