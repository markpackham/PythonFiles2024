from pathlib import Path

def open_file():
    path = Path(__file__).parent / 'characters.txt'
    data = ["Mario", "Luigi", "Peach", "Yoshi", "Bowser"]

# Context Mangers - allow us to work in files then automatically close when work done
with path.open('w') as file:
    for character in data:
        file.write(character + "\n")

def main():
    open_file()

if __name__ == "__main__":
    main()