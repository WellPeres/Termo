from django.urls import path
from .views import index, termo

urlpatterns = [
    path('', index, name='index'),
    path('termo/', termo,  name='termo'),
]