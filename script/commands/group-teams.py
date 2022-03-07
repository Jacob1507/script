import click
import requests


class GroupTeams:
    def __init__(self, json_data):
        self.divisions = {}
        self.json_data = json_data

    def get_divisions_dict(self):
        for team in self.json_data["data"]:
            division = team["division"]
            if division not in self.divisions.keys():
                self.divisions.update({division: []})

    def group_teams(self):
        for team in self.json_data["data"]:
            if team["division"] in self.divisions.keys():
                division = team["division"]
                team_name = team["full_name"]
                self.divisions[division].append(team_name)

    def stdout(self):
        for division, teams in self.divisions.items():
            print(division)
            for team in teams:
                print(f"\t{team}")


def main():
    url = "https://www.balldontlie.io/api/v1/teams"
    r = requests.get(url)
    api = r.json()
    gt = GroupTeams(api)
    gt.get_divisions_dict()
    gt.group_teams()
    gt.stdout()


@click.command()
def cli():
    main()
