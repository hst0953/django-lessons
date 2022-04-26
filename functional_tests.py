from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

w = 'Какая-то страница'

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
        self.assertIn('Виктор Болдырев', header.text)  

    def test_home_page_blog(self):
        self.browser.get("http://127.0.0.1:8000")
        article_list = self.browser.find_element_by_class_name('article-list')
        self.assertTrue(article_list)

    def test_home_page_acticles_look_correct(self):
        self.browser.get("http://127.0.0.1:8000")
        article_title = self.browser.find_element_by_class_name(
            'article-title')
        article_summary = self.browser.find_element_by_class_name(
            'article-summary')
        article_list = self.browser.find_element_by_class_name('article-list')
        self.assertTrue(article_list)
        self.assertTrue(article_summary)

# Если в админке есть статьи, то они неопубликованы
# Статьи открываются с красивым коротким адресом
        
if __name__ == '__main__':  
    unittest.main()