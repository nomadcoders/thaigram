from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Image
from django.views.decorators.csrf import csrf_exempt

"""
Create URL
Create View
Create template (BS) & Render
Add URL
Grab the data.
Render real data (
    user profile.
    image_set
    per image:
        like count
        comment count
)
HTML
Drop CSS.
Media querys + responsive

"""

# Create your views here.


def index_view(potato):
    if potato.method == "GET":
        if potato.user.is_authenticated:
            all_images = Image.objects.all()
            return render(potato, 'feed.html', context={'all_images': all_images})
        else:
            return render(potato, 'login.html')


def explore_view(request):
    """
    0) Create a shit ton of users
    1) Create the View 
    2) Create the URL
    3) Link the HTML to my URL (name)
    4) Fill the view (check the method, check authentication)
    5) Get all the User objcts on the DB
    6) I will import my explore.html as a template (just like feed, with extends)
    7) I will render the template with context
    8) Update the html and do a for user in all_users
    """
    return HttpResponse('this is explore')


def profile_view(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return render(request, 'profile.html', context={'user': request.user})
        else:
            return render(request, 'login.html')


@csrf_exempt
def upload(request):
    if request.method == "POST":
        description = request.POST.get('description')
        file = request.FILES.get('photo')
        location = request.POST.get('location')
        Image.objects.create(
            file=file,
            caption=description,
            location=location,
            author=request.user
        )
    return render(request, 'profile.html', context={'user': request.user})
