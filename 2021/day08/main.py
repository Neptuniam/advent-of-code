import utility

inputs = utility.inputs(parse=lambda x: x)

def part1():
    count = 0

    for line in inputs:
        segments = line.split(' | ')[1].split(' ')

        for segment in segments:
            length = len(segment)
            if length == 2 or length == 4 or length == 3 or length == 7:
                count += 1

    return utility.solution({ 'count': count })


def part2():

    return utility.solution({ 'res': 0 })


if __name__ == '__main__':
    utility.cli()
