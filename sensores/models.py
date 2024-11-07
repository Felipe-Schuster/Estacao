from django.db import models
from django.shortcuts import render


class SensorData(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    temperature_dht = models.FloatField()
    humidity = models.FloatField()
    temperature_bmp = models.FloatField()
    pressure = models.FloatField()
    light_level = models.IntegerField()  # 0 ou 1

    def __str__(self):
        return f"Data from {self.timestamp}"
    


def sensor_data_list(request):
    data = SensorData.objects.all().order_by('-timestamp')[:50]  # Mostra os últimos 50 registros
    return render(request, 'sensors/sensor_data_list.html', {'data': data})
