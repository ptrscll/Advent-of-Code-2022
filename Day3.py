# PART I
f = open("data.txt")
total = 0
for line in f:
    charSet = {line[0]}
    bucketSize = int(len(line)/2)
    for i in range(1, bucketSize):
        charSet.update(line[i])
    i = bucketSize
    while i < len(line):
        if line[i] in charSet:
            if ord(line[i]) > 90:
                total += ord(line[i]) - 96
            else:
                total += ord(line[i]) - 38
            i = len(line)
        i += 1
print("Part I answer:")
print(total)
f.close()

# PART II
f = open("data.txt")
total = 0
lineNum = 1

# Set of chars in first line
charSet1 = {}

# Set of chars in both first and second lines
charSet2 = {}
for line in f:
    if lineNum % 3 == 1:
        charSet1 = {line[0]}
        for i in range(1, len(line)):
            charSet1.update(line[i])
    elif lineNum % 3 == 2:
        charSet2 = {0}
        # 0 is a dummy value because .update requires CHarSet to not be empty
        for i in range(0, len(line)):
            if line[i] in charSet1:
                charSet2.update(line[i])
    elif lineNum % 3 == 0:
        i = 0
        while i < len(line):
            if line[i] in charSet2:
                if ord(line[i]) > 90:
                    total += ord(line[i]) - 96
                else:
                    total += ord(line[i]) - 38
                i = len(line)
            i += 1
    lineNum += 1
print("Part II answer:")
print(total)
f.close()
