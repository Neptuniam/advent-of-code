import utility

def coundDifferences(list):
    increaseAmount = 0
    decreaseAmount = 0
    previousLine = None

    for line in list:
        # can't compare on the first line, atom likes to end files with empty line
        if previousLine and line:
            if line == previousLine:
                print(str(line) + ' (no change)')
            elif line > previousLine:
                print(str(line) + ' (increased)')
                increaseAmount += 1
            else:
                print(str(line) + ' (decreased)')
                decreaseAmount += 1
        else:
            print(str(line) + ' (N/A - no previous sum)')
        previousLine = line

    return utility.solution({ 'increaseAmount': increaseAmount, 'decreaseAmount': decreaseAmount })

def part1():
    inputs = utility.inputs(parse=lambda x: int(x))
    return coundDifferences(inputs)


def part2():
    inputs = utility.inputs(parse=lambda x: int(x))
    sums = []

    for index in range(len(inputs) - 2):
        sums.append(inputs[index]+inputs[index+1]+inputs[index+2])

    return coundDifferences(sums)


if __name__ == '__main__':
    utility.cli()
