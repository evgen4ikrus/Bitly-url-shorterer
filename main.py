import os
import argparse
from urllib.parse import urlparse

import requests
from dotenv import load_dotenv

load_dotenv()


def get_link():
    parser = argparse.ArgumentParser(
        description='Передайте ссылку'
    )
    parser.add_argument('link', help='Ссылка')
    args = parser.parse_args()
    return args.link


def shorten_link(token, link):
    url = 'https://api-ssl.bitly.com/v4/shorten'
    headers = {
        "Authorization": f"Bearer {token}",
    }
    payload = {
        'long_url': link,
    }
    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()
    shortened_link = response.json()['link']
    return shortened_link


def count_clicks(token, link):
    headers = {
        "Authorization": f"Bearer {token}",
    }
    parsed_link = urlparse(link)
    bitlink = parsed_link.netloc + parsed_link.path
    url = f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary'
    payload = {
        'units': '-1',
    }
    response = requests.get(url, headers=headers, params=payload)
    response.raise_for_status()
    clicks_count = response.json()['total_clicks']
    return clicks_count


def is_bitlink(token, link):
    headers = {
        "Authorization": f"Bearer {token}",
    }
    parsed_url = urlparse(link)
    netloc, path = parsed_url.netloc, parsed_url.path
    url = f'https://api-ssl.bitly.com/v4/bitlinks/{netloc}{path}'
    response = requests.get(url, headers=headers)
    return response.ok


def main():
    token = os.environ["BITLY_TOKEN"]
    user_input_url = get_link()
    try:
        if is_bitlink(token, user_input_url):
            print("По вашей ссылке прошли:",
                  count_clicks(token, user_input_url),
                  "раз(а)")
        else:
            print('Битлинк', shorten_link(token, user_input_url))
    except requests.exceptions.HTTPError:
        exit('Ошибка: "Вы ввели несуществующую ссылку"')


if __name__ == '__main__':
    main()
