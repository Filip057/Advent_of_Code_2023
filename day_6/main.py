TEST = "day_6/test.txt"
DATA = "day_6/data.txt"

import re


def read_file(file):
    with open(file=file, mode="r") as file:
        return file.readlines()

content = read_file(DATA)

times = list(map(lambda x: int(x), re.findall("\d+", content[0])))
distance = list(map(lambda x: int(x), re.findall("\d+", content[1])))

# charging * time-charging > distance 
# if yes + 1 to solution 

total = 1
for i, race_time in enumerate(times):
    race_win_option = 0
    for secs in range(race_time):
        dist = secs * (race_time - secs)
        if dist > distance[i]:
            race_win_option += 1
    
    total *= race_win_option

print(total)