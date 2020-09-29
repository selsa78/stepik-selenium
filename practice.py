import time
from selenium import webdriver
import math
import pytest
from selenium.webdriver.support.ui import Select
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

links = [
    "https://stepik.org/lesson/236895/step/1",
    'https://stepik.org/lesson/236896/step/1',
    'https://stepik.org/lesson/236897/step/1',
    'https://stepik.org/lesson/236898/step/1',
    'https://stepik.org/lesson/236899/step/1',
    'https://stepik.org/lesson/236903/step/1',
    'https://stepik.org/lesson/236904/step/1',
    'https://stepik.org/lesson/236905/step/1'
]


@pytest.mark.parametrize('link', links)
def test_by_invalid_payment_address(link):
    browser = webdriver.Chrome()
    try:
        browser.get(link)
        time.sleep(3)
        answer = math.log(int(time.time()))
        browser.find_element_by_tag_name('textarea').send_keys(str(answer))
        time.sleep(3)
        browser.find_element_by_class_name('submit-submission').click()
        time.sleep(2)
        s = browser.find_element_by_class_name('smart-hints__hint').text
        assert s == 'Correct!'
        # button1 = browser.find_element_by_id('book')
        # WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), '$100'))
        # button1.click()
        # button2 = browser.find_element_by_id('solve')
        # browser.execute_script("return arguments[0].scrollIntoView(true);", button2)
        # x = browser.find_element_by_id('input_value').text
        # y = calc(x)
        # browser.find_element_by_id('answer').send_keys(y)
        # time.sleep(1)
        # button2.click()


    finally:
        time.sleep(1)
        browser.quit()