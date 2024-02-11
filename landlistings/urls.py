from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='landlistings'), 
    path('<int:landlisting_id>', views.landlisting, name="landlisting"),
]
