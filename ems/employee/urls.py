from django.urls import path, include
from rest_framework import routers

from employee import views

router = routers.DefaultRouter()
router.register('employee', views.EmployeeViewSet)

urlpatterns = [
    # path('employee/', views.employee),
    # path('employee/<int:id>/', views.employee_details),
    path('', include(router.urls))
]
