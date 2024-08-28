from pathlib import Path

def open_file():
    path = Path(__file__).parent / 'characters.txt'
    data = ["Mario", "Luigi", "Peach", "Yoshi", "Bowser"]

# Context mangers - allow us to work in files then automatically close when work done

def main():
    open_file()

if __name__ == "__main__":
    main()