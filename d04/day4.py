import re
# part 1
with open('day4.txt','r') as f:
    passports = f.read()
    passports = passports.rstrip().split('\n\n')
    count = 0
    for x in passports:
        x = x.replace('\n', ' ')
        byr = re.search(r'byr:', x)
        iyr = re.search(r'iyr:', x)
        eyr = re.search(r'eyr:', x)
        hgt = re.search(r'hgt:', x)
        hcl = re.search(r'hcl:', x)
        ecl = re.search(r'ecl:', x)
        pid = re.search(r'pid:', x)
        count += not not(byr and iyr and eyr and hgt and hcl and ecl and pid)
print(count)
f.close()

# part 2
count = 0
for x in passports:
    x = x.replace('\n', ' ')
    byr = re.search(r'byr:(19[2-9][0-9]|200[0-2])', x)
    iyr = re.search(r'iyr:(201[0-9]|2020)', x)
    eyr = re.search(r'eyr:(202[0-9]|2030)', x)
    hgt = re.search(r'hgt:(1[5-8][0-9]cm|19[0-3]cm|59in|6[0-9]in|7[0-6]in)', x)
    hcl = re.search(r'hcl:#[0-9a-f]{6}( |$)', x)
    ecl = re.search(r'ecl:(amb|blu|brn|gry|grn|hzl|oth)', x)
    pid = re.search(r'pid:[0-9]{9}( |$)', x)
    count += not not(byr and iyr and eyr and hgt and hcl and ecl and pid)

print(count)

