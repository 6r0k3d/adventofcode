from functools import reduce

with open("./Day 3/input.txt", 'r') as fd:
    data = fd.read().splitlines()

# data = rows 
# data[0] = specified row (y)
# data[0][0] = specified column (x)
MAX_X = len(data[0])
MAX_Y = len(data)

RIGHT_SLOPES = [1,3,5,7,1]
DOWN_SLOPES = [1,1,1,1,2]

counts = []
for index in range(len(RIGHT_SLOPES)):
    count = 0
    # 0,0 == top left
    x_pos = 0
    y_pos = 0
    
    RIGHT = RIGHT_SLOPES[index]
    DOWN = DOWN_SLOPES[index]
    while y_pos < MAX_Y:
        print(x_pos, y_pos)
        if data[y_pos][x_pos] == '#':
            count += 1
        y_pos += DOWN
        x_pos = (x_pos + RIGHT) % MAX_X

    counts.append(count)

print(counts)
result = reduce((lambda x,y : x * y), counts)
print("Ans: ", result)