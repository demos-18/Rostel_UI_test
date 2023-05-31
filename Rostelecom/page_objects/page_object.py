from base_pages.base_page import BasePage
from base_pages.base_page import ElementHasCssClass
from selenium.webdriver.common.by import By


class AuthorizationPageLocators:
    """There is a list of locators. NAME = (By.type_of_locator, 'locator')."""

    LEFT_SECTION = (By.ID, 'page-left')
    RIGHT_SECTION = (By.ID, 'page-right')
    PHONE_TAB = (By.ID, 't-btn-tab-phone')
    MAIL_TAB = (By.ID, 't-btn-tab-mail')
    LOGIN_TAB = (By.ID, 't-btn-tab-login')
    PERSONAL_ACCOUNT_TAB = (By.ID, 't-btn-tab-ls')
    LOGIN_BUTTON = (By.ID, 'kc-login')
    TAB_BAR = (By.CSS_SELECTOR, '.rt-tabs.rt-tabs--orange.rt-tabs--small.tabs-input-container__tabs')
    AUTHORIZATION_FORM = (By.CSS_SELECTOR, '.card-container__wrapper')
    USERNAME_FIELD = (By.ID, "username")
    PASSWORD_FIELD = (By.ID, "password")
    TITLE = (By.TAG_NAME, "title")
    SLOGAN_HEADER = (By.CSS_SELECTOR, "what-is__title")
    SLOGAN_TEXT = (By.CSS_SELECTOR, "what-is__desc")
    USERNAME_ERROR = (By.CSS_SELECTOR, ".rt-input-container__meta.rt-input-container__meta--error")
    REMEMBER_ME_BUTTON = (By.CSS_SELECTOR, ".rt-checkbox")
    FORGET_PASSWORD = (By.ID, "forgot_password")
    REGISTER_BUTTON = (By.ID, "kc-register")
    VK_SING_UP_BUTTON = (By.CSS_SELECTOR, ".rt-base-icon[alt='ВКонтакте']")
    OK_SING_UP_BUTTON = (By.CSS_SELECTOR, ".rt-base-icon[alt='Одноклассники.ru']")
    MAILRU_SING_UP_BUTTON = (By.CSS_SELECTOR, ".rt-base-icon[alt='Mail.ru']")
    YANDEX_SING_UP_BUTTON = (By.CSS_SELECTOR, ".rt-base-icon[alt='Yandex.ru']")
    FOOTER = (By.ID, "app-footer")
    SUPPORT_PHONE = (By.CSS_SELECTOR, "rt-footer-right__support-phone")


class ExpectedAttributes:
    """There is a list of expected attributes. ATTRIBUTE_NAME = 'attribute value'"""

    CSS_ACTIVE_TAB = 'rt-tab--active'
    TAB_BAR = ' .rt-tabs.rt-tabs--orange.rt-tabs--small.tabs-input-container__tabs'
    TITLE = "Ростелеком ID"
    SLOGAN_HEADER = " .what-is__title"
    SLOGAN_TEXT = " .what-is__desc"
    REMEMBER_ME_ACTIVE = "rt-checkbox--checked"
    SUPPORT_PHONE = " .rt-footer-right__support-phone"


class AuthorizationHelper(BasePage):

    """There are methods for interacting with page."""

    def check_left_section(self):

        left_section = self.find_element(AuthorizationPageLocators.LEFT_SECTION,  time=10)
        return left_section

    def check_right_section(self):

        right_section = self.find_element(AuthorizationPageLocators.RIGHT_SECTION, time=10)
        return right_section

    def check_phone_tab(self):

        phone_tab = self.find_element(AuthorizationPageLocators.PHONE_TAB, time=10)
        return phone_tab

    def check_mail_tab(self):

        mail_tab = self.find_element(AuthorizationPageLocators.MAIL_TAB, time=10)
        return mail_tab

    def check_login_tab(self):

        login_tab = self.find_element(AuthorizationPageLocators.LOGIN_TAB, time=10)
        return login_tab

    def check_personal_account_tab(self):

        personal_account = self.find_element(AuthorizationPageLocators.PERSONAL_ACCOUNT_TAB, time=10)
        return personal_account

    def check_authorization_block(self):

        authorization_block = self.find_element(AuthorizationPageLocators.AUTHORIZATION_FORM, time=10)
        return authorization_block

    def check_login_button(self):

        login_button = self.find_element(AuthorizationPageLocators.LOGIN_BUTTON, time=10)
        return login_button

    def check_left_section(self):

        left_section = self.find_element(AuthorizationPageLocators.LEFT_SECTION, time=10)
        return left_section

    def check_right_section(self):

        right_section = self.find_element(AuthorizationPageLocators.RIGHT_SECTION, time=10)
        return right_section

    def left_section_have_tab_bar(self):

        check = self.wait_children(AuthorizationPageLocators.LEFT_SECTION, ExpectedAttributes.TAB_BAR, time=10)
        return check

    def phone_tab_check_active_status(self):

        phone_button = self.wait_css_class(AuthorizationPageLocators.PHONE_TAB, ExpectedAttributes.CSS_ACTIVE_TAB, time=10)
        return phone_button

    def check_username_field(self):

        username_field = self.find_element(AuthorizationPageLocators.USERNAME_FIELD, time=10)
        return username_field

    def check_password_field(self):

        password_field = self.find_element(AuthorizationPageLocators.PASSWORD_FIELD, time=10)
        return password_field

    def mail_tab_check_active_status(self):

        mail_tab = self.wait_css_class(AuthorizationPageLocators.MAIL_TAB, ExpectedAttributes.CSS_ACTIVE_TAB, time=10)
        return mail_tab

    def login_tab_check_active_status(self):

        login_tab = self.wait_css_class(AuthorizationPageLocators.LOGIN_TAB, ExpectedAttributes.CSS_ACTIVE_TAB, time=10)
        return login_tab

    def personal_account_tab_active_check(self):

        personal_account_tab = self.wait_css_class(AuthorizationPageLocators.PERSONAL_ACCOUNT_TAB,
                                                   ExpectedAttributes.CSS_ACTIVE_TAB, time=10)
        return personal_account_tab

    def check_title(self):
        title = self.find_title(text=ExpectedAttributes.TITLE, time=10)
        return title

    def slogan_text_in_right_section(self):
        slogan_text = self.wait_children(AuthorizationPageLocators.RIGHT_SECTION, ExpectedAttributes.SLOGAN_TEXT,
                                         time=10)
        return slogan_text

    def check_login_button(self):
        login_button = self.find_element(AuthorizationPageLocators.LOGIN_BUTTON, time=10)

        return login_button

    def check_username_error_message(self):
        error_message = self.find_element(AuthorizationPageLocators.USERNAME_ERROR, time=10)

        return error_message

    def check_remember_me_button(self):
        remember_me_button = self.find_element(AuthorizationPageLocators.REMEMBER_ME_BUTTON, time=10)

        return remember_me_button

    def remember_me_button_is_active_by_default(self):
        active_remember_me_button = self.wait_css_class(AuthorizationPageLocators.REMEMBER_ME_BUTTON,
                                                        ExpectedAttributes.REMEMBER_ME_ACTIVE, time=10)

        return active_remember_me_button

    def check_forget_password_button(self):
        forget_password_button = self.find_element(AuthorizationPageLocators.FORGET_PASSWORD, time=10)

        return forget_password_button

    def check_register_button(self):
        register_button = self.find_element(AuthorizationPageLocators.REGISTER_BUTTON, time=10)

        return register_button

    def check_vk_button(self):
        vk_button = self.find_element(AuthorizationPageLocators.VK_SING_UP_BUTTON, time=10)

        return vk_button

    def check_ok_button(self):
        ok_button = self.find_element(AuthorizationPageLocators.OK_SING_UP_BUTTON, time=10)

        return ok_button

    def check_mail_ru_button(self):
        mail_ru_button = self.find_element(AuthorizationPageLocators.MAILRU_SING_UP_BUTTON, time=10)

        return mail_ru_button

    def check_yandex_button(self):
        yandex_button = self.find_element(AuthorizationPageLocators.YANDEX_SING_UP_BUTTON, time=10)

        return yandex_button

    def check_footer_on_page(self):
        footer = self.find_element(AuthorizationPageLocators.FOOTER, time=10)

        return footer

    def check_support_phone_in_footer(self):
        support_phone = self.wait_children(AuthorizationPageLocators.FOOTER, ExpectedAttributes.SUPPORT_PHONE, time=10)

        return support_phone



