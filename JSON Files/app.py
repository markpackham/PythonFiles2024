from pathlib import Path
# Handle Json (we import the whole module unlike Path where we just use "pathlib")
import json

path = Path(__file__).parent / 'characters.json'

characters = {
    "characters": [
        {"name": "Mario", "age": 25},
        {"name": "Luigi", "age": 27},
        {"name": "Peach", "age": 26},
        {"name": "Bowser", "age": 35},
    ]
}

def write_json():
    with path.open('w') as file:
        # We only want to indent 2 spaces when the file is written
        # If we didn't provide an indent they'd all sit on one line
        json.dump(characters, file, indent=2)
    return

def read_json():
    with path.open('r') as file:
        data = json.load(file)
    # We see the data presented as a Python Dictionary
    return data

def main():
    write_json()
    data = read_json()
    print(data)

if __name__ == "__main__":
    main()