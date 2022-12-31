from collections import deque

f = open("data6.txt")
code = f.readline()
finished = False
chars = deque()
charIndex = 0
newChar = ''
passwordLen = 14
# Change passwordLen to 4 to get the answer to part 1 (1578)
while not finished:
    newChar = code[charIndex]
    i = 0
    while i < len(chars):
        if newChar == chars[i]:
            for j in range(0, i + 1):
                chars.popleft()
            i = len(chars)
        i += 1
    chars.append(newChar)
    if len(chars) == passwordLen:
        finished = True
    charIndex += 1

print("Part II Answer:")
print(charIndex)
f.close()
