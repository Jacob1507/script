import click
from script.core import API
import sys


# players_url = "https://www.balldontlie.io/api/v1/players"
#
# try:
#     a = API(players_url)
# except Exception as e:
#     print(e)
#     print("URL address might be invalid\n")
#     sys.exit()
#
# r = a.request_players_data()
# pages_data = a.combine_pages_data(r)
#
#
# def display_tallest():
#     tallest = tallest_player()
#     msg = f"Tallest player: {tallest[0]} {feet_to_meters(tallest[1])} meters"
#     return msg
#
#
# def display_heaviest():
#     highest_value = highest_attr_value("weight_pounds")
#     match_player = player_info("weight_pounds", highest_value)
#
#     first_item = next(iter(match_player.items()))
#     msg = f"Heaviest player: {first_item[0]} {pounds_to_kilos(first_item[1])} kg"
#     return msg
#
#
# def tallest_player():
#     inches = 0
#     first_name = ""
#     last_name = ""
#     height = 0
#
#     highest_value = highest_attr_value("height_feet")
#     for player in pages_data:
#         if player["height_feet"] == highest_value:
#             tmp_highest_inches = player["height_inches"]
#             if tmp_highest_inches > inches:
#                 inches = tmp_highest_inches
#                 first_name = player["first_name"]
#                 last_name = player["last_name"]
#             height = highest_value + round(inches * float(0.083), 2)
#     return [f"{first_name} {last_name}", height]
#
#
# def player_info(attr, val):
#     data = dict()
#
#     for player in pages_data:
#         if player[attr] == val:
#             data[f"{player['first_name']} {player['last_name']}"] = val
#     return data
#
#
# def highest_attr_value(attr):
#     highest_val = 0
#     players_data = pages_data
#
#     for player in players_data:
#         attr_value = player[attr]
#         try:
#             if attr_value > highest_val:
#                 highest_val = attr_value
#         except TypeError:
#             continue
#     return highest_val
#
#
# def feet_to_meters(value):
#     return round(value * float(0.3048), 2)
#
#
# def pounds_to_kilos(value):
#     return round(value * float(0.4535924), 2)


@click.command(help="Display tallest and heaviest player")
@click.option("--name", prompt="")
def cli(name):
    players_url = f"https://www.balldontlie.io/api/v1/players?search={name}"

    try:
        a = API(players_url)
    except Exception as e:
        print(e)
        print("Player not found")
        sys.exit()

    r = a.request_players_data()
    pages_data = a.combine_pages_data(r)

    def display_tallest():
        tallest = tallest_player()
        msg = f"Tallest player: {tallest[0]} {feet_to_meters(tallest[1])} meters"
        return msg

    def display_heaviest():
        highest_value = highest_attr_value("weight_pounds")
        match_player = player_info("weight_pounds", highest_value)

        first_item = next(iter(match_player.items()))
        msg = f"Heaviest player: {first_item[0]} {pounds_to_kilos(first_item[1])} kg"
        return msg

    def tallest_player():
        inches = 0
        first_name = ""
        last_name = ""
        height = 0

        highest_value = highest_attr_value("height_feet")
        for player in pages_data:
            if player["height_feet"] == highest_value:
                tmp_highest_inches = player["height_inches"]
                if tmp_highest_inches > inches:
                    inches = tmp_highest_inches
                    first_name = player["first_name"]
                    last_name = player["last_name"]
                height = highest_value + round(inches * float(0.083), 2)
        return [f"{first_name} {last_name}", height]

    def player_info(attr, val):
        data = dict()

        for player in pages_data:
            if player[attr] == val:
                data[f"{player['first_name']} {player['last_name']}"] = val
        return data

    def highest_attr_value(attr):
        highest_val = 0
        players_data = pages_data

        for player in players_data:
            attr_value = player[attr]
            try:
                if attr_value > highest_val:
                    highest_val = attr_value
            except TypeError:
                continue
        return highest_val

    def feet_to_meters(value):
        return round(value * float(0.3048), 2)

    def pounds_to_kilos(value):
        return round(value * float(0.4535924), 2)

    try:
        click.echo(f"{display_tallest()}\n{display_heaviest()}")
    except Exception as e:
        print(e)
        print("Players not found")
