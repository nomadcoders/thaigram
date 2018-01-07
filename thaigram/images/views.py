from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index_view(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return HttpResponse(f'Your email is {request.user.email}')
        else:
            return HttpResponse('Please log in.')
