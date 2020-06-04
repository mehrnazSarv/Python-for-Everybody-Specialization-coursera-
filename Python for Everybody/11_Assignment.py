import re
name = input("Enter file:")
handle = open(name)
result = 0
nums = list()
for line in handle:
    strnums = re.findall('[0-9]+', line)
    if len(strnums) > 0:
        for num in strnums:
            result = result + int(num)
print (result)
