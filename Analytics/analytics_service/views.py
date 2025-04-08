from rest_framework import generics
from .models import AnalyticsEvent
from .serializers import AnalyticsEventSerializer

class AnalyticsEventCreateAPIView(generics.CreateAPIView):
    queryset = AnalyticsEvent.objects.all()
    serializer_class = AnalyticsEventSerializer
