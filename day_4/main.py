FILE_NAME1 = "day_4/test.txt"
FILE_NAME2 = "day_4/data.txt"

import re

def read_file(file):
    with open(file=file, mode="r") as file:
        return file.readlines()

content = read_file(FILE_NAME2)

result = 0

for card in content:
    all_numbers = card.split(':')[1].strip()
    winning_nums =re.findall("\d+" , all_numbers.split(" |")[0])
    game_nums = re.findall("\d+" , all_numbers.split(" |")[1])

    common_nums = set(winning_nums) & set(game_nums)
    if len(common_nums) >= 1:
        x = len(common_nums) - 1
        points = 2**x
        result += points



print(result)



    

