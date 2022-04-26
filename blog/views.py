from django.shortcuts import render
from django.http import HttpResponse
from .models import Article

# Create your views here.
def home_page(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'home_page.html', context)

