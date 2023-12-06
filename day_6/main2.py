TEST = "day_6/test.txt"
DATA = "day_6/data.txt"

import re


def read_file(file):
    with open(file=file, mode="r") as file:
        return file.readlines()

content = read_file(DATA)

times = int("".join(re.findall("\d+", content[0])))
distance = int("".join(re.findall("\d+", content[1])))

# charging * time-charging > distance 
# if yes + 1 to solution 


total = 1

race_win_option = 0
for secs in range(times):
    dist = secs * (times - secs)
    if dist > distance:
        race_win_option += 1
    
total *= race_win_option

print(total)