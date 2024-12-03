from collections import defaultdict


def main():
    left_list, right_list = create_list("input.txt")
    frequencies = defaultdict(int)

    # Part One
    output = 0
    for left_id, right_id in zip(sorted(left_list), sorted(right_list)):
        output += abs(left_id - right_id)

    print(output)

    ## Part Two
    output = 0
    for right_id in right_list:
        frequencies[right_id] += 1

    for left_id in left_list:
        output += left_id * frequencies[left_id]

    print(output)


def create_list(file_path: str):
    left_list = []
    right_list = []

    with open(file_path) as file:
        for line in file:
            left_id, right_id = line.split()
            left_list.append(int(left_id))
            right_list.append(int(right_id))

    return left_list, right_list


main()
