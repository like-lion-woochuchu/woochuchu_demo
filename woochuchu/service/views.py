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

def tip(request):
  return render(request, 'tip.html')

def tip_detail(request):
  return render(request, 'tip_detail.html')

def adopt(request):
  return render(request, 'adopt.html')

def adopt_detail(request):
  return render(request, 'adopt_detail.html')

def lost(request):
  return render(request, 'lost.html')

def lost_detail(request):
  return render(request, 'lost_detail.html')

def make_user(request):
  user = User()
  user.name = "Paul"
  user.profile_img_url = "https://www.incimages.com/uploaded_files/image/1920x1080/getty_481292845_77896.jpg"
  user.save()

  return redirect('index')
  
def make_post(request):
  main_feed = MainFeed()
  main_feed.user = User.objects.get(user_id=1)
  main_feed.body = "으르렁"
  main_feed.img_url = "https://www.aaha.org/contentassets/3c00345bcc2d430b9f471734e8417d75/2019-6-6-istock-460588321-osu-mean-dog-blog.jpg"
  main_feed.like = 0
  main_feed.save()

  return redirect('index')

def test(request):
  return render(request, 'test.html')