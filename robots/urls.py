from django.urls import path
from .views import RobotCreateView, generate_weekly_report

urlpatterns = [
    path('robots/', RobotCreateView.as_view(), name='robot-create'),
    path('download_weekly_report/', generate_weekly_report, name='download_weekly_report'),
]
