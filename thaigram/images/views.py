from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Image

# Create your views here.


def index_view(potato):
    if potato.method == "GET":
        if potato.user.is_authenticated:
            all_images = Image.objects.all()
            return render(potato, 'feed.html', context={'all_images': all_images})
        else:
            return render(potato, 'login.html')
