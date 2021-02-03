def print_formatted(number):
    l = []
    for i in range(1, number+1):
        l.append([str(i), str(oct(i)[2:]), str(hex(i)[2:].upper()), str(bin(i)[2:])])
    space_padding = len(l[-1][3])

    for i in l:
        print(" ".join(a.rjust(space_padding) for a in i))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
