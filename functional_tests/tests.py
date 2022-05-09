from selenium import webdriver
from selenium.webdriver.common.by import By
from django.test import LiveServerTestCase
import unittest
from blog.models import Article
from datetime import datetime
import pytz

w = 'Какая-то страница'

class BasicInstallTest(LiveServerTestCase):  

    def setUp(self):  
        self.browser = webdriver.Chrome()

    def tearDown(self):  
        self.browser.quit()

    def test_home_page_title(self):  
        # у пользователя открылся сайт
        # пользователь прочитал заголовок сайта
        self.browser.get(self.live_server_url)
        self.assertIn(w, self.browser.title)  
    
    def test_home_page_header(self):  
        # пользователь прочитал шапку сайта
        self.browser.get(self.live_server_url)
        header = self.browser.find_element(By.TAG_NAME,'h1')
        self.assertIn('Виктор Болдырев', header.text) 

    def test_layout_and_styling(self):
        # Edith goes to the home page
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024, 768)

        # She notices the input box is nicely centered
        header = self.browser.find_element(By.TAG_NAME, 'h1')
        self.assertTrue(header.location['x'] > 10) 

    def test_home_page_blog(self):
        self.browser.get(self.live_server_url)
        #article_list = self.browser.find_element_by_class_name('article-list')
        article_list = self.browser.find_element(By.CLASS_NAME,'article-list')
        self.assertTrue(article_list)

    def test_home_page_acticles_look_correct(self):
        self.browser.get(self.live_server_url)
        #article_title = self.browser.find_element(By.CLASS_NAME,
        #    'article-title')
        article_summary = self.browser.find_element(By.CLASS_NAME,
            'article-summary')
        #article_list = self.browser.find_element_by_class_name('article-list')
        article_list = self.browser.find_element(By.CLASS_NAME,'article-list')
        self.assertTrue(article_list)
        self.assertTrue(article_summary)

    # проверяем открывается ли статья по клику
    def test_home_page_article_title_link_leads_to_article_page(self):

        # открываем главную страницу
        self.browser.get(self.live_server_url)

        # создаем переменную с заголовком страницы
        article_title = self.browser.find_element(By.CLASS_NAME,
            'article-title')
        article_title_text = article_title.text
        
        # находим ссылку в заголовке статьи
        article_link = self.browser.find_element(By.TAG_NAME,'a')

        # переходим по ссылке
        self.browser.get(article_link.get_attribute('href'))

        # ожидаем что статья открылась
        # text добавляем чтобы получить текст, а не тег
        article_page_title = self.browser.find_element(By.CLASS_NAME,
            'article-title')
        self.assertEqual(article_title_text, article_page_title.text)

