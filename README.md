# qubika-site-pytest-py
Exercise 3 - Qubika main site e2e tests with pytest and python

This solution contains an automated test that navigates to Qubika main site, opens the contact form and validates the required inputs functionality.

## Installation
Please make sure you have the following requirements.
- Git
- Python
- pip

Clone the project
```sh
git clone https://github.com/luis-zambra/qubika-site-pytest-py.git
```
Navigate to root folder
```sh
cd qubika-site-pytest-py
```
Create a python virtual environment
```sh
python -m venv venv
```
Activate the virtual environment
- On Windows
```sh
venv\Scripts\activate
```
- On macOS and Linux
```sh
source venv/bin/activate
```
Once inside the virtual environment we will be able to install the requirements with the following command
```sh
pip install -r requirements.txt
```
This will install pytest, selenium and webdriver-manager which will handle the chromedriver instance. You can check which dependencies were installed with the following command
```sh
pip list
```

## Running the tests
Once all the dependencies are installed the framework is ready to use, run the following command to execute the tests
```sh
pytest -v src/tests
```
This will create an instance of Google Chrome that will run the test, the result will show as following.
<img width="1086" alt="Image" src="https://github.com/user-attachments/assets/f9b9a99e-bd65-406c-8d68-8bab5a315fba" />

## Solution explanation and enhancements

The framework relies on the page object pattern to define the pages that will be tests, assigning the responsibility of defining and handling the web component elements to the page, respecting the SOLID principles.

Some improvements that can be made to enhance the solution:
- The selector strategy for searching for elements relies heavily in robustness with what is available in the DOM. The ideal option for each selector would be having custom test tags only to be used for test automation, as ids may change dynamically and other types of selectors are not as reliable.

- As per what was required in the exercise, the expected behavior of the first name field was to be marked in red when submitting without filling it. The same behavior is expected for the email field. However this was not noticed when running the tests as said fields behaved as the other required fields, thus this behavior was not covered.
