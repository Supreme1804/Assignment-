from django.shortcuts import render
from .models import News

# Create your views here.

def news_list(request):
    news = News.objects.all()
    return render(request, 'news/news_list.html', {'news': news})

def news_details()