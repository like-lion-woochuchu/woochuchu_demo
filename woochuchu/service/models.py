from django.db import models

# Create your models here.
class User(models.Model):
  user_id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=30)
  profile_img_url = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

class MainFeed(models.Model):
  main_feed_id = models.AutoField(primary_key=True)
  user = models.ForeignKey('User', on_delete=models.CASCADE)
  body = models.TextField()
  img_url = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  like = models.IntegerField()

class TipFeed(models.Model):
  tip_feed_id = models.AutoField(primary_key=True)
  user = models.ForeignKey('User', on_delete=models.CASCADE)
  title = models.CharField(max_length=100)
  img_url = models.TextField()
  view = models.IntegerField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

class AdoptFeed(models.Model):
  adopt_feed_id = models.AutoField(primary_key=True)
  contact = models.CharField(max_length=30)
  animal_kind = models.CharField(max_length=30)
  feature = models.TextField()
  age = models.IntegerField()
  img_url = models.TextField()
  location = models.TextField()
  etc = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

class LostFeed(models.Model):
  lost_feed_id = models.AutoField(primary_key=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)