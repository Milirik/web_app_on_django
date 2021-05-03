from django.contrib.auth.views import LogoutView
from django.urls import path, include
from .views import index, auth

app_name = 'main'


urlpatterns = [
    path('auth/', auth, name='auth'),
    path('logout/', LogoutView.as_view(next_page='main:auth'), name='logout'),
    path('', index, name='index')
]
