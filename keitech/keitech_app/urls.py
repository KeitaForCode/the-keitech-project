from keitech_app import views
from django.urls import path

app_name = 'keitech_app'

"""mapping the urls with the views"""
urlpatterns = [
    path('services/', views.Services.as_view(), name='services'),
    path('about/', views.About.as_view(), name='about'),
    path('contacts/', views.Contacts.as_view(), name='contacts'),
    path('QandA/', views.QuestionAnsewer.as_view(), name='qa'),
    path('join/', views.SignUp, name='signup'),
]
