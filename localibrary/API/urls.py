from django.urls import path
from . import views

urlpatterns =[
    path("send/",views.hook_get, name= 'api_get'),
    path("", views.post_fon, name='fon_post'),

]




