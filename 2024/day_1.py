import bisect
from collections import defaultdict


def part_one():

    # Much more efficient to maintain a sorted list as we build them, as opposed to sorting at the end
    # The time gains are minimal, as it's such a small file anyway, but good practice!
    left, right = [], []
    with open('day_1_input.txt', 'r') as open_f:
        for line in open_f:
            numbers = line.strip().split('   ')
            bisect.insort(left, int(numbers[0]))
            bisect.insort(right, int(numbers[1]))

    print(sum(abs(left[i] - right[i]) for i in range(len(left))))


def part_two():

    # Again, consider the best data structure to answer the question WHEN building the list
    # Rather, than loading in as a list, and working with it after that
    # Left & right numbers represented as a dictionary, mapping from number to count
    # We use a default dict for syntax simplicity, but also important when indexing during calculation after that
    # numbers not present map to 0 for multiplication
    left, right = defaultdict(int), defaultdict(int)
    with open('day_1_input.txt', 'r') as open_f:
        for line in open_f:
            numbers = line.strip().split('   ')
            left[int(numbers[0])] += 1
            right[int(numbers[1])] += 1

    print(sum(key * left[key] * right[key] for key in left))


if __name__ == '__main__':

    # part_one()
    part_two()
