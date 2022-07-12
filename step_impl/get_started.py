from sqlite3 import Time
import time
from getgauge.python import step
from step_impl.utils.driver import Driver

@step("Go to login form at <url>")
def go_to_login_form_at(arg1):
  Driver.driver.get(arg1)


@step("Enter username <arg1>")
def enter_username(arg1):
  Driver.driver.find_element_by_name('username').send_keys(arg1)
  time.sleep(10);

@step("Enter password <arg1>")
def enter_password(arg1):
  Driver.driver.find_element_by_name('password').send_keys(arg1)

@step("Click log in button")
def click_log_in_button():
  Driver.driver.find_element_by_css_selector('#login > button').click()
  Driver.driver.implicitly_wait(20)


@step("Verify that we see logged in message <arg1>")
def verify_that_we_see_logged_in_message(arg1):
    assert Driver.driver.find_element_by_xpath('/html/body/div[2]/div/div/h4').text == arg1
