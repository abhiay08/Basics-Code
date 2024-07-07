def generate_pattern():
    start = 6
    end = 9
    sequence = list(range(start, end + 1)) + list(range(1, 9))

    while sequence:
        print(' '.join(map(str, sequence)))
        sequence.pop(0)

generate_pattern()
