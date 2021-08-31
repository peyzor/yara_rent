from django.urls import path

from . import views

app_name = 'rent'

urlpatterns = [
    path('car-list/', views.car_list, name='car_list'),
    path('car-list/<int:pk>', views.car_detail, name='car_detail'),
]