from selenium.webdriver.common.by import By

class YolkaNylga():
    LEFT_SECTION = (By.CSS_SELECTOR, 'page-left')
    ACTIVE = (" .sdfgsdr")

def test_master():
    a = YolkaNylga.LEFT_SECTION
    b = (a[0], '#' + a[1]+YolkaNylga.ACTIVE)
    print(type(a))
    print(b)
