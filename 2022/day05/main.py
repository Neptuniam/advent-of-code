import utility
import re

lines = utility.inputs(parse=lambda x: x)

def part1():
    final_tops = ''
    stack_of_stacks = []
    building_stacks = True

    for line in lines:
        if line[1] == '1':
            building_stacks = False
            continue
        
        if building_stacks:
            stack_index=0
            char_index=1
            while char_index < len(line):
                # New stack
                if stack_index >= len(stack_of_stacks):
                    stack_of_stacks.append([])
                
                if line[char_index] != ' ':
                    stack_of_stacks[stack_index].insert(0, line[char_index])

                char_index += 4
                stack_index += 1
        else:
            # convert the english instructions to the basics
            # <qty>, <from>, <to>
            instructions = list(map(int, re.split(r'\D+',line)[1::]))

            _qty = instructions[0]
            _from = instructions[1]-1
            _to = instructions[2]-1

            for qty in range(_qty):
                stack_of_stacks[_to].append(stack_of_stacks[_from].pop())

    # Add Tops
    for i in range(len(stack_of_stacks)):
        final_tops += stack_of_stacks[i][-1]

    return utility.solution({ 'final_tops': final_tops })


def part2():
    final_tops = ''
    stack_of_stacks = []
    building_stacks = True

    for line in lines:
        if line[1] == '1':
            building_stacks = False
            continue
        
        if building_stacks:
            stack_index=0
            char_index=1
            while char_index < len(line):
                # New stack
                if stack_index >= len(stack_of_stacks):
                    stack_of_stacks.append([])
                
                if line[char_index] != ' ':
                    stack_of_stacks[stack_index].insert(0, line[char_index])

                char_index += 4
                stack_index += 1
        else:
            # convert the english instructions to the basics
            # <qty>, <from>, <to>
            instructions = list(map(int, re.split(r'\D+',line)[1::]))

            _qty = instructions[0]
            _from = instructions[1]-1
            _to = instructions[2]-1

            _moving_index = len(stack_of_stacks[_from])-_qty

            for qty in range(_qty):
                stack_of_stacks[_to].append(stack_of_stacks[_from][_moving_index])
                del stack_of_stacks[_from][_moving_index]

    # Add Tops
    for i in range(len(stack_of_stacks)):
        final_tops += stack_of_stacks[i][-1]

    return utility.solution({ 'final_tops': final_tops })


if __name__ == '__main__':
    utility.cli()
