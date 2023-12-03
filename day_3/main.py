FILE_NAME1 = "day_3/test_data.txt"
FILE_NAME2 = "day_3/file_1.txt"

def read_file(file):
    with open(file=file, mode="r") as file:
        return file.read()

symbol_positions = set()

content = read_file(FILE_NAME2)
field = content.split("\n")

for x, row in enumerate(field):
    for y, column in enumerate(row):
        if column.isdigit() or column == ".":
            continue
        symbol_positions.add((x,y))

number_beginnings = set()

for x,y in symbol_positions:
    for dx in range(x-1, x + 2):
        for dy in range(y - 1, y + 2):
            if dx < 0 or dx > len(field) or not field[dx][dy].isdigit():
                continue
            if dy < 0 or dy > len(field[dx]) or not field[dx][dy].isdigit():
                continue
            while dy > 0 and field[dx][dy - 1].isdigit():
                dy -= 1
            number_beginnings.add((dx,dy))

numbers = []

for x,y in number_beginnings:
    temp = ""
    while y < len(field[x]) and field[x][y].isdigit():
        temp += field[x][y]
        y += 1
    numbers.append(int(temp))

print(sum(numbers))
