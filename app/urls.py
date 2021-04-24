from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('vrc/', views.vrc, name="vrc"),
    path('lrc/', views.lrc, name="lrc"),
    path('vrc_lrc/', views.vrc_lrc, name="vrc_lrc"),
    path('hamming/', views.hamming, name="hamming"),
    path('about/', views.about, name="about"),
    path('repreprep/', views.rep, name="rep"),
]
