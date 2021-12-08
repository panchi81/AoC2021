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

        print(reader)


if __name__ == "__main__":
    main()
