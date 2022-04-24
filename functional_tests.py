from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

w = 'To-Do lists'

class BasicInstallTest(unittest.TestCase):  

    def setUp(self):  
        self.browser = webdriver.Chrome()

    def tearDown(self):  
        self.browser.quit()

    def test_home_page_title(self):  
        # у пользователя открылся сайт
        # пользователь прочитал заголовок сайта
        self.browser.get('http://127.0.0.1:8000')
        self.assertIn(w, self.browser.title)  
    
    def test_home_page_header(self):  
        # пользователь прочитал шапку сайта
        self.browser.get('http://127.0.0.1:8000')
        header = self.browser.find_element(By.TAG_NAME,'h1')
        self.assertIn('To-Do lists', header.text)  

if __name__ == '__main__':  
    unittest.main()