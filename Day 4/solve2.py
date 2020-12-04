import re

# byr (Birth Year) - four digits; at least 1920 and at most 2002
def val_byr(value):
    #print("byr: ", value, end='')
    if len(value) < 4:
        #print(" invalid")
        return 0
    if 1920 <= int(value) <= 2002:
        #print(" valid")
        return 1
    else:
        #print(" invalid")
        return 0

# iyr (Issue Year) - four digits; at least 2010 and at most 2020
def val_iyr(value):
    #print("iyr: ", value, end='')
    if len(value) < 4:
        #print(" invalid")
        return 0
    if 2010 <= int(value) <= 2020:
        #print(" valid")
        return 1
    else:
        #print(" invalid")
        return 0

# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
def val_eyr(value):
    #print("eyr: ", value)
    if len(value) < 4:
        return 0
    if 2020 <= int(value) <= 2030:
        return 1
    else:
        return 0

#hgt (Height) - a number followed by either cm or in:
#If cm, the number must be at least 150 and at most 193.
#If in, the number must be at least 59 and at most 76
def val_hgt(value):
    #print("hgt: ", value, end='')
    system = value[-2:]
    amount = value[:-2]

    if system == 'cm':
        if 150 <= int(amount) <= 193:
            #print(" valid")
            return 1
        else:
            #print(" invalid")
            return 0
    elif system == 'in':
        if 59 <= int(amount) <= 76:
            #print(" valid")
            return 1
        else:
            #print(" invalid")
            return 0
    else:
        #print(" invalid")
        return 0

# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
def val_hcl(value):
    #print("hcl: ", value, end=' ')
    if len(value) < 7:
        #print("invalid")
        return 0

    # https://stackoverflow.com/a/1636354/1101802
    x = re.search("^#[a-z0-9]{6}$", value)
    if x:
        #print("valid")
        return 1
    else:
        #print("invalid")
        return 0

# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
def val_ecl(value):
    #print("ecl: ", value, end=' ')
    valid = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if value in valid:
        #print("valid")
        return 1
    else:
        #print("invalid")
        return 0

# pid (Passport ID) - a nine-digit number, including leading zeroes.
def val_pid(value):
    #print("pid: ", value, end=' ')
    x = re.search("^\d{9}$", value)
    if x:
        return 1
    else:
        return 0


#cid (Country ID) - ignored, missing or not.
def val_cid(value):
    return 1

def validate_fields(record):
    dispatch = {'byr' : val_byr, 
                'iyr' : val_iyr, 
                'eyr' : val_eyr, 
                'hgt' : val_hgt, 
                'hcl' : val_hcl, 
                'ecl' : val_ecl, 
                'pid' : val_pid,
                'cid' : val_cid}

    values = dict((x.strip(), y.strip()) for x,y in (kv_pairs.split(':') for kv_pairs in record.split(' ')))
    for k, v in values.items():
        res = dispatch[k](v)
        if res == 0:
            return 0

    return 1

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
    records.append(record.rstrip(' ')) #append last record

count = 0
complete = 1
total = len(records)
req_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'] # cid optional
for record in records:
    print("Checking [", complete, "/", total, "]", end=" ")
    for field in req_fields:
        if field not in record:
            print("invalid, skipping")
            break
    else: # all required fields present
        check = validate_fields(record)
        if check:
            print("valid")
            count += 1
        else:
            print("invalid")
    complete += 1

print("Ans: ", count)