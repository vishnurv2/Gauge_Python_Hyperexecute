# Getting Started with Selenium Gauge and Python

This is an example for getting started with Gauge, Selenium, and LambdaTest's selenium grid.

<br>

## Install Gauge

For this example, we used brew to install Gauge on macOS:

`brew install gauge`

<br>

## Download Template Gauge Project

In this example, we started with a project template provided by Gauge:

`gauge init python_selenium`

You can also clone this repository to use this template.

These are the changes we made to the gauge python_selenium template:

<br>

## Change driver.py to point to LT Hub

In step_impl -> utils, you will find a driver.py file. In order to connect to Lambdatest, you will need to point to our hub.

This is also where you should enter your LT credentials along with the capabilities for the device/browser configuration you want to test.

You can generate the desired capabilities for your test using our capabilities generator: https://www.lambdatest.com/capabilities-generator/

```
from getgauge.python import before_suite, after_suite
from selenium import webdriver

class Driver(object):
    driver = None

    @before_suite
    def init(self):
        self.username = "LT_USERNAME" #replace with your LT username
        self.authkey  = "LT_ACCESS_KEY" #replace with your LT access key

        caps = {}

        caps['name'] = 'Gauge Sample'
        caps['build'] = 'Python_Gauge_LambdaTest'
        caps['browserName'] = 'Chrome'
        caps['version'] = 'latest'
        caps['platform'] = 'Windows 10'


        # start the remote browser on our server
        Driver.driver = webdriver.Remote(
            desired_capabilities=caps,
            command_executor="http://%s:%s@hub.lambdatest.com/wd/hub"%(self.username,self.authkey)
        )


    @after_suite
    def close():
        Driver.driver.quit()

```

<br>

## Add your Test Spec and Step Implementations

We are adding the following test steps to specs -> example.spec:

```
# Getting Started with Gauge

## Let's log in
* Go to login form at "https://the-internet.herokuapp.com/login"
* Enter username "tomsmith"
* Enter password "SuperSecretPassword!"
* Click log in button
* Verify that we see logged in message "Welcome to the Secure Area. When you are done click logout below."
```

So that our test knows how to run those steps, we will also need to add the step implementations for this test under step_impl -> get_started.py

```
from getgauge.python import step
from step_impl.utils.driver import Driver

@step("Go to login form at <url>")
def go_to_login_form_at(arg1):
  Driver.driver.get(arg1)


@step("Enter username <arg1>")
def enter_username(arg1):
  Driver.driver.find_element_by_name('username').send_keys(arg1)

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
```

<br>

## Run Your Test

Now you can run your Selenium Gauge Python test on LambdaTest:

`gauge run specs`

<img height="100" alt="hyperexecute_logo" src="https://user-images.githubusercontent.com/1688653/159473714-384e60ba-d830-435e-a33f-730df3c3ebc6.png">

HyperExecute is a smart test orchestration platform to run end-to-end Selenium tests at the fastest speed possible. HyperExecute lets you achieve an accelerated time to market by providing a test infrastructure that offers optimal speed, test orchestration, and detailed execution logs.

The overall experience helps teams test code and fix issues at a much faster pace. HyperExecute is configured using a YAML file. Instead of moving the Hub close to you, HyperExecute brings the test scripts close to the Hub!

- <b>HyperExecute HomePage</b>: https://www.lambdatest.com/hyperexecute
- <b>Lambdatest HomePage</b>: https://www.lambdatest.com
- <b>LambdaTest Support</b>: [support@lambdatest.com](mailto:support@lambdatest.com)

To know more about how HyperExecute does intelligent Test Orchestration, do check out [HyperExecute Getting Started Guide](https://www.lambdatest.com/support/docs/getting-started-with-hyperexecute/)

[<img alt="Try it now" width="200 px" align="center" src="images/Try it Now.svg" />](https://hyperexecute.lambdatest.com/?utm_source=github&utm_medium=repository&utm_content=java&utm_term=testng)

To run this project on Hyperexecute you can simply use the following command:

`./hyperexecute --user 'YOUR LT_USERNAME' --key 'YOUR LT_ACCESS_KEY' --config hyperexecute.yml`
