import utility

lines = utility.inputs(parse=lambda x: x)

def split_range(rangeStr):
    return list(map(int, rangeStr.split('-')))
def contains_fully(line):
    elves = list(map(split_range, line.split(',')))

    # # Test is either range is fully in the other
    return (elves[0][0] >= elves[1][0] and elves[0][1] <= elves[1][1]) or (elves[1][0] >= elves[0][0] and elves[1][1] <= elves[0][1])

def contains_overlap(line):
    elves = list(map(split_range, line.split(',')))
    if (elves[0][0] <= elves[1][1] and elves[0][1] >= elves[1][0]) or (elves[1][0] <= elves[0][1] and elves[1][1] >= elves[0][0]):
        print(elves[0], elves[1])
        # print(elves[1])

    # # Test is either range is fully in the other
    return (elves[0][0] <= elves[1][1] and elves[0][1] >= elves[1][0]) or (elves[1][0] <= elves[0][1] and elves[1][1] >= elves[0][0])

def part1():
    count = 0

    for line in lines:
        if contains_fully(line):
            count += 1

    return utility.solution({ 'count': count })


def part2():
    count = 0

    for line in lines:
        if contains_overlap(line):
            count += 1

    return utility.solution({ 'count': count })


if __name__ == '__main__':
    utility.cli()
