from django.urls import path
from consumer_profile import views



urlpatterns = [
    path('home/', views.profile, name='main'),
    path('settings/', views.SettingsView.as_view(), name='settings'),
    path('create-cost-group/', views.CreateCostGroupView.as_view(), name='create-cost-group'),
    path('create-cost-record/', views.CreateCostRecordView.as_view(), name='create-cost-record'),
]