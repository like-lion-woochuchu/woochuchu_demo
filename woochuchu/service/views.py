from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def main(request):
  return redirect('login')

def login(request):
  return render(request, 'login.html')

def index(request):
  main_feeds = MainFeed.objects.all()
  return render(request, 'main.html', {'main_feeds': main_feeds})

def make_user(request):
  user = User()
  user.name = "Paul"
  user.profile_img_url = "https://www.incimages.com/uploaded_files/image/1920x1080/getty_481292845_77896.jpg"
  user.save()

  return redirect('index')
  
def make_post(request):
  main_feed = MainFeed()
  main_feed.user = User.objects.get(user_id=2)
  main_feed.body = "하품도 잘해 내 새끼"
  main_feed.img_url = "https://i.insider.com/5e0f920d954bda5354419594?width=700"
  main_feed.like = 0
  main_feed.save()

  return redirect('index')