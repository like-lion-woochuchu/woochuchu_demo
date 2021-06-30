"""woochuchu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from service import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name='main'),
    path('login/', views.login, name='login'),
    path('index/', views.index, name='index'),
    path('tip/', views.tip, name='tip'),
    path('tip/1', views.tip_detail, name='tip_detail'),
    path('adopt/', views.adopt, name='adopt'),
    path('adopt/1', views.adopt_detail, name='adopt_detail'),
    path('lost/', views.lost, name='lost'),
    path('lost/1', views.lost_detail, name='lost_detail'),
    path('make-user/', views.make_user, name='make_user'),
    path('make-post/', views.make_post, name='make_post'),
    # path('test/', views.test, name='test'),
]
