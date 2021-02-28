

from django.urls import path
from django.urls.conf import include
# from .views import home_api, student_list_create_api, student_get_update_delete,student_list_api
from .views import home_api,StudentGetUpdateDelete,StudentCreate
# from .views import home_api,student_list_api,StudentList,



urlpatterns = [
   
    path('home-api/', home_api),
    # path('list-api/', student_list_api),
    # path('list-create-api/',student_list_create_api),
    # path('list-create-api/', StudentList.as_view()),
    path('list-create-api/', StudentCreate.as_view()),
    path('<int:id>', StudentGetUpdateDelete.as_view(), name='detail'),
    # default ta pk var . id ypınca view da id yapmak gerek
    
    # path('<int:id>',StudentGetUpdateDelete.as_view()),
    # path('<int:id>/',student_get_update_delete, name="detail"),
    # path('list-api/', student_list_api),
    # path('create-api/', student_create_api),

# <int:id> kısmı slug ile de yapılabilir
]