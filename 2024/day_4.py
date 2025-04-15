def part_one():

    char_array = []

    with open('day_4_input.txt', 'r') as open_f:
        for line in open_f:
            char_array.append(line.strip())

    rows = len(char_array)
    cols = len(char_array[0])

    # Words can be: horizontal, vertical, diagonal, and any of these backwards. Also overlapping is allowed.
    # We look in four directions: right, down, down-right, down-left
    # Look for both XMAS and SAMX, so we don't have to look backwards in the opposite four directions

    # Draw resulting array showing all places XMAS occurs, replacing irrelevant characters with '.', just like example
    result = [["." for i in range(cols)] for j in range(rows)]

    total = 0
    for row in range(rows):
        for col in range(cols):

            # Horizontal
            if col <= cols-4:
                if char_array[row][col:col+4] in ['XMAS', 'SAMX']:
                    total += 1
                    result[row][col:col+4] = char_array[row][col:col+4]

            # Vertical
            if row <= rows-4:
                if ''.join(char_array[row+i][col] for i in range(4)) in ['XMAS', 'SAMX']:
                    total += 1
                    for i in range(4):
                        result[row+i][col] = char_array[row+i][col]

            # Diagonal (Down-Right)
            if col <= cols-4 and row <= rows-4:
                if ''.join(char_array[row+i][col+i] for i in range(4)) in ['XMAS', 'SAMX']:
                    total += 1
                    for i in range(4):
                        result[row+i][col+i] = char_array[row+i][col+i]

            # Diagonal (Down-Left)
            if col >= 3 and row <= rows-4:
                if ''.join(char_array[row+i][col-i] for i in range(4)) in ['XMAS', 'SAMX']:
                    total += 1
                    for i in range(4):
                        result[row+i][col-i] = char_array[row+i][col-i]

    for r in result:
        print(r)

    print(total)


def part_two():

    char_array = []

    with open('day_4_input.txt', 'r') as open_f:
        for line in open_f:
            char_array.append(line.strip())

    rows = len(char_array)
    cols = len(char_array[0])

    total = 0
    for row in range(1, rows-1):
        for col in range(1, cols-1):

            # Consider each element as center of the X, and look in diagonals if it forms an X-MAS

            if (''.join(char_array[row+i][col+i] for i in range(-1, 2)) in ['MAS', 'SAM'] and
                    ''.join(char_array[row+i][col-i] for i in range(-1, 2)) in ['MAS', 'SAM']):
                total += 1

    print(total)


if __name__ == '__main__':

    part_one()
    part_two()
