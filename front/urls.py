from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.index, name='index'),
	path('make/', views.MakeView.as_view(), name='make_list'),
	path('make/create/', views.MakeCreate.as_view(), name='make_create'),
	path('make/<int:pk>/update', views.MakeUpdate.as_view(), name='make_update'),
	path('make/<int:pk>/delete', views.MakeDelete.as_view(), name='make_delete'),
	path('car/create/', views.CarCreate.as_view(), name='car_create'),
	path('cars/', views.CarView.as_view(), name='car_list'),
	path('car/<int:pk>/update', views.CarUpdate.as_view(), name='car_update'),
	path('car/<int:pk>/delete', views.CarDelete.as_view(), name='car_delete'), 
]
