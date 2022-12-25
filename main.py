# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def parse_file():
    given_input = open('input_2.txt', 'r')
    lines = given_input.readlines()

    formatted_list = [item.strip() for item in lines]

    return formatted_list


def main():
    print('Running...')

    formatted_input = parse_file()

    return "foo"


if __name__ == '__main__':
    answer = main()
    print(answer)
