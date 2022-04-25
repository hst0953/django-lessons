from django.urls import resolve
from django.test import TestCase
from blog.views import home_page
from django.http import HttpRequest  
from blog.models import Article 
from selenium import webdriver

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')  
        self.assertEqual(found.func, home_page)  

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()  
        response = home_page(request)  
        html = response.content.decode('utf8')

        self.assertTrue(html.startswith('<html>'))  
        self.assertIn('<title>To-Do lists</title>', html)
        self.assertIn('<h1>To-Do lists</h1>', html)
        self.assertTrue(html.endswith('</html>'))


    def test_article_model_save_and_retrieve(self):
        # создай статью 1
        # сохрани статью 1 в базе
        article1 = Article(
            title = 'article 1',
            full_text = 'full_text 1',
            summary = 'summary 1',
            category = 'category 1',
            pubdate = 'pubdate 1',
        )
        article1.save()

        # создай стаью 2
        # сохрани статью 2 в базе
        article2 = Article(
            title = 'article 2',
            full_text = 'full_text 2',
            summary = 'summary 2',
            category = 'category 2',
            pubdate = 'pubdate 2',
        )
        article2.save()

        # загрузи из базы все статьи
        all_articles = Article.objects.all()

        # проверь: статей должно быть 2
        self.assertEqual(len(all_articles), 2)

        # проверь: 1 загруженная из базы статья == статья 1
        self.assertEqual(
            all_articles[0].title,
            article1.title
        )
        # проверь: 2 загруженная из базы статья == статья 2
        self.assertEqual(
            all_articles[1].title,
            article2.title
        )