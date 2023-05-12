# This is so that you can import selenium_helpers or import connect_webdriver from selenium_helpers
# instead of from selenium_helpers.managers import connect_webdriver

from .helpers import cleanup, save_screenshot, dump_and_exit
from .wrappers import selenium_load_page, selenium_wait_for_presence, selenium_wait_for_visibility, \
    selenium_click_element, selenium_send_keys, selenium_hoover_over_element, selenium_switch_to_iframe, \
    selenium_get_table_data
from .managers import connect_webdriver
