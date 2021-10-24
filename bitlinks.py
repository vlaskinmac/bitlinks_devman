import logging
import requests
from urllib.parse import urlparse
import os
from dotenv import load_dotenv

load_dotenv()


def shorten_link(url, link, token):
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    payload = {
        "long_url": f"{link}"
    }
    response = requests.post(url=url, json=payload, headers=headers)
    response.raise_for_status()
    logging.warning(response.status_code)
    return response.json()["link"]


def count_clicks_total(url, link, token):
    parsed_link = urlparse(link)
    url_link = f"{url}/{parsed_link.netloc}{parsed_link.path}/clicks/summary"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    payload = {
        "unit": "day"
    }
    response = requests.get(url=url_link, params=payload, headers=headers)
    logging.warning(response.status_code)
    return response.json()


def check_link(url, token):
    try:
        try:
            link = input("Введите полный адрес ссылки: ")
            print("\nВы ввели длинную ссылку!\nBitlink: ", shorten_link(url=url,
                                                                        link=link,
                                                                        token=token)
                  )
        except:

            print("\nВы ввели Bitlink!\nСумма кликов Bitlink:",
                  count_clicks_total(url=url, link=link, token=token)["total_clicks"], "\n")
    except requests.exceptions.HTTPError as exc:
        logging.warning(exc)
        print(exc)


def main():
    token = os.getenv("BITLY_ACCESS_TOKEN")
    url = "https://api-ssl.bitly.com/v4/bitlinks"
    logging.basicConfig(
        level=logging.WARNING,
        filename="logs.log",
        filemode="w",
        format="%(asctime)s - [%(levelname)s] - %(message)s"
    )
    check_link(url=url, token=token)


if __name__ == "__main__":
    main()
