import utility

inputs = utility.inputs(parse=lambda x: x)

def pick_winner(player_1, player_2):
    points = 0

    if player_2 == 'X': # Rock
        points = 1

        if player_1 == 'A': # Rock
            # Tied
            points += 3
        elif player_1 == 'C': #Scissors
            # I win
            points += 6
    elif player_2 == 'Y': # Paper
        points = 2

        if player_1 == 'B': # Paper
            # Tied
            points += 3
        elif player_1 == 'A': # Rock
            # I win
            points += 6
    elif player_2 == 'Z': # Scissors
        points = 3

        if player_1 == 'C': # Scissors
            # Tied
            points += 3
        elif player_1 == 'B': # Paper
            # I win
            points += 6

    return points

def pick_correct_shape(player_1, player_2):
    points = 0

    if player_2 == 'X': # Lose
        if player_1 == 'A': # Rock
            points = 3 + 0
        elif player_1 == 'B': # Paper
            points = 1 + 0
        elif player_1 == 'C': # Scissors
            points = 2 + 0
    elif player_2 == 'Y': # Draw
        if player_1 == 'A': # Rock
            points = 1 + 3
        elif player_1 == 'B': # Paper
            points = 2 + 3
        elif player_1 == 'C': # Scissors
            points = 3 + 3
    elif player_2 == 'Z': # Win
        if player_1 == 'A': # Rock
            points = 2 + 6
        elif player_1 == 'B': # Paper
            points = 3 + 6
        elif player_1 == 'C': # Scissors
            points = 1 + 6

    print(points)
    return points

def part1():
    lines = utility.inputs(parse=lambda x: x.split(' '))
    total_points = 0

    for line in lines:
        total_points += pick_winner(line[0], line[1])

    return utility.solution({ 'total_points': total_points })


def part2():
    lines = utility.inputs(parse=lambda x: x.split(' '))
    total_points = 0

    for line in lines:
        total_points += pick_correct_shape(line[0], line[1])

    return utility.solution({ 'total_points': total_points })


if __name__ == '__main__':
    utility.cli()
