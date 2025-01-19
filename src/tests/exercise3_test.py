from pages.home_page import HomePage
from config import BASE_URL

def test_homepage_contact_form(browser):
    # Step 1: Navigate to Qubika website and validate the page loaded correctly
    home_page = HomePage(browser)
    home_page.open(BASE_URL)
    assert browser.current_url == BASE_URL, f"Expected URL {BASE_URL}, but got {browser.current_url}"
    assert home_page.is_logo_visible(), "Qubika logo was not displayed correctly in home page"

    # Step 2: Click on contact us button and validate form displayed correctly
    home_page.click_contact_us_button()
    assert home_page.validate_contact_form_displayed(), "Contact form elements were not displayed as expected"

    # Step 3: Click get in touch button and validate error messages
    home_page.click_contact_form_submit_button()
    assert home_page.validate_firstname_alert(), "Error label for first name was not displayed"
    assert home_page.validate_email_alert(), "Error label for email was not displayed"
    assert home_page.validate_lastname_alert(), "Error label for last name was not displayed"
    assert home_page.validate_company_alert(), "Error label for company was not displayed"
    assert home_page.validate_contact_type_alert(), "Error label for contact type was not displayed"
    assert home_page.validate_message_alert(), "Error label for message was not displayed"

    # Step 4: Write text on name field and click get in touch button, validate fields
    home_page.write_firstname("test name")
    home_page.click_contact_form_submit_button()
    assert home_page.validate_firstname_alert() is False, "Error label for first name was displayed"
    assert home_page.validate_email_alert(), "Error label for email was not displayed"
    assert home_page.validate_lastname_alert(), "Error label for last name was not displayed"
    assert home_page.validate_company_alert(), "Error label for company was not displayed"
    assert home_page.validate_contact_type_alert(), "Error label for contact type was not displayed"
    assert home_page.validate_message_alert(), "Error label for message was not displayed"
