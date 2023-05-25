# selenium-assist
Python package for easy writing of selenium scripts.

## install
```bash
pip install selenium-assist
```

## usage
```python
import time
import selenium_assist as sa
from selenium.webdriver.common.keys import Keys
import logging


# setup and silence loggers
logging.basicConfig(level=logging.DEBUG)
logging.getLogger("selenium.webdriver.remote.remote_connection").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)

# connect webdriver (use False for headless mode)
driver = sa.connect_webdriver(True)

# do stuff
sa.load_page("Loading initial webpage ...", "https://google.com/ncr", driver)
sa.wait_for_presence("Waiting for Accept all ...", '//*[@id="L2AGLb"]', driver, extra_timeout=1)
sa.click_element("Clicking Accept all ...", '//*[@id="L2AGLb"]', driver)
sa.wait_for_presence("Waiting for Google Search ...", '//*[@id="APjFqb"]', driver)
sa.click_element("Clicking search box ...", '//*[@id="APjFqb"]', driver)
sa.send_keys("Sending text ...", '//*[@id="APjFqb"]', "news" + Keys.ENTER, driver, skip_check=True)

# close webdriver
logging.debug("Done with webdriver, sleeping 3s and exiting ...")
time.sleep(3)
driver.close()
```
