# Advent of Code - Day 11 Solution

# Arrays to keep track of monkeys' corresponding items and potential actions
# Note that the monkey's number corresponds to its index in the arrays
# For the operations array, the first number in each monkey's array corresponds to the type of operation (0 = +, 1 = *,
#   2 = ^2) and the second number corresponds to the number to add/multiply by (if applicable)
# The tests array contains the number that the worry level must be divisible by in order for the test to return true
# The next two arrays contain the monkey to throw the item to depending on if the test returns true or false
# monkeyTotals contains the number of items inspected by each monkey
items = []
operations = []
tests = []
trueReceivers = []
falseReceivers = []
monkeyTotals = []

# Parsing the given file
f = open("data11.txt")
lineNum = 0
currMonkey = -1
words = []
for line in f:
    if lineNum % 7 == 0:
        currMonkey += 1
        items.append([])
        monkeyTotals.append(0)
    elif lineNum % 7 == 1:
        words = line.split()
        i = 2
        while i < len(words) - 1:
            items[currMonkey].append(int(words[i][:-1]))
            i += 1
        items[currMonkey].append(int(words[i]))
    elif lineNum % 7 == 2:
        words = line.split()
        if words[4] == "+":
            operations.append([0, int(words[5])])
        elif words[4] == "*":
            if words[5] == "old":
                operations.append([2])
            else:
                operations.append([1, int(words[5])])
    elif lineNum % 7 == 3:
        tests.append(int(line.split()[3]))
    elif lineNum % 7 == 4:
        trueReceivers.append(int(line.split()[5]))
    elif lineNum % 7 == 5:
        falseReceivers.append(int(line.split()[5]))

    lineNum += 1

f.close()

# Running Rounds (note: change numRounds to 20 to get the answer to part I)
# For Part II, worry levels are taken mod worryManager to keep them manageable
worryManager = 1
for i in range(0, len(tests)):
    worryManager *= tests[i]

currItem = 0
numRounds = 10000
for i in range(0, 10000):
    for monkey in range(0, len(items)):
        while len(items[monkey]) > 0:
            if operations[monkey][0] == 0:
                currItem = items[monkey].pop() + operations[monkey][1]
            elif operations[monkey][0] == 1:
                currItem = items[monkey].pop() * operations[monkey][1]
            elif operations[monkey][0] == 2:
                currItem = items[monkey].pop() ** 2
            # Uncomment this line (and comment out the line below) to get the answer to part I
            # currItem //= 3
            currItem %= worryManager
            if currItem % tests[monkey] == 0:
                items[trueReceivers[monkey]].append(currItem)
            else:
                items[falseReceivers[monkey]].append(currItem)
            monkeyTotals[monkey] += 1

# Getting the answer
highestTotal = monkeyTotals[0]
secondHighestTotal = 0
for i in range(1, len(monkeyTotals)):
    if monkeyTotals[i] > highestTotal:
        secondHighestTotal = highestTotal
        highestTotal = monkeyTotals[i]
    elif monkeyTotals[i] > secondHighestTotal:
        secondHighestTotal = monkeyTotals[i]

print("Answer:")
print(highestTotal * secondHighestTotal)
