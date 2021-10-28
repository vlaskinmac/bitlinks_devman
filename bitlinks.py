import logging
import os

<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
import requests
>>>>>>> 1464ab60bc92b6e4914a0caf14c1c0c7b51928e3
>>>>>>> d6184a31916c0ee56507d53149e675e9e380c725
from dotenv import load_dotenv
from urllib.parse import urlparse


def shorten_link(link, token):
    url = "https://api-ssl.bitly.com/v4/bitlinks"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    payload = {
        "long_url": link
    }
    response = requests.post(url=url, json=payload, headers=headers)
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
>>>>>>> 08edcd4b9e6c51f241b88502283fc6dfe522131a


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
