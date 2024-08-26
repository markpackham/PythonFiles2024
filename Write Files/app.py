# Files data to files

characters = ["Mario", "Lugi", "Peach", "Yoshi", "Bowser", "Toad"]

def write_characters_to_file(filename):
    # Open file
    file = open(filename, 'w')

    # Write characters to file
    for c in characters:
        file.write(c)

    # Close file
    file.close()

    return

def main():
    write_characters_to_file('characters.txt')

if __name__ == "__main__":
    main()