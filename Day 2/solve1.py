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
0: min
1: max
"""
count = 0
for line in data:
    split = line.split(' ')
    search = split[1][0]

    sub_split = split[0].split('-')
    min = int(sub_split[0])
    max = int(sub_split[1])

    match = [x for x in split[2] if x == search]
    if min <= len(match) <= max:
        count += 1

print("Ans: ", count)
