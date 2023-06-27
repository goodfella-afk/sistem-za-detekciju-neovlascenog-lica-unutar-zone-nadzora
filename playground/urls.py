from django.urls import path, include
from . import views 


urlpatterns = [ 
     path('', views.say_hello),
     path('reqReboot',views.reqReboot),
     path('reqStart',views.reqStart),
     path('reqStop',views.reqStop)
]