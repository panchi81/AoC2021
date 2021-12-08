#! 2021\venv\Scripts\python.exe

from pathlib import Path


def main():

    # f_path = Path("input\\4.txt")
    f_path = Path("input\\test.txt")

    if f_path.exists():
        try:
            with open(f_path, "r") as f_in:
                reader = f_in.read().splitlines()
        except FileExistsError:
            print("\nFile doesn't exist")
        except FileNotFoundError:
            print("\nFile not found")
        except:
            print("\nError")

        drawn = draw(reader)
        boards = board(reader)
        print(boards)


def draw(entry: list[str]) -> list[int]:
    return [int(i) for i in entry[0].split(",")]


def board(entry: list[str]):
    bla = []
    for row in entry[2:]:
        if row:
            bla.append([int(i) for i in row.split(",")])
    return bla

    # return [[int(i) for i in row.split(",")] for row in entry[2:] if row]
    # return [int(i) for row in entry[2:] for i in row.split(",") if row]


if __name__ == "__main__":
    main()
