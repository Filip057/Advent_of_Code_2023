import re


test_data = 'day_1/test_data.txt'

data = 'day_1/data.txt'

result = 0
with open(data, mode='r') as data:
    
    for line in data:
        only_digits = re.findall("\d", line)
        first_d = only_digits[0]
        last_d = only_digits[-1]
        num = int(first_d+last_d)
        result += num

print(result)
    
            