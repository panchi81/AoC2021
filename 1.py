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

    # reader = """
    # 199
    # 200
    # 208
    # 210
    # 200
    # 207
    # 240
    # 269
    # 260
    # 263
    # """

    # increases = (
    #     sum(
    #         j.strip() > reader.splitlines()[i - 1].strip()
    #         for i, j in enumerate(reader.splitlines())
    #     )
    #     - 1
    # )
    # print(increases)

    increases = sum(int(j) > int(reader[i - 1]) for i, j in enumerate(reader))
    print(increases)


if __name__ == "__main__":
    main()
