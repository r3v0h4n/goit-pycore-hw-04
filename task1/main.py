import pathlib


def parse_salary(line):
    return float(line.split(",")[1])

def total_salary(path):
    current_dir = pathlib.Path(__file__).parent

    try:
        with open(current_dir / path, "r", encoding="UTF-8") as file:        
            salaries = [parse_salary(line) for line in file.read().splitlines()]
    except FileNotFoundError:
        print("File not found")
    except Exception:
        print("Unexpected error")
    return 0, 0
    
    salary_sum = sum(salaries)
    avarage_salary = salary_sum / len(salaries)
    return salary_sum, avarage_salary


if __name__ == "__main__":
    total, average = total_salary("salaries.txt")
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")