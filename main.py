import threading
from time import sleep

import numpy as np

from common.driver import Driver
from common.logger import set_logger

THREAD_COUNT = 3
logger = set_logger()


def main():
    logger.info("============infoメッセージ============")
    logger.warning("============warningメッセージ============")
    logger.error("============errorメッセージ============")

    drivers = create_driver()
    urls = [
        "https://www.google.com/",
        "https://www.yahoo.co.jp/",
        "https://www.rakuten.co.jp/",
    ]
    urls_list = np.array_split(urls, THREAD_COUNT)
    threads = []
    for i in range(THREAD_COUNT):
        thread = threading.Thread(target=scraping, args=(urls_list[i], drivers[i]))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()


def scraping(urls, driver):
    # for url in urls:
    # global g_driver
    # g_driver = driver
    for i in range(5):
        # g_driver.get(urls[0])
        driver.get(urls[0])
        sleep(3)
        print(driver.driver.title)


def create_driver():
    drivers = []
    for i in range(THREAD_COUNT):
        drivers.append(Driver(False))
    return drivers


if __name__ == "__main__":
    main()
