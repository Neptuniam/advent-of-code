import utility

inputs = utility.inputs(parse=lambda x: x)

def build_grid():
    # Option 1 causes some sort of pointer issue?
    # grid = [['.']*10]*10
    grid = []
    for i in range(1000):
        grid.append([0]*1000)
    return grid

def parse_points(line):
    points = line.split(' -> ')
    points[0] = points[0].split(',')
    points[1] = points[1].split(',')

    points[0] = {
        'x': int(points[0][0]),
        'y': int(points[0][1])
    }
    points[1] = {
        'x': int(points[1][0]),
        'y': int(points[1][1])
    }
    return points

def count_2s(grid):
    count2 = 0
    for row in grid:
        for col in row:
            if col >= 2:
                count2 += 1
    return count2

def part1():
    grid = build_grid()

    for line in inputs:
        points = parse_points(line)

        # Ignore diaganol lines
        if points[0]['x'] != points[1]['x'] and points[0]['y'] != points[1]['y']:
            continue

        distance_in_x = abs(points[0]['x'] - points[1]['x'])+1
        distance_in_y = abs(points[0]['y'] - points[1]['y'])+1

        direction_x = 1 if points[0]['x'] < points[1]['x'] else -1
        direction_y = 1 if points[0]['y'] < points[1]['y'] else -1

        for x in range(distance_in_x):
            for y in range(distance_in_y):
                offset_x = points[0]['x'] + (x * direction_x)
                offset_y = points[0]['y'] + (y * direction_y)

                grid[offset_y][offset_x] += 1



    return utility.solution({ 'count2': count_2s(grid) })


def part2():
    grid = build_grid()

    for line in inputs:
        points = parse_points(line)

        distance_in_x = abs(points[0]['x'] - points[1]['x'])
        distance_in_y = abs(points[0]['y'] - points[1]['y'])

        is_diagonal = False
        # Ignore non 45 degree diaganol lines
        # At least one of the points need to match to be a straight line
        if points[0]['x'] != points[1]['x'] and points[0]['y'] != points[1]['y']:
            if distance_in_x != distance_in_y:
                continue
            else:
                is_diagonal = True

        direction_x = 1 if points[0]['x'] < points[1]['x'] else -1
        direction_y = 1 if points[0]['y'] < points[1]['y'] else -1

        if is_diagonal:
            for x in range(distance_in_x+1):
                offset_x = points[0]['x'] + (x * direction_x)
                offset_y = points[0]['y'] + (x * direction_y)

                grid[offset_y][offset_x] += 1
        else:
            for x in range(distance_in_x+1):
                for y in range(distance_in_y+1):
                    offset_x = points[0]['x'] + (x * direction_x)
                    offset_y = points[0]['y'] + (y * direction_y)

                    grid[offset_y][offset_x] += 1

    return utility.solution({ 'count2': count_2s(grid) })


if __name__ == '__main__':
    utility.cli()
