import logging
from selenium_helpers.helpers import dump_and_exit


def selenium_load_page(task, url, driver):
    logging.debug(task)
    try:
        driver.get(url)
    except Exception as e:
        dump_and_exit("Cannot load webpage, dumping source and exiting!", driver, exc=e)
    return
