# Append data to files

more_characters = ["Diddy Kong", "Donkey Kong", "Wario"]

def write_characters_to_file(filename):
    # Open file
    file = open(filename, 'a')

    # Append to file
    for c in more_characters:
        file.write(c + "\n")

    # Close file
    file.close()

    return

def main():
    write_characters_to_file('characters.txt')

if __name__ == "__main__":
    main()