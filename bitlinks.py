import logging
import requests
from urllib.parse import urlparse
import os

from dotenv import load_dotenv

load_dotenv()


# Link example
# https://dvmn.org


class Bitlinks:

    def __init__(self):
        self.token = os.getenv("API_KEY")
        self.url = "https://api-ssl.bitly.com/v4/bitlinks"

    def shorten_link(self, link):
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }
        payload = {
            "long_url": f"{link}"
        }
        response = requests.post(url=self.url, json=payload, headers=headers)
        logging.warning(response.status_code)
        return response.json()["link"]

    def count_clicks_total(self, link):
        parsed_link = urlparse(link)
        url_link = f"{self.url}/{parsed_link.netloc}{parsed_link.path}/clicks/summary"
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }
        payload = {
            "unit": "day"
        }
        response = requests.get(url=url_link, params=payload, headers=headers)
        logging.warning(response.status_code)
        return response.json()

    def check_link(self):
        try:
            try:
                link = input("Введите полный адрес ссылки: ")
                print("Вы ввели длинную ссылку! \n Bitlink: ", self.shorten_link(link))
            except:
                print("Вы ввели Bitlink! \n")
                print("Сумма кликов Bitlink:", self.count_clicks_total(link)["total_clicks"], "\n")
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
