import requests


class API:
    def __init__(self, url):
        self.url = url

    def get_page_url(self, page=1, per_page=100):
        return self.url + f"?page={page}&per_page={per_page}"

    def request_players_data(self):
        players_data = list()
        params = [
            ("per_page", 100),
            ["page", 1]
        ]
        r = requests.get(self.url, params=params)
        meta = r.json()["meta"]
        for page in range(1, meta["total_pages"]+1):
            params[1][1] = page
            r = requests.get(self.url, params=params)
            data = r.json()["data"]
            players_data.append(data)
        return players_data

    @staticmethod
    def combine_pages_data(data):
        all_pages_data = []

        for page in data:
            for items in page:
                all_pages_data.append(items)

        return all_pages_data
