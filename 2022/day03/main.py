import utility

lines = utility.inputs(parse=lambda x: x)


def find_common(compartment_1, compartment_2):
    return list(set(list(compartment_1)).intersection(list(compartment_2)))[0]
def find_common(rucksack_1, rucksack_2, rucksack_3):
    return list(set(list(rucksack_1)).intersection(list(rucksack_2)).intersection(list(rucksack_3)))[0]

def convert_to_priority(char):
    return ord(char)-38 if char.isupper() else ord(char)-96

def part1():
    sum = 0

    for line in lines:
        sum += convert_to_priority(find_common(line[:len(line)//2], line[len(line)//2:]))

    return utility.solution({ 'sum': sum })


def part2():
    sum = 0

    for chunk in utility.partition(lines, 3):
        sum += convert_to_priority(find_common(chunk[0], chunk[1], chunk[2]))

    return utility.solution({ 'sum': sum })


if __name__ == '__main__':
    utility.cli()
