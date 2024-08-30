from pathlib import Path

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
    return

def read_json():
    return

def main():
    write_json()
    data = read_json()
    print(data)

if __name__ == "__main__":
    main()