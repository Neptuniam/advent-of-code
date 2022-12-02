import utility

def create_list():
    lines = utility.inputs(parse=lambda x: x, hide_empty=False)
    line_count = len(lines)

    elf_calories = []

    current_sum = 0

    for index in range(line_count):
        line = lines[index]

        if line:
            # Sum the elf's calories until we reach an empty line, that shows we are on the next elf
            current_sum += int(line)
        
        if not line or index == line_count-1:
            elf_calories.append(current_sum)
            current_sum = 0
    
    return elf_calories

def part1():
    return utility.solution({ 'mostCalories': max(create_list()) })

def part2():
    sorted = create_list()
    sorted.sort()

    line_count = len(sorted)

    return utility.solution({ 'top_3_calories': sum([ sorted[line_count-1], sorted[line_count-2], sorted[line_count-3] ]) })


if __name__ == '__main__':
    utility.cli()
