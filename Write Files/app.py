# Files data to files

characters = ["Mario", "Lugi", "Peach", "Yoshi", "Bowser", "Toad"]

def write_characters_to_file(filename):
    # Open file
    # file = open(filename, 'w')

    # with w+ we can Read & Write
    file = open(filename, 'w+')

    # Write characters to file with new line
    for c in characters:
        file.write(c + "\n")

    # Reset pointer back to the start via see() or we'd read the end of the file with nothing
    file.seek(0,0)

    content = file.read()
    print(content)

    # Close file
    file.close()

    return

def main():
    write_characters_to_file('characters.txt')

if __name__ == "__main__":
    main()