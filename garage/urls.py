from django.urls import path
from .views import current_user, UserList
from . import views
from rest_framework.routers import DefaultRouter

# API endpoints to be used by frontend

urlpatterns = [
    path('current_user/', current_user),
    path('users/', UserList.as_view()),
    path('repairs/', views.RepairList.as_view(), name='repair_list'),
    path('repairs/<int:pk>', views.RepairSpecific.as_view(), name='repair_specific'),
]