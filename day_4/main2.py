from collections import defaultdict

TEST = "day_4/test.txt"
FILE_NAME2 = "day_4/data.txt"

import re

def read_file(file):
    with open(file=file, mode="r") as file:
        return file.readlines()

content = read_file(FILE_NAME2)


start = 1 
card_dict = {k: start for k in range(len(content))}

counter = defaultdict(int)

for i, card in enumerate(content):
    all_numbers = card.split(':')[1].strip()
    winning_nums =re.findall("\d+" , all_numbers.split(" |")[0])
    game_nums = re.findall("\d+" , all_numbers.split(" |")[1])

    index_of_copies = len(list(set(winning_nums) & set(game_nums)))
    
    if index_of_copies > 0:
        indexes = [ii for ii in range(i+1, i+index_of_copies+1)]
        # kolikrat musim pridat 
        num_of_cards = card_dict[i]
        # prochazim kam musim pridat 
        for id in indexes:
            card_dict[id] += num_of_cards

total_sum = sum(card_dict.values())
print(total_sum)
# print(card_dict)


