from configs.urls import Urls
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service
import shutil
import pytest
from datetime import datetime
import random
import string


@pytest.fixture()
def driver():
    options = ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    chromedriver_path = shutil.which("chromedriver") or "/usr/local/bin/chromedriver"
    service = Service(chromedriver_path)
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(Urls.BASE_PAGE_URL)
    yield driver
    driver.quit()


def _random_suffix(length: int = 6) -> str:
    ts = datetime.utcnow().strftime("%Y%m%d%H%M%S")
    rand = "".join(random.choices(string.ascii_lowercase + string.digits, k=length))
    return f"{ts}{rand}"


@pytest.fixture()
def user():
    return {
        'firstname': 'Ник',
        'surname': 'Ли',
        'username': ''.join(random.choices(string.ascii_lowercase + string.digits, k=8)),
        'email': ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))+'@example.com',
        'psw': 'S3cur3P@ssw0rd',
    }
