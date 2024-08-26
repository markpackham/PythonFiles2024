# pathlib module (easier than using the "os" module although both are built into python)
from pathlib import Path

file = open('characters.txt', 'r')

def create_path():
    # Construct new path object
    # path gets determined at runtime
    script_dir = Path(__file__)
    # print(script_dir.parent)

    # Add a folder to this path (won't exist yet)
    path = script_dir / 'characters'
    
    # Make the folder exist
    path.mkdir(parents=True, exist_ok=True)

    return

def main():
    create_path()

if __name__ == "__main__":
    main()