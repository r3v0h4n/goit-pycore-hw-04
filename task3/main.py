from pathlib import Path
import sys
from colorama import Fore

def tree(path, level=0):
    indent = " " * 4 * level
    sub_indent = " " * 4 * (level + 1)
    
    print(f"{Fore.BLUE}{indent}{path.name}/")

    dir_content = list(path.iterdir())  
    for filepath in dir_content:
        if filepath.is_dir():
            tree(Path(filepath), level=level + 1)
        else:
            print(f"{Fore.YELLOW}{sub_indent}{filepath.name}")

def main():
    if len(sys.argv) != 2:
        print("Please, provide path")
        return
    
    path = Path(sys.argv[1])
    if not path.exists():
        print(f"Path {path} does not exist")
        return
    
    if path.is_file():
        print(f"Path {path} is a file")
        return
    
    tree(path)
    print(Fore.RESET)

if __name__ == "__main__":
    main()