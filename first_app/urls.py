#from -- import 
from django.urls import path
from .views import homepage, menu, who_we_are
from .views import variables, index
#code
urlpatterns = [#start urlpatterns
    path('welcome/', homepage, name = 'homepage'),
    path('menu/', menu, name = 'menu'),
    path('who_we_are/', who_we_are, name = 'who_we_are'),
    path('variables/', variables, name = 'variables'),
    path('index/', index, name = 'index'),
]#end urlpatterns