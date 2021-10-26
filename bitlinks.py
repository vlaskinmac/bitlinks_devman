import logging
import requests
from urllib.parse import urlparse
import os

from dotenv import load_dotenv


def shorten_link(link, token):
    url = "https://api-ssl.bitly.com/v4/bitlinks"
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


def count_clicks_total(link, token):
    url = "https://api-ssl.bitly.com/v4/bitlinks"
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


def is_bitlink(token, link):
    url = "https://api-ssl.bitly.com/v4/bitlinks"
    flag = False
    parsed_link = urlparse(link)
    url_link = f"{url}/{parsed_link.netloc}{parsed_link.path}"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    try:
        response = requests.get(url=url_link, headers=headers)
        if response.ok:
            flag = True
            return flag
    except:
        return flag


def printing(token, link):
    var_is_bitlink = is_bitlink(token=token, link=link)
    try:
        if not var_is_bitlink:
            print("\nВы ввели длинную ссылку!\nBitlink: ", shorten_link(link=link,
                                                                        token=token)
                  )
        else:
            print("\nВы ввели Bitlink!\nСумма кликов Bitlink:",
                  count_clicks_total(link=link, token=token)["total_clicks"], "\n")
    except KeyError as exc:
        logging.warning(exc)
        print('Ошибка в параметре: ', exc)


def main():
    load_dotenv()
    link = input("Введите полный адрес ссылки: ")
    token = os.getenv("BITLY_ACCESS_TOKEN")
    logging.basicConfig(
        level=logging.WARNING,
        filename="logs.log",
        filemode="w",
        format="%(asctime)s - [%(levelname)s] - %(message)s"
    )
    printing(token=token, link=link)


if __name__ == "__main__":
    main()
