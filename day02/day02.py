import numpy as np


def get_input(fp):
    with open(fp, 'r') as f:
        input_data = [row.strip('\n').split() for row in f.readlines()]
    input_data = [[int(num) for num in row] for row in input_data]
    return input_data


def mark_safe(x):
    if np.any([(np.sum(np.diff(x) > 0) > len(x) - 2),(np.sum(np.diff(x) < 0) > len(x) - 2)]):
        diffmin = np.abs(np.diff(x)).min()
        diffmax = np.abs(np.diff(x)).max()

        return 1 if diffmin >= 1 and diffmax <= 3 else 0
    return 0


def mark_safer(x):
    if mark_safe(x) == 1:
        return 1
    else:
        for i, num in enumerate(x):
            if mark_safe(x[:i] + x[i+1:]) == 1:
                return 1
    return 0


def check_reports(fp, dampener=False):
    report = get_input(fp)
    return sum([mark_safe(x) for x in report]) if not dampener else sum([mark_safer(x) for x in report])

print('part 1', check_reports('input.txt', dampener=False))
print('part 2', check_reports('input.txt', dampener=True))
