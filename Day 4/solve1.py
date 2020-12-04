records = []
with open("./Day 4/input.txt", 'r') as fd:
    record = ''
    for line in fd:
        data = line.rstrip('\n')
        if data == '':
            record = record[:-1] # strip trailing space
            records.append(record)
            record = ''
        else:
            record += data
            record += ' '
    #this is gross solution, but it fixes the off by 1
    records.append(record) #append last record

count = 0
wrong_count = 0
req_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'] # cid optional
for record in records:
    for field in req_fields:
        if field not in record:
            wrong_count += 1
            print(record)
            print("Not Valid! Missing: ", field)
            print()
            break
    else: # all required fields present
        print(record)
        print()
        count += 1

print("Ans: ", count)
print("Wrong: ", wrong_count)