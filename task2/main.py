import pathlib

def parse_cat_info(line):
    parts = line.split(",")
    return {"id": parts[0], "name": parts[1], "age": parts[2]}

def get_cats_info(path):
    current_dir = pathlib.Path(__file__).parent
    try:
        with open(current_dir / path, "r", encoding="UTF-8") as file:        
            return [parse_cat_info(line) for line in file.read().splitlines()]
    except FileNotFoundError:
        print("File not found")
    except Exception:
        print("Unexpected error")
    return []

if __name__ == "__main__":
    cats_info = get_cats_info("cats.txt")
    print(cats_info)