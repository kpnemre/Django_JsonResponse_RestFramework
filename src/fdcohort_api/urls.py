

from django.urls import path
from django.urls.conf import include
from .views import home_api, student_list_api


urlpatterns = [
   
    path('home-api/', home_api),
    path('list-api/', student_list_api),

]