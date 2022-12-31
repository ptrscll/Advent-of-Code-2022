f = open("data4.txt")
total1 = 0
total2 = 0
for line in f:
    elfRanges = line.split(",")
    range1 = elfRanges[0].split("-")
    range2 = elfRanges[1].split("-")
    if not (int(range1[1]) < int(range2[0]) or int(range2[1]) < int(range1[0])):
        total2 += 1
        if int(range1[0]) <= int(range2[0]) and int(range1[1]) >= int(range2[1]):
            total1 += 1
        elif int(range1[0]) >= int(range2[0]) and int(range1[1]) <= int(range2[1]):
            total1 += 1
print("Part I Answer:")
print(total1)
print("")
print("Part II Answer:")
print(total2)
f.close()
