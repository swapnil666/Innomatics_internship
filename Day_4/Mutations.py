def mutate_string(string, position, character):
    A = (s[:int(i)] + c + s[int(i)+1:])
    return A

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
