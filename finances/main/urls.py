from django.urls import path
from main import views


urlpatterns = [
    path('home/', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('sign-in/', views.contacts, name='sign_in'),
]