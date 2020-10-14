from django.urls import path
from .views import if_one, if_else, if_elif, for_one
#global variables
app_name = 'seconda_app'
#code
urlpatterns = [
    path('if_one/', if_one, name='if_one'),
    path('if_else/', if_else, name = 'if_else'),
    path('if_elif/', if_elif, name = 'if_elif'),
    path('for_one/', for_one, name = 'for_one'),
]