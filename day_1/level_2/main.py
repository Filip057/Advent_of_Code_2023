import re


test_data = 'level_2/test_data.txt'

data = 'level_2/data.txt'

result = 0

digits ={
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7, 
    'eight': 8,
    'nine': 9,
}

with open(test_data, mode='r') as data:
    
    for line in data:
        print(line)