import utility

inputs = utility.inputs(parse=lambda x: x)

def part1():
    # We are making the assumption all lines have the same number of bits
    bit_count = len(inputs[0])
    gamma = ''
    epsilon = ''

    for i in range(bit_count):
        count1 = 0
        count0 = 0

        for line in inputs:
            if line[i] == '1':
                count1 += 1
            elif line[i] == '0':
                count0 += 1
            else:
                print(f'unknown input {line[i]}')

        if count1 == count0:
            print('tied, what do we do here?')
        elif count1 > count0:
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'

    return utility.solution({ 'power_consumption': int(gamma, 2) * int(epsilon, 2) })


def find_value(value):
    # We are making the assumption all lines have the same number of bits
    bit_count = len(inputs[0])
    gamma = ''
    epsilon = ''
    list = inputs

    for i in range(bit_count):
        count1 = 0
        list1 = []
        count0 = 0
        list0 = []

        for line in list:
            if line[i] == '1':
                count1 += 1
                list1.append(line)
            elif line[i] == '0':
                count0 += 1
                list0.append(line)
            else:
                print(f'unknown input {line[i]}')

        if value == 'gamma':
            if count1 >= count0:
                list = list1
            else:
                list = list0
        else:
            if count1 < count0:
                list = list1
            else:
                list = list0

        if (len(list) == 1):
            return int(list[0], 2)
def part2():
    print(find_value('gamma'))
    print(find_value('epsilon'))

    return utility.solution({ 'res': find_value('gamma') * find_value('epsilon') })


if __name__ == '__main__':
    utility.cli()
