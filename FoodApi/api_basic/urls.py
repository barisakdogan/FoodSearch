from django.urls import path
from .views import FoodList, food_detail

urlpatterns = [
    path('foods/', FoodList),
    path('detail/<string:pk>/', food_detail),
]
