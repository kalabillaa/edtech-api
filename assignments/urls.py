from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_assignment),
    path('submit/', views.submit_assignment),
    path('submissions/', views.view_submissions),
]
