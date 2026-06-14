from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('delete/<int:id>/', views.delete_patient, name='delete_patient'),
    path('edit/<int:id>/', views.edit_patient, name='edit_patient'),
]