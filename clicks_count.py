import logging
import requests
from urllib.parse import urlparse
from config import token

# https://dvmn.org


class Bitlinks:

    def __init__(self):
        self.token = token
        self.url = "https://api-ssl.bitly.com/v4/bitlinks"
        self.units_days = 5

    def shorten_link(self, link):
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }
        payload = {
            "long_url": f"{link}"
        }
        response = requests.post(url=self.url, json=payload, headers=headers)
        response.raise_for_status()
        logging.warning(response.status_code)
        return response.json()['link']

    def count_clicks_per_date(self, link):
        parsed_link = urlparse(link)

        url_link = f"{self.url}/{parsed_link.netloc}{parsed_link.path}/clicks"
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }
        payload = {
            "unit": "day", "units": 5
        }
        response = requests.get(url=url_link, params=payload, headers=headers)
        response.raise_for_status()
        logging.warning(response.status_code)
        return response.json()

    def count_clicks_total(self, link):
        parsed_link = urlparse(link)
        url_link = f"{self.url}/{parsed_link.netloc}{parsed_link.path}/clicks/summary"
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }
        payload = {
            "unit": "day", "units": self.units_days
        }
        response = requests.get(url=url_link, params=payload, headers=headers)
        response.raise_for_status()
        logging.warning(response.status_code)
        return response.json()

    def check_link(self):
        try:
            try:
                link = input("Введите полный адрес ссылки: ")
                print("Битлинк: ", self.shorten_link(link))
            except:
                clicks_per_date = self.count_clicks_per_date(link)["link_clicks"]
                print("Сумма кликов:", self.count_clicks_total(link)["total_clicks"], "\n")
                print("Кликов по дням:")
                for i in range(0, self.units_days):
                    parse_date = clicks_per_date[i]["date"]
                    parse_date = str(parse_date).split("T")[0]
                    print(f'Кликов: {clicks_per_date[i]["clicks"]} - {parse_date}')
        except requests.exceptions.HTTPError as exc:
            logging.warning(exc)
            print(exc)


def main():
    logging.basicConfig(
        level=logging.WARNING,
        filename="logs.log",
        filemode="w",
        format="%(asctime)s - [%(levelname)s] - %(message)s"
    )
    bitlinks = Bitlinks()
    bitlinks.check_link()


if __name__ == "__main__":
    main()
