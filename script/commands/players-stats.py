import click
from script.core import *

URL = f"https://www.balldontlie.io/api/v1/players"
PAGE = 1
PER_PAGE = 100


class PlayersStats:
    def __init__(self, data):
        self.data = data

    def tallest_player(self):
        tallest_player = {
            "first_name": "",
            "last_name": "",
            "height": 0,
        }
        for player in self.data:
            if player["height_feet"] is not None:
                total_height = player["height_feet"] + (player["height_inches"] / 10)
                if total_height >= tallest_player["height"]:
                    tallest_player["first_name"] = player["first_name"]
                    tallest_player["last_name"] = player["last_name"]
                    tallest_player["height"] = total_height

        return tallest_player

    def heaviest_player(self):
        heaviest_player = {
            "first_name": "",
            "last_name": "",
            "weight": 0,
        }

        for player in self.data:
            if player["weight_pounds"] is not None:
                if player["weight_pounds"] > heaviest_player["weight"]:
                    tmp = player["weight_pounds"]
                    heaviest_player["first_name"] = player["first_name"]
                    heaviest_player["last_name"] = player["last_name"]
                    heaviest_player["weight"] = tmp

        return heaviest_player


def feet_to_meters(feet_height):
    one_feet_to_meter = float(0.3048)
    return round(feet_height * one_feet_to_meter, 2)


def pounds_to_kilos(pounds_weight):
    one_pound_to_kilo = float(0.4535924)
    return round(pounds_weight * one_pound_to_kilo, 2)


@click.command(help="Display tallest and heaviest player")
@click.option("--name", prompt="")
def cli(name):
    params = [
        ["search", name],
        ["page", PAGE],
        ["per_page", PER_PAGE],
    ]

    initial_request = request_to_json(URL, params)
    total_pages = initial_request["meta"]["total_pages"]
    data = list()

    if total_pages > 1:
        for page in range(1, total_pages):
            params[1][1] = page
            req_new_page = request_to_json(URL, params)["data"]
            data.append(req_new_page)

    else:
        data = initial_request["data"]

    ps = PlayersStats(data)

    heaviest = ps.heaviest_player()
    tallest = ps.tallest_player()

    print(f"Heaviest player: {heaviest['first_name']} {heaviest['last_name']}"
          f" {pounds_to_kilos(heaviest['weight'])}")
    print(f"Tallest player: {tallest['first_name']} {tallest['last_name']}"
          f" {feet_to_meters(tallest['height'])}")
