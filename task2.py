

line = input("Write line: ")

l = len(line)

for i, c in enumerate(line):
    if i == 2 or i == l - 1:
        continue
    print(c)

if line.find("c") >= 0:
    print("Line has 'c'")

print("Length:", l)
