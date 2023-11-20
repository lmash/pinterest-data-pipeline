from itertools import cycle

counter = cycle('123')
counter_file_mapping = {
    '1': 'pin_result',
    '2': 'geo_result',
    '3': 'user_result'
}

with open("user_posting.txt") as fh:
    lines = fh.readlines()

for line in lines:
    file_number = next(counter)
    print(f"{counter_file_mapping[file_number]}: {line}")
