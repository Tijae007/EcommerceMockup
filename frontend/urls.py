from django.urls import path
from frontend import views

app_name = 'frontend'

urlpatterns = [
    path('about-page/', views.about, name='about'),
    path('phones-page/', views.phones, name='phones'),
    path('laptops-page/', views.laptops, name='laptops'),
    path('shirts-page/', views.shirts, name='shirts'),
    path('screens-page/', views.screens, name='screens'),
    path('contact-page/', views.contact, name='contact'),
]
