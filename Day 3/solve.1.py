with open("./Day 3/input.txt", 'r') as fd:
    data = fd.read().splitlines()

# data = rows 
# data[0] = specified row (y)
# data[0][0] = specified column (x)
MAX_X = len(data[0])
MAX_Y = len(data)

# 0,0 == top left
x_pos = 0
y_pos = 0

RIGHT = 3
DOWN = 1

count = 0
while y_pos < MAX_Y:
    print(x_pos, y_pos)
    if data[y_pos][x_pos] == '#':
        count += 1
    y_pos += DOWN
    x_pos = (x_pos + RIGHT) % MAX_X

print("Ans: ", count)