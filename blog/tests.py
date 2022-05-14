from typing import Any
from django.urls import resolve
from django.test import TestCase
from blog.views import home_page, article_page
from django.http import HttpRequest  
from blog.models import Article 
from selenium import webdriver
from datetime import datetime
from django.urls import reverse
import pytz

class ArticlePageTest(TestCase):

    def test_article_page_displays_correct_article(self):
        Article.objects.create(
            title = 'title 1',
            summary = 'summary 1',
            full_text = 'full_text 1',
            pubdate = datetime.utcnow().replace(tzinfo = pytz.utc),
            slug = 'slug 1'
        )

        request = HttpRequest()
        response = article_page(request, 'slug 1')
        html = response.content.decode('utf8')

        self.assertIn('title 1', html)
        self.assertIn('full_text 1', html)
        self.assertIn('summary 1', html)

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')  
        self.assertEqual(found.func, home_page)  

    def test_home_page_returns_correct_html(self):
        url = reverse('home_page')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'home_page.html')


    def test_article_model_save_and_retrieve(self):
        # создай статью 1
        # сохрани статью 1 в базе
        article1 = Article(
            title = 'article 1',
            full_text = 'full_text 1',
            summary = 'summary 1',
            category = 'category 1',
            pubdate = datetime.utcnow().replace(tzinfo = pytz.utc),
            slug = 'slug-1'
        )
        article1.save()

        # создай стаью 2
        # сохрани статью 2 в базе
        article2 = Article(
            title = 'article 2',
            full_text = 'full_text 2',
            summary = 'summary 2',
            category = 'category 2',
            pubdate = datetime.utcnow().replace(tzinfo = pytz.utc),
            slug = 'slug-2'
        )
        article2.save()

        # загрузи из базы все статьи
        all_articles = Article.objects.all()

        # проверь: статей должно быть 2
        self.assertEqual(len(all_articles), 2)

        # проверь: 1 загруженная из базы статья == статья 1
        self.assertEqual(
            all_articles[0].slug,
            article1.slug
        )
        # проверь: 2 загруженная из базы статья == статья 2
        self.assertEqual(
            all_articles[1].slug,
            article2.slug
        )

        self.assertEqual(
            all_articles[0].title,
            article1.title
        )
        # проверь: 2 загруженная из базы статья == статья 2
        self.assertEqual(
            all_articles[1].title,
            article2.title
        )
