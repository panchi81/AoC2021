#! venv\Scripts\python.exe
from pathlib import Path


def main():
    f_path = Path("input\\2.txt")

    if f_path.exists():
        try:
            with open(f_path, "r") as f_in:
                # reader = [com.split() for com in f_in.read().splitlines()]
                reader = [com.split() for com in f_in.readlines()]
        except FileExistsError:
            print(f"File Error: {f_path}")

        commands = {"forward": forward, "down": down, "up": up}

        horizontal = 0
        depth = 0
        for item in reader:
            horizontal, depth = commands[item[0]](item[1], horizontal, depth)

        print(horizontal * depth)


def forward(value: str, horizontal: int, depth: int):
    return horizontal + int(value), depth


def down(value: str, horizontal: int, depth: int):
    return horizontal, depth + int(value)


def up(value: str, horizontal: int, depth: int):
    return horizontal, depth - int(value)


if __name__ == "__main__":
    main()
