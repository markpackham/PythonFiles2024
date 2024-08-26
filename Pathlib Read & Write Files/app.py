# pathlib module (easier than using the "os" module although both are built into python)
from pathlib import Path

file = open('characters.txt', 'r')

def create_path():
    script_dir = Path(__file__).parent
    # print(script_dir.parent)

    # Add a folder to this path (won't exist yet)
    path = script_dir / 'characters'
    
    # Make the folder exist
    path.mkdir(parents=True, exist_ok=True)

    # Add absolute path to file which doesn't yet exist
    path = path / 'zelda.txt'

    # Use open method on "path" so it will already know of the path's existence
    # so we can avoid having to put path in as an argument
    # file = path.open('r')
    # content = file.read()
    # print(content)

    file.close()

    content = path.read_text()
    print(content)

    return

def main():
    create_path()

if __name__ == "__main__":
    main()