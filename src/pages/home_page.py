from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.logo = (By.CSS_SELECTOR, 'header.main-header a.logo')
        self.contact_us_button = (By.CSS_SELECTOR, 'a.contact-us-modal-open')
        self.contact_form = (By.CSS_SELECTOR, 'div.modal-content.hubspot-form')
        self.contact_form_firstname_input = (By.CSS_SELECTOR, "input[name='firstname']")
        self.contact_form_email_input = (By.CSS_SELECTOR, "input[name='email']")
        self.contact_form_lastname_input = (By.CSS_SELECTOR, "input[name='email']")
        self.contact_form_company_input = (By.CSS_SELECTOR, "input[name='company']")
        self.contact_form_contact_type_select = (By.XPATH, "//select[@name='contact_type']/parent::div")
        self.contact_form_message_textarea = (By.CSS_SELECTOR, "textarea[name='message']")
        self.contact_form_submit_button = (By.CSS_SELECTOR, "input[type='submit']")

    def open(self, base_url):
        self.driver.get(base_url)

    def is_logo_visible(self):
        logo = self.driver.find_element(*self.logo)
        return logo.is_displayed()

    def click_contact_us_button(self):
        button = self.driver.find_element(*self.contact_us_button)
        button.click()

    def validate_contact_form_displayed(self):
        contact_form_visible = self.driver.find_element(*self.contact_form).is_displayed()
        name_input_visible = self.driver.find_element(*self.contact_form_firstname_input).is_displayed()
        email_input_visible = self.driver.find_element(*self.contact_form_email_input).is_displayed()
        submit_button_visible = self.driver.find_element(*self.contact_form_submit_button).is_displayed()
        return contact_form_visible and name_input_visible and email_input_visible and submit_button_visible
    
    def click_contact_form_submit_button(self):
        button = self.driver.find_element(*self.contact_form_submit_button)
        self.driver.execute_script("arguments[0].scrollIntoView();", button)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.contact_form_submit_button)
        )
        button.click()

    def validate_firstname_alert(self):
        return self._validate_element_alert(self.contact_form_firstname_input)

    def validate_email_alert(self):
        return self._validate_element_alert(self.contact_form_email_input)

    def validate_lastname_alert(self):
        return self._validate_element_alert(self.contact_form_lastname_input)

    def validate_company_alert(self):
        return self._validate_element_alert(self.contact_form_company_input)

    def validate_contact_type_alert(self):
        return self._validate_element_alert(self.contact_form_contact_type_select)

    def validate_message_alert(self):
        return self._validate_element_alert(self.contact_form_message_textarea)

    def _validate_element_alert(self, element):
        try:
            input_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(element)
            )

            parent = input_element.find_element(By.XPATH, "..")
            error_sibling = parent.find_element(
                By.XPATH, "following-sibling::ul[@class='no-list hs-error-msgs inputs-list'][@role='alert']"
            )
            
            return error_sibling is not None
        except Exception as e:
            return False
    
    def write_firstname(self, text):
        firstname_input = self.driver.find_element(*self.contact_form_firstname_input)
        firstname_input.clear()
        firstname_input.send_keys(text)

