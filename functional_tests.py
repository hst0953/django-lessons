from selenium import webdriver
import unittest

w = 'install'

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
        browser = self.browser.get('http://127.0.0.1:8000')
        header = browser.find_elements_by_tag_name('h1')[0]
        self.assertIn(w, header)  

if __name__ == '__main__':  
    unittest.main()