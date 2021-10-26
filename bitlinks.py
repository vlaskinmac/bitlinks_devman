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


def is_bitlink(url, token, link):
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


def printing(url, token, link):
    var_is_bitlink = is_bitlink(url=url, token=token, link=link)
    try:
        if not var_is_bitlink:
            print("\nВы ввели длинную ссылку!\nBitlink: ", shorten_link(url=url,
                                                                        link=link,
                                                                        token=token)
                  )
        else:
            print("\nВы ввели Bitlink!\nСумма кликов Bitlink:",
                  count_clicks_total(url=url, link=link, token=token)["total_clicks"], "\n")
    except KeyError as exc:
        logging.warning(exc)
        print('Ошибка в параметре: ', exc)


def main():
    link = input("Введите полный адрес ссылки: ")
    token = os.getenv("BITLY_ACCESS_TOKEN")
    url = "https://api-ssl.bitly.com/v4/bitlinks"
    logging.basicConfig(
        level=logging.WARNING,
        filename="logs.log",
        filemode="w",
        format="%(asctime)s - [%(levelname)s] - %(message)s"
    )
    printing(url=url, token=token, link=link)


if __name__ == "__main__":
    main()
