#! venv\Scripts\python.exe
from pathlib import Path


def main():
    f_path = Path("input\\3.txt")

    if f_path.exists():
        try:
            with open(f_path, "r") as f_in:
                reader = f_in.read().splitlines()
        except FileExistsError:
            print(f"File Error: {f_path}")

    rate = columns(reader)
    gamma, epsilon = gameps(rate)

    print(int(gamma, 2) * int(epsilon, 2))


def columns(entry: list[str]) -> list[str]:

    # columns = []
    # for idx in range(len(entry[0])):
    #     item = "".join(byte[idx] for byte in entry)
    #     columns.append(item)
    # return columns

    return ["".join(byte[idx] for byte in entry) for idx in range(len(entry[0]))]


def gameps(columns: list[str]) -> int:

    # s = ""
    # for byte in rate:
    #     if byte.count("1") > byte.count("0"):
    #         s += "1"
    #     else:
    #         s += "0"

    most = "".join(
        "1" if byte.count("1") > byte.count("0") else "0" for byte in columns
    )
    least = "".join("1" if i == "0" else "0" for i in most)

    return most, least


if __name__ == "__main__":
    main()
