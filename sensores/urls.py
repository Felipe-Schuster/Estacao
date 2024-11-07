from django.urls import path
from .views import SensorDataView

urlpatterns = [
    path('sensordata/', SensorDataView.as_view(), name='sensor'),
]
