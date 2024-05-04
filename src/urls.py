from django.urls import path
from . import views
from .views import signup, user_login

urlpatterns = [
    path('', views.title, name='title'),
    path('bo/', views.bo, name='bo'),
    path('bo2/', views.bo2, name='bo2'),
    path('bo3/', views.bo3, name='bo3'),
    path('bo4/', views.bo4, name='bo4'),
    path('bo5/', views.bo5, name='bo5'),
    path('bo6/', views.bo6, name='bo6'),
    path('bo7/', views.bo7, name='bo7'),
    path('bo8/', views.bo8, name='bo8'),
    path('bo9/', views.bo9, name='bo9'),
    path('signup', signup, name='signup'),
    path('login/', user_login, name='login'),
]
