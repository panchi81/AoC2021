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

        # print(reader[:20])

        # reader = [
        #     ["forward", "5"],
        #     ["down", "5"],
        #     ["forward", "8"],
        #     ["up", "3"],
        #     ["down", "8"],
        #     ["forward", "2"],
        # ]

        commands = {"forward": forward, "down": down, "up": up}

        horizontal = 0
        aim = 0
        depth = 0
        for item in reader:
            horizontal, aim, depth = commands[item[0]](item[1], horizontal, aim, depth)
            # print(f"{horizontal= }, {aim= }, {depth= }")

        print(horizontal * depth)


def forward(value: str, horizontal: int, aim: int, depth: int):
    # print("forward")
    return horizontal + int(value), aim, depth + (int(value) * aim)


def down(value: str, horizontal: int, aim: int, depth: int):
    # print("down")
    return horizontal, aim + int(value), depth


def up(value: str, horizontal: int, aim: int, depth: int):
    # print("up")
    return horizontal, aim - int(value), depth


if __name__ == "__main__":
    main()
