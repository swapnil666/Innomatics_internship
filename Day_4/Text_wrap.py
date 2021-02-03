import textwrap

def wrap(string, max_width):
    A = textwrap.wrap(string,max_width)
    B = textwrap.fill(string,max_width)
    return B

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
