from django.http import HttpResponse
from django.shortcuts import render

from .models import News


def home(request):
    news = News.objects.all().order_by('-created_at')  # Получаем все новости, отсортированные по дате
    return render(request, 'main/index.html', {'news': news})