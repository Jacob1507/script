import click
import requests

url = "https://www.balldontlie.io/api/v1/players"


@click.command()
@click.option("--name", prompt="", help="Search players by name")
def cli(name):
    url = f"https://www.balldontlie.io/api/v1/players?search={name}"
    r = requests.get(url)
    js = r.json()
    for player in js["data"]:
        if player["first_name"].lower() == name.lower():
            print(f"{player}")
