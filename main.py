# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def is_prime(num) -> bool:
    from math import sqrt
    end = int(sqrt(num))
    for i in range(2, end + 1):
        if num % i == 0:
            return False
    if num == 1:
        return False
    return True


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    for i in range(100):
        if is_prime(i):
            print('%d' % i, end='\t')