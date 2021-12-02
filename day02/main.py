import utility

inputs = utility.inputs(parse=lambda x: x)

def part1():
    depth = 0
    position = 0

    for line in inputs:
        split = line.split(' ')

        if len(split) == 2:
            direction = split[0]
            amount = int(split[1])

            if direction == 'forward':
                position += amount
            elif direction == 'up':
                depth -= amount
            elif direction == 'down':
                depth += amount
            else:
                print(f'failed to match: {direction}')

    return utility.solution({ 'position': depth*position })


def part2():
    aim = 0
    depth = 0
    position = 0

    for line in inputs:
        split = line.split(' ')

        if len(split) == 2:
            direction = split[0]
            amount = int(split[1])

            if direction == 'forward':
                position += amount
                depth += (aim * amount)
            elif direction == 'up':
                aim -= amount
            elif direction == 'down':
                aim += amount
            else:
                print(f'failed to match: {direction}')

    return utility.solution({ 'position': depth*position })


if __name__ == '__main__':
    utility.cli()
