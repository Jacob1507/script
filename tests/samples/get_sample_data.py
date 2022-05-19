import requests
import json

URL_PLAYERS = "https://www.balldontlie.io/api/v1/players"
URL_TEAMS = "https://www.balldontlie.io/api/v1/teams"
URL_GAMES = "https://www.balldontlie.io/api/v1/games"

# Settings
PAGE = 1
PER_PAGE = 100


PARAMS = [
    ("page", PAGE),
    ("per_page", PER_PAGE)
]


def get_request_to_json(url, params):
    return requests.get(url, params).json()


def players_data_to_json_file(data):
    with open("players_data.json", "w") as f:
        json.dump(data, f, indent=2)


def teams_data_to_json_file(data):
    with open("teams_data.json", "w") as f:
        json.dump(data, f, indent=2)


def games_data_to_json_file(data):
    with open("games_data.json", "w") as f:
        json.dump(data, f, indent=2)


def main():
    players_data_to_json_file(get_request_to_json(URL_PLAYERS, PARAMS))
    teams_data_to_json_file(get_request_to_json(URL_TEAMS, PARAMS))
    games_data_to_json_file(get_request_to_json(URL_GAMES, PARAMS))


if __name__ == "__main__":
    main()

