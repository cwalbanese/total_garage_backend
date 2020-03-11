from django.urls import path
from .views import current_user, UserList
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('current_user/', current_user),
    path('users/', UserList.as_view()),
    # path('years/', views.YearList.as_view(), name='year_list'),
    # path('years/<int:pk>', views.YearSpecific.as_view(), name='year_specific'),
    path('repairs/', views.RepairList.as_view(), name='repair_list'),
    path('repairs/<int:pk>', views.RepairSpecific.as_view(), name='repair_specific'),
]