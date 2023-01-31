from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.Index, name='index'),
    path('home/', views.home, name='home'),
    path('predict/', views.Predict, name='predict'),
    path('records/', views.db_record, name='records'),
    path('delete/<int:pk>', views.delete, name='delete')
]
