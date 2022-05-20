import click
import requests
from ..core import Command


games_api_url = "https://www.balldontlie.io/api/v1/games/"
teams_api_url = "https://www.balldontlie.io/api/v1/teams/"


class TeamsStats(Command):
    def __init__(self, teams_url, games_url, season_year):
        self.teams_url = teams_url
        self.games_url = games_url
        self.season_year = season_year

        Command.__init__(self, data=self.collect_teams_stats())

    def collect_teams_stats(self):
        list_of_games = self.season_games()
        team_names = self.team_names()
        teams_stats = list()

        for team_index in range(len(team_names)):
            new_table = self.create_table(team_names[team_index])
            teams_stats.append(new_table)
            team_name = team_names[team_index]
            self.update_team_stats(teams_stats[team_index], team_name, list_of_games)
        return teams_stats

    @staticmethod
    def update_team_stats(table, team, list_of_games):
        for game_index in range(1, len(list_of_games)):
            game = list_of_games[game_index]
            home_team = game["home_team"]["full_name"]
            visitor_team = game["visitor_team"]["full_name"]
            home_team_score = game["home_team_score"]
            visitor_team_score = game["visitor_team_score"]

            if team == home_team:
                if home_team_score > visitor_team_score:
                    table["won_games_as_home_team"] += 1
                else:
                    table["lost_games_as_home_team"] += 1

            if team == visitor_team:
                if visitor_team_score > home_team_score:
                    table["won_games_as_visitor_team"] += 1
                else:
                    table["lost_games_as_visitor_team"] += 1

    def season_games(self):
        season_data = self.season_data()
        all_season_games = []
        for page in season_data:
            for game in page["data"]:
                all_season_games.append(game)
        return all_season_games

    def season_data(self):
        season_data = list()
        params = [
            ("seasons[]", self.season_year),
            ("per_page", 100),
            ["page", 1]
        ]
        r = requests.get(self.games_url, params=params)
        meta = r.json()["meta"]

        for page in range(1, meta["total_pages"]+1):
            params[2][1] = page
            r = requests.get(self.games_url, params=params)
            data = r.json()
            season_data.append(data)
        return season_data

    def team_names(self):
        lst = list()
        r = requests.get(self.teams_url)
        data = r.json()["data"]

        for line in data:
            lst.append(line["full_name"])
        return lst

    @staticmethod
    def create_table(team_name):
        table = {
            "team_name": team_name,
            "won_games_as_home_team": 0,
            "won_games_as_visitor_team": 0,
            "lost_games_as_home_team": 0,
            "lost_games_as_visitor_team": 0,
        }
        return table


@click.command()
@click.option("--season", prompt="", help="Shows team statistics in given season")
@click.option("--output", default="stdout", help="display or save output")
def cli(season, output):
    ts_data = TeamsStats(teams_api_url, games_api_url, season).collect_teams_stats()
    cmd  = Command(ts_data)

    if output == "stdout":
        cmd.stdout()

    if output == "json":
        cmd.data_to_json()

    if output == "csv":
        cmd.data_to_csv()

    if output == "sqlite":
        cmd.data_do_sqlite()
