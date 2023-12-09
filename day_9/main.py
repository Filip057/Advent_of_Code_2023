def process_line(line):
    if all(x == 0 for x in line):
        return 0
    
    differences = [y - x for x,y in zip(line, line[1:])]

    return line[-1] + process_line(differences)

print(sum([process_line(list(map(int, line.split()))) for line in open("day_9/data.txt", "r").read().splitlines()]))