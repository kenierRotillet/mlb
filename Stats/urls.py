
from django.urls import path,include
from Stats import views

urlpatterns = [
    path('index/',views.index,name='index')
]