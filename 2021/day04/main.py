import utility

inputs = utility.inputs(parse=lambda x: x, hide_empty=False)

def build_board(inputs):
    board = []

    for line in inputs:
        if not line:
            return board

        row = []
        for num in line.split(' '):
            if num:
                row.append({ 'val': num, 'selected': False })
        board.append(row)

    return board
def build_boards():
    boards = []
    inputs.pop(0)

    board_lines = []
    for line in inputs:
        if line:
            board_lines.append(line)
        else:
            boards.append(build_board(board_lines))
            board_lines = []
    return boards

def check_call(board, call):
    for row in board:
        for col in row:
            if col['val'] == call:
                col['selected'] = True
def check_win(board):
    amount_to_win = len(board[0])
    col_sums = [0]*amount_to_win

    for row in board:
        selected_in_row = 0
        for col_index in range(len(row)):
            col = row[col_index]

            if col['selected'] == True:
                selected_in_row += 1
                col_sums[col_index] += 1

        if selected_in_row == amount_to_win:
            return True

    for col_sum in col_sums:
        if col_sum == amount_to_win:
            return True

    return False

def find_winner(calls, boards):
    for call in calls:
        for board in boards:
            check_call(board, call)
        for index in range(len(boards)):
            if (check_win(boards[index])):
                return { 'index': index, 'call': call }
    return None

def sum_winner(board, last_called):
    sum_unmarked = 0

    for row in board:
        for col in row:
            if not col['selected']:
                sum_unmarked += int(col['val'])

    return sum_unmarked * last_called

def part1():
    calls = inputs.pop(0).split(',')
    boards = build_boards()
    res = find_winner(calls, boards)

    if res is not None:
        index = int(res['index'])
        call = int(res['call'])
        return utility.solution({ 'res': sum_winner(boards[index], call) })
    else:
        print('Failed to find winner')


    return utility.solution({ 'res': -1 })


def part2():
    calls = inputs.pop(0).split(',')
    boards = build_boards()

    while len(boards) > 1:
        res = find_winner(calls, boards)
        index = int(res['index'])

        if index >= 0:
            del boards[index]
        else:
            print('no winner found')
            return utility.solution({ 'res': -1 })

    res = find_winner(calls, boards)

    index = int(res['index'])
    call = int(res['call'])
    return utility.solution({ 'res': sum_winner(boards[index], call) })


if __name__ == '__main__':
    utility.cli()
