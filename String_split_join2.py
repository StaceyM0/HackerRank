def split_and_join(line):
    newline = "-".join(line.split(" "))
    return newline

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)