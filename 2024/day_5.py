import networkx as nx
from collections import defaultdict


def part_one():

    # X|Y: if both page no X and page no Y are to in same update, then X must be printed at some point before Y

    with open('day_5_input.txt', 'r') as open_f:

        # First, build a data structure to represent page ordering rules
        # Mapping from keys X to all Ys, such that there is a rule X|Y
        page_ordering = defaultdict(list)
        while True:

            line = open_f.readline().strip()
            if not line:
                break
            x, y = line.split('|')
            page_ordering[x].append(y)

        # Now, go through each update (line of page numbers), and check if they're in right order
        # Store the incorrect ones too, while we're going through them, as we need them for part two
        total = 0
        incorrect = []
        while True:

            line = open_f.readline().strip()
            if not line:
                break

            pages = line.split(',')

            # Use transitive property: if X|Y and Y|Z then X|Z
            # So we only need to check adjacent pages for | property
            valid = all(pages[idx+1] in page_ordering[pages[idx]] for idx in range(len(pages)-1))

            if valid:
                # Sum middle page numbers
                total += int(pages[len(pages)//2])
            else:
                incorrect.append(pages)

    print(total)
    return page_ordering, incorrect


def part_two(page_ordering, incorrect):

    # Looking at ALL the rules together, it has cycles in it, and cannot be considered a DAG
    # Looking out only the sub-graph of rules for each update, we can find a DAG
    # Perform a transitive reduction on it, so resulting graph will just be one chain,
    # Then topologically sort it to get our sorted page numbers

    total = 0
    for update in incorrect:

        # Make a graph, only looking at edges (X|Y rules) if they are pages in our update. This will be a DAG
        G = nx.DiGraph()
        for x in filter(lambda p: p in update, page_ordering):
            for y in filter(lambda p: p in update, page_ordering[x]):
                G.add_edge(x, y)

        G = nx.transitive_reduction(G)
        sorted_update = list(nx.topological_sort(G))
        total += int(sorted_update[len(sorted_update)//2])

    print(total)


if __name__ == '__main__':

    page_ordering, incorrect = part_one()
    part_two(page_ordering, incorrect)
