import string
def split_and_join(line):
    # write your code here
    line= line.split(" ")
    final= "-".join(line)
    return final

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
