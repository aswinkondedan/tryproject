from django.urls import path
from . import views



urlpatterns = [
    path('home',views.homefunction,name='home'),
    path('about',views.aboutfunction,name='home'),
    path('design',views.designfunction,name='design'),
    
 
] 