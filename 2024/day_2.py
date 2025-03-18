def is_safe(report):
    # `report` is a list of numbers
    ordering = (all(report[i] > report[i + 1] for i in range(len(report) - 1)) or
                all(report[i] < report[i + 1] for i in range(len(report) - 1)))
    differing = all(1 <= abs(report[i] - report[i + 1]) <= 3 for i in range(len(report) - 1))

    return ordering and differing


def part_one():

    # Safe if and only if
    # (i) The levels are either all increasing or all decreasing
    # (ii) Any two adjacent levels differ by at least one and at most three

    safe_reports = 0
    with open('day_2_input.txt', 'r') as open_f:
        for line in open_f:
            numbers = [int(n) for n in line.strip().split(' ')]
            if is_safe(numbers):
                safe_reports += 1

    print(safe_reports)


def part_two():

    safe_reports = 0
    with open('day_2_input.txt', 'r') as open_f:
        for line in open_f:
            numbers = [int(n) for n in line.strip().split(' ')]
            if is_safe(numbers):
                safe_reports += 1
            else:
                # Try and remove one possible level, and see if remaining report is safe
                for i in range(len(numbers)):
                    if is_safe(numbers[:i] + numbers[i+1:]):
                        safe_reports += 1
                        break

    print(safe_reports)


if __name__ == '__main__':

    # part_one()
    part_two()
