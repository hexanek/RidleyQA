from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from tests.selectors import EXPECTED_TITLE, URL, XPATH_ESTATE_BUTTON, APPLICANT_DATA_NAV_ID, FIRST_FORM_NAME_FIELD, \
    FIRST_FORM_COMMITMENTS_FIELD, FIRST_FORM_MONEY_FIELD, XPATH_NEXT_BUTTON, DEFENDANT_DATA_NAV_ID, \
    SECOND_FORM_DEFENDANT_NAME, SECOND_FORM_DEFENDANT_FAULT, SECOND_FORM_DEFENDANT_DROPDOWN, SUMMARY_NAV_ID, \
    XPATH_DOWNLOAD_BUTTON


def test_estate_treasury(browser):
    browser.get(URL)
    assert browser.title == EXPECTED_TITLE

    estate_button = browser.find_element(By.XPATH, XPATH_ESTATE_BUTTON)
    estate_button.click()
    applicant_data_nav = browser.find_element(By.ID, APPLICANT_DATA_NAV_ID).get_attribute('ng-reflect-active')
    assert applicant_data_nav == 'true'

    name_field = browser.find_element(By.ID, FIRST_FORM_NAME_FIELD)
    name_field.send_keys('test')

    commitments_field = browser.find_element(By.ID, FIRST_FORM_COMMITMENTS_FIELD)
    commitments_field.send_keys('test')

    money_field = browser.find_element(By.ID, FIRST_FORM_MONEY_FIELD)
    money_field.clear()
    money_field.send_keys('10000')

    next_button = browser.find_element(By.XPATH, XPATH_NEXT_BUTTON)
    next_button.click()

    defendant_data_nav = browser.find_element(By.ID, DEFENDANT_DATA_NAV_ID).get_attribute('ng-reflect-active')
    assert defendant_data_nav == 'true'

    browser.implicitly_wait(5)

    defendant_name = browser.find_element(By.ID, SECOND_FORM_DEFENDANT_NAME)
    defendant_name.send_keys('Testowy')

    defendant_fault = browser.find_element(By.ID, SECOND_FORM_DEFENDANT_FAULT)
    defendant_fault.send_keys('Tester')

    dropdown_menu_defendant = Select(browser.find_element(By.ID, SECOND_FORM_DEFENDANT_DROPDOWN))
    dropdown_menu_defendant.select_by_index(1)

    defendant_name.send_keys(Keys.RETURN)

    summary_nav = browser.find_element(By.ID, SUMMARY_NAV_ID).get_attribute('ng-reflect-active')
    assert summary_nav == 'true'

    download_button = browser.find_element(By.XPATH, XPATH_DOWNLOAD_BUTTON)
    download_button.click()



