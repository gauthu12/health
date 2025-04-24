import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import requests

def check_all_apps():
    with open('apps_config.json', 'r') as f:
        apps = json.load(f)
    
    status_report = {}
    for app in apps:
        try:
            options = Options()
            options.headless = True
            driver = webdriver.Chrome(options=options)
            driver.get(app['url'])

            driver.find_element(By.NAME, app['username_field']).send_keys(app['username'])
            driver.find_element(By.NAME, app['password_field']).send_keys(app['password'])
            driver.find_element(By.NAME, app['submit_button']).click()

            if "dashboard" in driver.current_url or driver.current_url != app['url']:
                status = "UP"
            else:
                status = "DOWN"
            driver.quit()
        except Exception as e:
            status = "DOWN"

        try:
            response = requests.get(app['url'], timeout=5)
            if response.status_code != 200:
                status = "DOWN"
        except:
            status = "DOWN"

        status_report[app['name']] = status
    return status_report
