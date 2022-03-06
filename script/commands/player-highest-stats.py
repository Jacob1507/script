import click
from script.core import API
import sys


players_url = "https://www.balldontlie.io/api/v1/players"

try:
    a = API(players_url)
except Exception as e:
    print(e)
    print("URL address might be invalid\n")
    sys.exit()


def feet_to_meters(value):
    return round(value * float(0.3048), 2)


def pounds_to_kilos(value):
    return round(value * float(0.4535924), 2)


def tallest_player():
    data = a.check_feet_and_inches()
    sorted_items = sorted(data.items(), key=lambda x: x[1], reverse=True)
    tallest = sorted_items[0]
    feet = 0
    for i in tallest:
        if type(i) is float:
            feet = i
    msg = f"Tallest player: {tallest[0]} {feet_to_meters(feet)} meters"
    return msg


def heaviest_player():
    highest_value = a.highest_attr_value("weight_pounds")
    result = a.player_info("weight_pounds", highest_value)

    first_item = next(iter(result.items()))
    msg = f"Heaviest player: {first_item[0]} {pounds_to_kilos(first_item[1])} kg"
    return msg


@click.command(help="All player data needs to be saved as json file")
def cli():
    try:
        click.echo(f"{tallest_player()}\n{heaviest_player()}")
    except Exception as e:
        print(e)
        print("Invalid data\n")
