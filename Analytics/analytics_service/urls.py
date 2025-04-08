from django.urls import path
from .views import AnalyticsEventCreateAPIView

urlpatterns = [
    path('events/', AnalyticsEventCreateAPIView.as_view(), name='analytics-event-create'),
]
