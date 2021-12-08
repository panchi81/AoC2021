#! venv\Scripts\python.exe

from datetime import date
from pathlib import Path


def main():

    dom = date.today().strftime("%d")
    today = dom.lstrip("0")
    # f_path = Path(f"input\\{today}.txt")
    f_path = Path("input\\1.txt")

    with open(f_path, "r") as f_input:
        reader = f_input.readlines()

    for i in range(0, len(reader), 3):
        print(reader[i])

    # increases = sum(int(j) > int(reader[i - 1]) for i, j in enumerate(reader))
    # print(increases)


if __name__ == "__main__":
    main()
