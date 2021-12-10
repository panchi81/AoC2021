#! venv\Scripts\python.exe
from pathlib import Path


def main():
    f_path = Path("input\\1.txt")

    if f_path.exists():
        try:
            with open(f_path, "r") as f_in:
                reader = f_in.readlines()
        except FileExistsError:
            print(f"File Error: {f_path}")

        increases = sum(
            int(row) > int(reader[num - 1]) for num, row in enumerate(reader)
        )
        print(increases)


if __name__ == "__main__":
    main()
