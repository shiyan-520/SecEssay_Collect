from django.urls import path
from Authentication import views


urlpatterns = [
    path('', views.index_logout,name='index_logout'),
]



