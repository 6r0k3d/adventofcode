with open("./Day 1/input.txt", 'r') as fd:
    data = fd.read().splitlines()

for val in data:
    temp = 2020 - int(val)
    if str(temp) in data:
        print("Ans: ", temp * int(val))
        exit(0)