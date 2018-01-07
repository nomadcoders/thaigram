from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
  

# Create your views here.
def index_view(potato):
    if potato.method == "GET":
        if potato.user.is_authenticated:
            return render(potato, 'feed.html')
        else:
            return render(potato, 'login.html')
