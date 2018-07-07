from django.contrib import admin
from django.urls import path
from . import views
import re
urlpatterns = [

    path('index/', views.index),
    path('city/',views.city),
    path('city/<city>/', views.scenicspot),
    path('place/<place>/', views.place),
    path('about/',views.about),
    path('contact/',views.contact),
    path('test/',views.test),
]


# urlpatterns = [
#
#     path('index/', views.index),
#     path('sight/<b>/', views.sight),
#     path('place/<place>/', views.place),
#     path('about/', views.about),
#     path('contact/',views.contact),
# ]