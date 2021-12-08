import utility
import statistics

inputs = utility.inputs(parse=lambda x: x)



def part1():
    def total_distance_to_point(crabs, point):
        sum = 0
        for crab in crabs:
            sum += abs(crab - point)
        return sum

    crabs = inputs[0].split(',')
    crabs = list(map(lambda x: int(x), crabs))
    crabs.sort()
    highest_point = crabs[len(crabs)-1]

    smallest_fuel = total_distance_to_point(crabs, 0)
    for i in range(highest_point):
        _fuel = total_distance_to_point(crabs, i)

        if _fuel < smallest_fuel:
            smallest_fuel = _fuel

    return utility.solution({ 'smallest_fuel': smallest_fuel })


def part2():
    def total_distance_to_point(crabs, point):
        sum = 0
        for crab in crabs:
            distance = abs(crab - point)
            count = 0
            for i in range(distance):
                count += i+1
            sum += count

        return sum

    crabs = inputs[0].split(',')
    crabs = list(map(lambda x: int(x), crabs))
    crabs.sort()
    highest_point = crabs[len(crabs)-1]

    smallest_fuel = total_distance_to_point(crabs, 0)
    for i in range(highest_point):
        _fuel = total_distance_to_point(crabs, i)

        if _fuel < smallest_fuel:
            smallest_fuel = _fuel

    return utility.solution({ 'smallest_fuel': smallest_fuel })


if __name__ == '__main__':
    utility.cli()
