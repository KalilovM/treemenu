from django.contrib import admin
from django.urls import path
from tree import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("home/child/", views.home, name="home-child"),
    path("home/child/child/", views.home, name="home-child-child"),
    path("home/child1/", views.home, name="home-child1"),
    path("home/child2/", views.home, name="home-child2"),
]
