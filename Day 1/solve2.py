with open("./Day 1/input.txt", 'r') as fd:
    data = fd.read().splitlines()

for val1 in data:
    temp1 = 2020 - int(val1)

    for val2 in data:
        temp2 = temp1 - int(val2)


        if str(temp2) in data:
            print(temp2, int(val1), int(val2))
            print("Ans: ", temp2 * int(val1) * int(val2))
            exit(0)