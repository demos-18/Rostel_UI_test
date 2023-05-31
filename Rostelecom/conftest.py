import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def chrome():
    driver = webdriver.Chrome(executable_path='\chromedriver.exe')
    yield driver
    driver.quit()

