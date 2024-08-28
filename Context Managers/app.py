from pathlib import Path

def open_file():
    path = Path(__file__).parent / 'characters.txt'
    data = ["Mario", "Luigi", "Peach", "Yoshi", "Bowser"]

# Context Mangers - allow us to work in files then automatically close when work done
# "with" is the most common context manger
# "Context managers allow you to allocate and release resources precisely when you want to"
# https://book.pythontips.com/en/latest/context_managers.html
# The main advantage of using a "with" statement is that it makes sure our file is 
# closed without paying attention to how the nested block exits. Hence no file.close()
    with path.open('w') as file:
        for character in data:
            file.write(character + "\n")

def main():
    open_file()

if __name__ == "__main__":
    main()