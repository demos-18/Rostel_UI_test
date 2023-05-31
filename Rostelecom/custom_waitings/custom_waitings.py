from selenium.webdriver.common.by import By

class ElementHasCssClass(object):

    def __init__(self, locator, css_class):
        self.locator = locator
        self.css_class = css_class

    def __call__(self, driver):
        element = driver.find_element(*self.locator)
        if self.css_class in element.get_attribute("class"):
            return element
        else:
            return False

class ElemenHasChildren(object):

    def __init__(self, locator, sub_locator):
        self.locator = locator
        self.sub_locator = sub_locator

    def __call__(self, driver):
        prop = '#'+self.locator[1]+self.sub_locator
        lac = (By.CSS_SELECTOR, prop)
        element = driver.find_element(*lac)
        if element:
            return element

        else:
            False




