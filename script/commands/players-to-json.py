import sys
import click
from script.core import API


url = "https://www.balldontlie.io/api/v1/players"


@click.command()
def cli():
    click.echo("It might take few moments..")

    try:

        api = API(url)
        api.save_data_to_json()
    except Exception as e:
        print(e)
        print("URL address might be invalid\n")
        sys.exit()
    click.echo("Done")
