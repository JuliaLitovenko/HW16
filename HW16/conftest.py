import subprocess
import pytest
import time
import os
from selenium import webdriver
subprocess.run("docker rm -f selenium_chrome", shell=True, check=True)

port = 4444


@pytest.fixture(scope="module", autouse=True)
def docker():
    os.system(f"docker run -d --name selenium_chrome -p {port}:4444 selenium/standalone-chrome-debug")
    time.sleep(5)
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--headless')
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--disable-dev-shm-usage")
    pytest.driver = webdriver.Remote(
        command_executor=f'http://localhost:{port}/wd/hub',
        options=options
        )

    # Post-conditions
    yield
    os.system("docker rm -f selenium_chrome")






