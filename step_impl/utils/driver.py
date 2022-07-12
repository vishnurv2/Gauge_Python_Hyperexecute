import os
from getgauge.python import before_suite, after_suite
from selenium import webdriver
import requests

class Driver(object):
    driver = None

    @before_suite
    def init(self):
        self.username = os.getenv("LT_USERNAME") # replace with your LT username
        self.authkey  = os.getenv("LT_ACCESS_KEY") # replace with your LT access key


        caps = {}
        
        # replace with your desired test capabilities
        caps['name'] = 'Gauge Sample Test'
        caps['build'] = 'Python_Gauge_LambdaTest'
        caps['browserName'] = 'Chrome'
        caps['version'] = 'latest'
        caps['platform'] = 'Windows 10'


        # start the remote browser on our server
        Driver.driver = webdriver.Remote(
            desired_capabilities=caps,
            command_executor="http://%s:%s@stage-hub.lambdatest.com/wd/hub"%(self.username,self.authkey)
        )


    @after_suite
    def close():
        Driver.driver.quit()