# Reading files

def read_file():
    # Open file ("open()" path is relative to your position in the terminal not the app.py location itself)
    file = open('characters.txt', 'r')

    # Read file
    # content = file.read()
    # print(content)

    lines = file.readlines()

    for line in lines:
        print(line)

    # Close file
    file.close()

    return

def main():
    read_file()
    return

if __name__ == "__main__":
    main()