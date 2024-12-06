from django.urls import path
from . import views
# url configuration

urlpatterns = [
    path('hello/', views.say_hello),
    path('hi/', views.say_hi),
    path('post/', views.blog_list),
    path('post/<id>/', views.blog_detail)
]