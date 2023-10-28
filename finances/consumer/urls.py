from django.urls import path
from consumer import views


urlpatterns = [
    path('sign-in/', views.sign_in, name='sign_in'),
    path('sign-up/', views.sign_up, name='sign_up'),
    path('profile/', views.profile, name='profile'),
    path('create-cost-group/', views.create_cost_group, name='create-cost-group'),
    path('create-cost-record/', views.create_cost_record, name='create-cost-record'),
]