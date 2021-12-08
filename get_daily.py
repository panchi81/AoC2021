#! venv\Scripts\python.exe

from datetime import date
import requests
from bs4 import BeautifulSoup as bs


def main():

    dom = date.today().strftime("%d")
    today = dom.lstrip("0")
    # url = f"https://adventofcode.com/2021/day/{today}/input"
    url = "https://adventofcode.com/2021/day/1/input"
    daily = requests.get(url)
    soup = bs(daily.text, "html.parser")

    print(soup)


if __name__ == "__main__":
    main()
