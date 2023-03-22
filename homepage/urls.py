from django.urls import path

from homepage.views import index

app_name = 'index'

urlpatterns = [
    path('', index, name='index')
]