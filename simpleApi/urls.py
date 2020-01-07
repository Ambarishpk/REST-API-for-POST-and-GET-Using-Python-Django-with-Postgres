from django.contrib import admin
from django.urls import path
from myApiApp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('postdetails/',views.postDetails),
    path('fetchdetails/',views.fetchDetails)
]
