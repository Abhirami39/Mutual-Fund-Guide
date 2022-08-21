from bs4 import BeautifulSoup
import requests
from random import randint
import datetime
import time

from mf_database import database_insertion
from mf_fetch_data import getting_mf_info, database_all_mf_info

url = "https://www.moneycontrol.com/mutual-funds/find-fund/"
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html5lib')


def getting_urls():
    links = []
    # test = soup.findAll(class_="robo_medium")
    i = int(0)
    for link in soup.findAll(class_="robo_medium"):
        # print(link)
        # print(link.get('href'))

        if i > 5:
            break

        # mf_info = call_functions()
        # print(mf_info)
        links.append(link.get('href'))
        i += 1

    print(links)
    return links


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    urls = []
    urls = getting_urls()

    all_mfs_info = []
    all_mfs_info = getting_mf_info(urls)
    print(all_mfs_info)

    # mf_info = []
    # mf_info = call_functions()
    # print(mf_info)

    database_insertion(all_mfs_info, database_all_mf_info)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
