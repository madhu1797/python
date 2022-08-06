"""
textwrap:  split the string based on max width
input:  hello world,   2
output: he, ll, o , wo, rl, d

"""

import textwrap

def wrap(string, max_width):
    list_1 = textwrap.wrap(string, width=max_width)
    list_1 = " ".join(list_1)
    string=textwrap.fill(list_1,max_width)
    return string
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
