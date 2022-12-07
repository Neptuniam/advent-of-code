import utility

inputs = utility.inputs(parse=lambda x: x)

def parser(packet_size):
    packet = ''

    for index, char in enumerate(inputs[0]):
        print(char, index)
        packet += char

        if len(packet) > packet_size:
            packet = packet[1::]

        if len(set(packet)) == packet_size:
            return index+1


def part1():

    return utility.solution({ 'index': parser(4) })


def part2():

    return utility.solution({ 'index': parser(14) })


if __name__ == '__main__':
    utility.cli()
