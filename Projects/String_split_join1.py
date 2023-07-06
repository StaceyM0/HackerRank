


string = line.split()
result = "-".join(string)
return result

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
