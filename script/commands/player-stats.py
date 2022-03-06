import click
import requests

url = "https://www.balldontlie.io/api/v1/players"


@click.command()
@click.option("--name", prompt="", help="Search players by name")
def cli(name, output):
    url = f"https://www.balldontlie.io/api/v1/players?search={name}"
    r = requests.get(url)
    js = r.json()
    if name:
        result = list()
        for data in js["data"]:
            if data["first_name"].lower() == name.lower():
                print(f"{data}\n")
                result.append(data)
