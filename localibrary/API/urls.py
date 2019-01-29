from django.urls import path
from . import views

urlpatterns =[
    path("send/",views.hook_get, name= 'api_get'),
    path("", views.post_fon, name='fon_post'),
    path ("temp/",views.save_exel,name="pd"),
    path("save/", views.list_push, name="save"),
    path("deleted/", views.list_push, name="deleted"),
    path("send_push/",views.push,name="push"),

]





