from django.urls import path,include
from myapp.views import *

urlpatterns = [

    path('',Home.as_view(),name="home"),
# path('',Answer.as_view(),name="answer"),
]