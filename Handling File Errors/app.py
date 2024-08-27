from pathlib import Path

def open_file():
    path = Path(__file__).parent
    path = path / 'does' / 'not' / 'exist.txt'

    try:
        file = path.open('r')
        content = file.read()
        print(content)
        file.close()
    except FileExistsError:
        print(f"{path} does not exist")
    # Catch all error block if the error isn't FileExistsError
    except Exception as e:
        print(f"Unexpected error: {e}")
    
    print('*** End of Function! ***')

def main():
    open_file()

if __name__ == "__main__":
    main()