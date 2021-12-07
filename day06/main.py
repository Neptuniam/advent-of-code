import utility

inputs = utility.inputs(parse=lambda x: x)

def simulate_population(days):
    fishes = inputs[0].split(',')
    fishes = list(map(lambda x: int(x), fishes))

    for day in range(days):
        print(f'Day: {day}')
        toAdd = []

        for i in range(len(fishes)):
            fishes[i] -= 1

            if fishes[i] < 0:
                fishes[i] = 6
                toAdd.append(8)

        # Add the baby fish at the end of the day to not mess with the above for loop
        for newFish in toAdd:
            fishes.append(newFish)
        # print(f'After {day+1} days: {fishes}')

    return len(fishes)

def part1():
    return utility.solution({ 'fish_count': simulate_population(80) })


def part2():
    return utility.solution({ 'fish_count': simulate_population(256) })


if __name__ == '__main__':
    utility.cli()
