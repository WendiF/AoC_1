# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def main():
    print('Running...')
    given_input = open('input.txt', 'r')
    count = 0
    current_max = 0
    running_count = 0

    while True:
        count += 1
        line = given_input.readline()

        if not line:
            break

        (current_max, running_count) = do_first_part(line, current_max, running_count)


    given_input.close()
    print(count)
    print(current_max)
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
