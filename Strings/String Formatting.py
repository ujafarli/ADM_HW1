def print_formatted(number):
    # your code goes here
    wid = len("{0:b}".format(number))

    # from  1 to number itself print decimal, octal, hexadecimal and binary format
    for i in range(1, number+1):
        print("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width = wid))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
