import time
import webbrowser

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from LocalStorage import LocalStorage

NAME_COOKIE = 'new Cookie'
VALUE_COOKIE = 'something interesting'
NAME_LOCALSTORAGE = 'new LocalStorage'
VALUE_LOCALSTORAGE = 'something new in LocalStorage'


def main():
    service = Service(executable_path='chromedriver.exe')
    driver = webdriver.Chrome(service=service)
    storage = LocalStorage(driver)

    driver.get('https://google.com')

    # get cookies
    cookies = driver.get_cookies()
    print('Cookies: ', cookies)

    # add cookies
    driver.add_cookie({'name': NAME_COOKIE, 'value': VALUE_COOKIE})

    cookies = driver.get_cookies()
    print('New Cookies: ', cookies)

    # delete cookies
    driver.delete_cookie(NAME_COOKIE)

    cookies = driver.get_cookies()
    print('Deleted Cookies', cookies, end='\n============================\n')

    # ===============================

    # get data from localStorage
    print('LocalStorage:', storage)

    # set data
    storage[NAME_LOCALSTORAGE] = VALUE_LOCALSTORAGE
    print('New LocalStorage:', storage)

    # delete data
    storage.remove(NAME_LOCALSTORAGE)
    print('Deletes data in LocalStorage:', storage)

    driver.quit()


if __name__ == '__main__':
    main()


