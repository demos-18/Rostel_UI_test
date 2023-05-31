from page_objects.page_object import AuthorizationHelper
import pytest


@pytest.mark.checkelement
def test_left_section_on_page(chrome):
    """Проверяет наличие левого блока на странице."""
    main_page = AuthorizationHelper(chrome)
    main_page.go_to_site()

    assert main_page.check_left_section()


@pytest.mark.checkelement
def test_right_section_on_page(chrome):
    """Проверяет наличие правого блока на странице."""
    main_page = AuthorizationHelper(chrome)
    main_page.go_to_site()

    assert main_page.check_right_section()


@pytest.check.elementplace
def test_tab_bar_in_left_section(chrome):
    """"Проверяет наличие в левом блоке меню выбора типа аутентификации."""
    main_page = AuthorizationHelper(chrome)
    main_page.go_to_site()

    assert main_page.left_section_have_tab_bar()


@pytest.mark.checkelement
def test_phone_tab_on_page(chrome):
    """Проверяет наличие кнопки выбора аутентификации по телефону."""
    main_page = AuthorizationHelper(chrome)
    main_page.go_to_site()
    phone_tab = main_page.check_phone_tab()

    assert phone_tab.text == 'Телефон'


@pytest.mark.checkelement
def test_mail_tab_on_page(chrome):
    """Проверяет наличие кнопки выбора аутентификации по почте."""
    main_page = AuthorizationHelper(chrome)
    main_page.go_to_site()
    mail_tab = main_page.check_mail_tab()

    assert mail_tab.text == 'Почта'


@pytest.mark.checkelement
def test_login_tab_on_page(chrome):
    """Проверяет наличие кнопки выбора аутентификации по логину."""
    main_page = AuthorizationHelper(chrome)
    main_page.go_to_site()
    login_tab = main_page.check_login_tab()

    assert login_tab.text == 'Логин'


@pytest.mark.checkelement
def test_personal_account_tab_on_page(chrome):
    """Проверяет наличие кнопки выбора аутентификации по лицевому счёту."""
    main_page = AuthorizationHelper(chrome)
    main_page.go_to_site()
    personal_account_tab = main_page.check_personal_account_tab()

    assert personal_account_tab.text == 'Лицевой счёт'


@pytest.mark.checkelement
def test_password_field_on_page(chrome):
    """Проверяет наличие поля ввода пароля."""
    main_page = AuthorizationHelper(chrome)
    main_page.go_to_site()

    assert main_page.check_password_field()


@pytest.mark.checkelement
def test_username_field_on_page(chrome):
    """Проверяет наличие поля для ввода номера/почты/логина/лицевого счёта."""
    main_page = AuthorizationHelper(chrome)
    main_page.go_to_site()

    assert main_page.check_username_field()


@pytest.mark.elementstatus
def test_phone_tab_is_active_by_default(chrome):
    """Проверяет активность типа аутентификаци по телефону по умолчанию."""
    main_page = AuthorizationHelper(chrome)
    main_page.go_to_site()

    assert main_page.phone_tab_check_active_status()


@pytest.mark.elementstatus
def test_mail_tab_is_active_by_click(chrome):
    """Проверяет то, что таб выбора типа аутенфикации по почте активировался после нажатия."""
    main_page = AuthorizationHelper(chrome)
    main_page.go_to_site()
    main_page.check_mail_tab().click()

    assert main_page.mail_tab_check_active_status()


@pytest.mark.elementstatus
def test_login_tab_is_active_by_click(chrome):
    """Проверяет то, что таб выбора типа аутенфикации по логину активировался после нажатия."""
    main_page = AuthorizationHelper(chrome)
    main_page.go_to_site()
    main_page.check_login_tab().click()

    assert main_page.login_tab_check_active_status()


@pytest.mark.elementstatus
def test_personal_account_tab_is_active_by_click(chrome):
    """Проверяет то, что таб выбора типа аутенфикации по лицевому счёту активировался после нажатия."""
    main_page = AuthorizationHelper(chrome)
    main_page.go_to_site()
    main_page.check_personal_account_tab().click()

    assert main_page.personal_account_tab_active_check()


@pytest.mark.elementstatus
def test_input_phone_activate_phone_tab(chrome):
    """Проверяет то, что таб выбора типа аутенфикации по телефону активировался после ввода номера телефона."""
    main_page = AuthorizationHelper(chrome)
    main_page.go_to_site()
    main_page.check_mail_tab().click()
    main_page.check_username_field().clear()
    main_page.check_username_field().send_keys('+79225169845')
    main_page.check_password_field().click()

    assert main_page.phone_tab_check_active_status()


@pytest.mark.elementstatus
def test_input_mail_activate_mail_tab(chrome):
    """Проверяет то, что таб выбора типа аутенфикации по почте активировался после ввода электронной почты."""
    main_page = AuthorizationHelper(chrome)
    main_page.go_to_site()
    main_page.check_username_field().clear()
    main_page.check_username_field().send_keys('ivam.dam452@gmail.com')
    main_page.check_password_field().click()

    assert main_page.mail_tab_check_active_status()


@pytest.mark.elementstatus
def test_input_login_activate_login_tab(chrome):
    """Проверяет то что таб выбора типа аутенфикации по логину активировался после ввода логина."""
    main_page = AuthorizationHelper(chrome)
    main_page.go_to_site()
    main_page.check_username_field().clear()
    main_page.check_username_field().send_keys('demos_18')
    main_page.check_password_field().click()

    assert main_page.login_tab_check_active_status()


@pytest.mark.elementstatus
def test_input_personal_account_activate_tab_personal_account(chrome):
    """Проверяет то что таб выбора типа аутенфикации по номеру лицевого счёта активировался
    после ввода номера лицевого счёта."""
    main_page = AuthorizationHelper(chrome)
    main_page.go_to_site()
    main_page.check_username_field().clear()
    main_page.check_username_field().send_keys('987654321987')
    main_page.check_password_field().click()

    assert main_page.personal_account_tab_active_check()


@pytest.mark.checkelement
def test_title(chrome):
    """Проверяет, что название личного кабинета равно 'Ростелеком ID'"""
    main_page = AuthorizationHelper(chrome)
    main_page.go_to_site()
    title = main_page.check_title()
    assert title is True


@pytest.mark.elementplace
def test_slogan_on_right_section(chrome):
    """Проверяет наличие слогана в правом блоке."""
    main_page = AuthorizationHelper(chrome)
    main_page.go_to_site()
    slogan_text = main_page.slogan_text_in_right_section().text

    assert slogan_text == 'Персональный помощник в цифровом мире Ростелекома'


@pytest.mark.checkelement
def test_login_button_on_page(chrome):
    """Проверяет наличие кнопки входа на странице."""
    main_page = AuthorizationHelper(chrome)
    main_page.go_to_site()
    login_button = main_page.check_login_button()

    assert login_button.text == 'Войти'


@pytest.mark.destruction
@pytest.mark.parametrize('data', ['круцио', '不要放在心上', '№;%::*%;_', '123456789123456789', '789456', '+79225169977', ''])
def test_username_field_personal_account(chrome, data):
    """"Проверяет возможность ввода в поле для ввода лицевого счёта некорректных данных."""
    main_page = AuthorizationHelper(chrome)
    main_page.go_to_site()
    main_page.check_personal_account_tab().click()
    main_page.check_username_field().clear()
    main_page.check_username_field().send_keys(data)
    main_page.check_password_field().click()
    error_message = main_page.check_username_error_message()

    assert error_message.text == 'Проверьте, пожалуйста, номер лицевого счета'


@pytest.mark.checkelement
def test_remember_me_button_on_page(chrome):
    """Проверяет наличие кнопки 'Запомнить меня' на странице."""
    main_page = AuthorizationHelper(chrome)
    main_page.go_to_site()
    remember_me_button = main_page.check_remember_me_button()

    assert remember_me_button.text == 'Запомнить меня'


@pytest.mark.elementstatus
def test_remember_me_button_active_by_default(chrome):
    """Проверяет что кнопка 'Запомнить меня' активна по умолчанию."""
    main_page = AuthorizationHelper(chrome)
    main_page.go_to_site()

    assert main_page.remember_me_button_is_active_by_default()


@pytest.mark.checkelement
def test_forget_password_on_page(chrome):
    """Проверяет наличие на странице кнопки 'Забыл пароль'."""
    main_page = AuthorizationHelper(chrome)
    main_page.go_to_site()
    forget_password = main_page.check_forget_password_button()

    assert forget_password.text == 'Забыл пароль'


@pytest.mark.checkelement
def test_register_button_on_page(chrome):
    """Проверяет наличие на странице кнопки 'Зарегистрироваться'."""
    main_page = AuthorizationHelper(chrome)
    main_page.go_to_site()
    register_button = main_page.check_register_button()

    assert register_button.text == 'Зарегистрироваться'


@pytest.mark.checkelement
def test_vk_log_button_on_page(chrome):
    """Проверяет наличие на странице кнопки входа через ВКонтакте."""
    main_page = AuthorizationHelper(chrome)
    main_page.go_to_site()

    assert main_page.check_vk_button()


@pytest.mark.checkelement
def test_ok_log_button_on_page(chrome):
    """Проверяет наличие на странице кнопки входа через Однокласники.ru"""
    main_page = AuthorizationHelper(chrome)
    main_page.go_to_site()

    assert main_page.check_ok_button()


@pytest.mark.checkelement
def test_mail_ru_log_button_on_page(chrome):
    """Проверяет наличие на странице кнопки входа через Mail.ru"""
    main_page = AuthorizationHelper(chrome)
    main_page.go_to_site()

    assert main_page.check_mail_ru_button()


@pytest.mark.checkelement
def test_yandex_log_button(chrome):
    """Проверяет наличие на странице кнопки входа через Яндекс."""
    main_page = AuthorizationHelper(chrome)
    main_page.go_to_site()

    assert main_page.check_yandex_button()


@pytest.mark.checkelement
def test_footer_on_page(chrome):
    """Проверяет наличие на странице футера."""
    main_page = AuthorizationHelper(chrome)
    main_page.go_to_site()

    assert main_page.check_footer_on_page()


@pytest.mark.elementplace
def test_support_phone_in_footer(chrome):
    """Проверяет наличие номера службы поддержки в футере страницы."""
    main_page = AuthorizationHelper(chrome)
    main_page.go_to_site()
    support_phone = main_page.check_support_phone_in_footer()

    assert support_phone.text == '8 800 100 0 800'









