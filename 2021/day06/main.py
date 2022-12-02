import utility

inputs = utility.inputs(parse=lambda x: x)

def simulate_population(days):
    fishes = inputs[0].split(',')
    fishes = list(map(lambda x: int(x), fishes))
    fishes.sort()
    fishes_by_days_left = [0] * 9

    for fish in fishes:
        fishes_by_days_left[fish] += 1

    for day in range(days):
        fishes_birthing = fishes_by_days_left.pop(0)

        fishes_by_days_left[6] += fishes_birthing
        fishes_by_days_left.append(fishes_birthing)

    sum = 0
    for fish_day in fishes_by_days_left:
        sum += fish_day

    return sum

def part1():
    return utility.solution({ 'fish_count': simulate_population(80) })


def part2():
    return utility.solution({ 'fish_count': simulate_population(256) })


if __name__ == '__main__':
    utility.cli()
