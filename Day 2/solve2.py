with open("./Day 2/input.txt", 'r') as fd:
    data = fd.read().splitlines()

#print(data[0].split(' '))
#print(data[0].split(' ')[0].split('-'))

"""
split
0 : min-max
1 : letter
2 : string to match

sub_split[0]
0: first
1: second
"""

count = 0
for line in data:
    check = 0
    split = line.split(' ')
    search = split[1][0]

    sub_split = split[0].split('-')
    first = int(sub_split[0]) - 1
    second = int(sub_split[1]) - 1

    if split[2][first] == search : check += 1
    if split[2][second] == search : check += 1

    if check == 1: count += 1

print("Ans: ", count)
