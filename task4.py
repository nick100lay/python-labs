

vegetables = []
vegetables_count = []


for i in range(3):
    vegetables.append(input("Write vegetable: "))

for v in vegetables:
    print(v, v.lower(), v.upper(), v.capitalize())

for v in vegetables:
    vegetables_count.append(int(input("Write count of %s: " % v)))

for i, v in enumerate(vegetables):
    print("Count of %s: %i" % (v, vegetables_count[i]))
