import re
regex_str = '(mul\(\d+,\d+\))'


def get_input(fp):
    with open(fp, 'r') as f:
        input_data = f.read()
    return input_data


def calc_result(input_data):
    result = re.findall(regex_str, input_data)
    final_number = sum([int(x.split(',')[0].split('(')[1]) * int(x.split(',')[1].split(')')[0]) for x in result])
    return final_number


def do_filter(scrambled_text):
    do_split = scrambled_text.split('do()')
    do_list = [x.split("don't()")[0] for x in do_split]
    return sum([calc_result(y) for y in do_list]) 


def part_one(fp):
    return calc_result(get_input(fp))


def part_two(fp):
    return do_filter(get_input(fp))

print('part 1', part_one('input.txt'))
print('part 2', part_two('input.txt'))
