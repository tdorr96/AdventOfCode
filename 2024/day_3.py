import regex

# Valid instructions are "mul(X,Y)", where X and Y are 1-3 digit numbers
# Use regex to find patterns of valid mul instructions, with capturing groups to find the X and Y to multiply
mul_regex = regex.compile(r"mul\((\d{1,3}),(\d{1,3})\)")


def sum_mul_instructions(text):
    # Uses regex to find all the valid mul instructions in a `text`, and sums all the resulting multiplications

    return sum(int(match[0]) * int(match[1]) for match in mul_regex.findall(text))


def part_one():

    # Use regex to search text string for all valid occurrences of `mul(X,Y)`
    # Neat way, but not very efficient if text file was massive (see part two for character-by-character reading)

    with open('day_3_input.txt', 'r') as open_f:
        text = open_f.read()

    print(sum_mul_instructions(text))


def part_two():

    # More efficient approach this time, we read file character by character
    # We have a buffer string, that accumulates characters between any occurrence of do() and don't()
    # At each "boundary", we sum the multiplications if text was after a do(), and reset buffer

    total = 0
    buffer = ""
    enabled = True

    with open('day_3_input.txt', 'r') as open_f:

        while True:

            # Read one character at a time, until EOF
            ch = open_f.read(1)
            if not ch:
                break

            buffer += ch

            if buffer[-7:] == "don't()" or buffer[-4:] == "do()":
                if enabled:
                    total += sum_mul_instructions(buffer)
                enabled = buffer[-4:] == "do()"
                buffer = ""

        # Process last text buffer
        if enabled:
            total += sum_mul_instructions(buffer)

    print(total)


if __name__ == '__main__':

    part_one()
    part_two()
