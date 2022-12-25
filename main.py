# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def parse_file():
    given_input = open('input.txt', 'r')
    lines = given_input.readlines()

    formatted_list = [item.strip() for item in lines]

    # print(f'Parsed file with {len(formatted_list)} lines')
    return formatted_list


def main():
    print('Running...')

    formatted_input = parse_file()

    current_max = 0
    running_count = 0
    sums = []
    for line in formatted_input:
        if line == '':
            sums.append(running_count)
            running_count = 0
        else:
            running_count += int(line)
    sums.sort(reverse=True)
    print(sum(sums[:3]))
    # while True:
    #     line = given_input.readline()
    #
    #     if not line:
    #         break
    #
    #     (current_max, running_count) = do_first_part(line, current_max, running_count)
    #

    # print(current_max)
    return current_max


def do_first_part(line, current_max, running_count):
    if line == '\n':
        if running_count > current_max:
            current_max = running_count
            print(current_max)
        running_count = 0
    else:
        running_count += int(line)
    return current_max, running_count


if __name__ == '__main__':
    answer = main()
    print(answer)
