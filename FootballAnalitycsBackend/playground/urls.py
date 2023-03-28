from django.urls import path
from . import  views

#url conf
urlpatterns = [
    path('hello/',views.say_hello) ,
    
    path('bye/',views.say_bye),
    path('players/',views.all_players) 

]