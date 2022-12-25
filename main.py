# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def print_hi():
    print('Running...')
    given_input = open('input.txt', 'r')
    count = 0

    while True:
        count += 1
        line = given_input.readline()

        if not line:
            break

    given_input.close()
    print(count)



if __name__ == '__main__':
    print_hi()
