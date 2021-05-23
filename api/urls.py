from django.contrib import admin
from django.urls import path
from . import views


app_name='api'

urlpatterns = [
    path('branches/autocomplete', views.autocomplete, name="autocomplete"),
    path('branches', views.search, name="search")

]