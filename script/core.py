import requests
import json
import sys


class API:
    def __init__(self, url):
        self.url = url

        self.file = {}
        self.meta = self.req_to_json(self.get_page_url())["meta"]

    @staticmethod
    def req_to_json(url):
        r = requests.get(url)
        return r.json()

    def get_page_url(self, page=1, per_page=100):
        return self.url + f"?page={page}&per_page={per_page}"

    def save_data_to_json(self, filename="data"):
        all_pages = list()
        for page in range(1, self.meta["total_pages"]):
            page_url = self.get_page_url(page)
            r = self.req_to_json(page_url)["data"]
            all_pages.append(r)

        with open(f"{filename}.json", "w", encoding="utf-8") as f:
            json.dump(all_pages, f)

    def open_file(self, filename="data"):
        try:
            with open(f"{filename}.json", "r", encoding="utf-8") as f:
                self.file = json.load(f)
            return self.file
        except Exception as e:
            print(e)
            print("Load data to json file")
            sys.exit()

    def highest_attr_value(self, attr):
        highest_val = 0

        for page in self.open_file():
            for player in page:
                attr_value = player[attr]
                try:
                    if attr_value > highest_val:
                        highest_val = attr_value
                except TypeError:
                    continue
        return highest_val

    def check_feet_and_inches(self):
        file = self.open_file()
        highest_feet = self.highest_attr_value("height_feet")
        inches = 0

        result = dict()

        for line in file:
            for player in line:
                if player["height_feet"] == highest_feet:
                    tmp = player["height_inches"]
                    if tmp > inches:
                        inches = tmp
                        result[f"{player['first_name']} {player['last_name']}"] = \
                            highest_feet + round(tmp * float(0.083), 2)
        return result

    def player_info(self, attr, val):
        data = dict()

        for page in self.file:
            for player in page:
                if player[attr] == val:
                    data[f"{player['first_name']} {player['last_name']}"] = val
        return data
