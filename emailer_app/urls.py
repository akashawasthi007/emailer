from emailer_app import views
from django.urls import path,include

urlpatterns = [
    path('',views.index,name='index')
]
