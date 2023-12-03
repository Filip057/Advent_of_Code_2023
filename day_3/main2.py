FILE_NAME1 = "day_3/test_data.txt"
FILE_NAME2 = "day_3/file_1.txt"

def read_file(file):
    with open(file=file, mode="r") as file:
        return file.read()

star_positions = set()

content = read_file(FILE_NAME2)
field = content.split("\n")
result = 0

for x, row in enumerate(field):
    for y, column in enumerate(row):
        if column == "*":
            star_positions.add((x,y))
        



for x,y in star_positions:
    number_beginnings = set()
    for dx in range(x-1, x + 2):
        for dy in range(y - 1, y + 2):
            if dx < 0 or dx > len(field) or not field[dx][dy].isdigit():
                continue
            if dy < 0 or dy > len(field[dx]) or not field[dx][dy].isdigit():
                continue
            while dy > 0 and field[dx][dy - 1].isdigit():
                dy -= 1
            number_beginnings.add((dx,dy))
    if len(number_beginnings) == 2:
        numbers = []
        for xx,yy in number_beginnings:
            temp = ""
            while yy < len(field[xx]) and field[xx][yy].isdigit():
                temp += field[xx][yy]
                yy += 1
            numbers.append(int(temp))
        result += numbers[0] * numbers[1]

print(result)

# numbers = []

# for x,y in number_beginnings:
#     temp = ""
#     while y < len(field[x]) and field[x][y].isdigit():
#         temp += field[x][y]
#         y += 1
#     numbers.append(int(temp))

# print(sum(numbers))
