#! venv\Scripts\python.exe
from pathlib import Path


def main():
    f_path = Path("input\\1.txt")

    if f_path.exists():
        try:
            with open(f_path, "r") as f_in:
                reader = [int(row) for row in f_in.read().splitlines()]

        except FileExistsError:
            print(f"File Error: {f_path}")

        increases = sum(
            sum(reader[i : i + 3]) > sum(reader[i - 1 : i + 2])
            for i in range(len(reader))
            if len(reader[i : i + 3]) == len(reader[i - 1 : i + 2])
        )
        print(increases)


if __name__ == "__main__":
    main()
