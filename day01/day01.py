from math import dist

def get_input(fp):
    with open(fp, 'r') as f:
        input_data = [row.strip('\n').split() for row in f.readlines()]
    distances_1 = [int(row[0]) for row in input_data]
    distances_2 = [int(row[1]) for row in input_data]

    list_1 = list(sorted(distances_1))
    list_2 = list(sorted(distances_2))

    return list_1, list_2


def calc_distances(list_1, list_2):
    distances = []
    for idx in range(len(list_1)):
        distances.append(dist([list_1[idx]], [list_2[idx]]))

    return sum(distances)


def count_numbers(list_1, list_2):
    count_result = []
    for num in list_1:
        count_result.append(num*list_2.count(num))
    return count_result


def total_distance(fp):
    list_1, list_2 = get_input(fp)
    total_dist = calc_distances(list_1, list_2)
    return int(total_dist)


def similarity_score(fp):
    list_1, list_2 = get_input(fp)
    count_result = count_numbers(list_1, list_2)
    return sum(count_result)

# part 1 result
print(total_distance('input.txt')

# part 2 result
print(similarity_score('input.txt'))