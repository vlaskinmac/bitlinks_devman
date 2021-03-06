import argparse
import logging
import os
from urllib.parse import urlparse

import requests
from dotenv import load_dotenv


def shorten_link(link, token):
    url = "https://api-ssl.bitly.com/v4/bitlinks"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }
    payload = {
        "long_url": link,
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
        "Content-Type": "application/json",
    }
    payload = {
        "unit": "day",
    }
    response = requests.get(url=url_link, params=payload, headers=headers)
    response.raise_for_status()
    logging.warning(response.status_code)
    return response.json()


def is_bitlink(token, link):
    url = "https://api-ssl.bitly.com/v4/bitlinks"

    parsed_link = urlparse(link)
    url_link = f"{url}/{parsed_link.netloc}{parsed_link.path}"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }
    response = requests.get(url=url_link, headers=headers)
    return response.ok


def gets_link_from_user():
    parser = argparse.ArgumentParser(
        description="Skript shorten links and sum clicks by shorten links"
    )
    parser.add_argument(
        "link", nargs="+",
        help="Input links or bitlinks"
    )
    args_link = parser.parse_args().link
    if args_link:
        return args_link


def main():
    links = gets_link_from_user()
    load_dotenv()
    token = os.getenv("BITLY_ACCESS_TOKEN")
    logging.basicConfig(
        level=logging.WARNING,
        filename="logs.log",
        filemode="w",
        format="%(asctime)s - [%(levelname)s] - %(message)s",
    )
    try:
        for link in links:
            if not is_bitlink(token=token, link=link):
                print(
                    "\n???? ?????????? ?????????????? ????????????!\nBitlink: ",
                    shorten_link(link=link, token=token, )
                )
            else:
                print(
                    "\n???? ?????????? Bitlink!\n?????????? ???????????? Bitlink:",
                    count_clicks_total(link=link, token=token, )["total_clicks"],
                    "\n",
                )
    except KeyError as exc:
        logging.warning(exc)


if __name__ == "__main__":
    main()
