from django.urls import path
from about_me.views import about_me_view, hobby_view, time_view, random_numbers_view


urlpatterns = [
    path('about/', about_me_view),
    path('myhobby/', hobby_view),
    path('datatime/', time_view),
    path('random_numbers/', random_numbers_view),
]