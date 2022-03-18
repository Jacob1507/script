import requests
import json
import csv
import sqlite3


def request_to_json(url, params):
    r = requests.get(url, params)
    data = r.json()
    return data


class Command:
    def __init__(self, data: list):
        self.data = data

    def stdout(self):
        for item in self.data:
            print(f"""
{item["team_name"]}
\twon games as home team: {item["won_games_as_home_team"]}
\twon games as visitor team: {item["won_games_as_visitor_team"]}
\tlost games as home team: {item["lost_games_as_home_team"]}
\tlost games as visitor team: {item["lost_games_as_visitor_team"]}
        """)

    def data_to_json(self):
        with open("output.json", "w", encoding="utf-8") as f:
            json.dump(self.data, f, indent=2)

    def data_to_csv(self):
        header_info = ["team_name", "won_games_as_home_team", "won_games_as_visitor_team",
                       "lost_games_as_home_team", "lost_games_as_visitor_team"]

        with open("output.csv", "w") as f:
            writer = csv.DictWriter(f, fieldnames=header_info)
            writer.writeheader()
            writer.writerows(self.data)

    def data_do_sqlite(self):
        data = self.data
        conn = sqlite3.connect("output.db")
        db = conn.cursor()

        try:
            db.execute("""create table teams_stats (
                         team_name varchar(50),
                         won_games_as_home_team int,
                         won_games_as_visitor_team int,
                         lost_games_as_home_team int,
                         lost_games_as_visitor_team int
                       )""")
        except sqlite3.Error:
            """ ignores exception if table exists """
            pass

        for team in data:
            db.execute(f""" INSERT INTO teams_stats VALUES(?, ?, ?, ?, ?)""", (
                            team["team_name"],
                            team["won_games_as_home_team"],
                            team["won_games_as_visitor_team"],
                            team["lost_games_as_home_team"],
                            team["lost_games_as_visitor_team"]
                        ))

            conn.commit()
        conn.close()
