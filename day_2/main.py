import re

test_file = 'day_2/test_data.txt'

data = 'day_2/data.txt'

total = 0

limits = {
    'red': 12,
    'green': 13,
    'blue': 14
}

with open(file=data, mode='r') as file:

    for line in file:
        game_id= int(re.findall(r'Game (\d+):', line)[0])
        bag_of_cubes = line.split(':')[1].split(";")
        can_add = True
        for hand in bag_of_cubes:
            cubes = hand.split(",")
            for c in cubes:
                num = int("".join(re.findall("\d",c)))
                color = c[3:].strip()
                if num > limits[color]:
                    can_add = False
                    break
        if can_add:
            total += game_id

            

print(total)




