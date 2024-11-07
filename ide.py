import urequests
import dht
from machine import Pin, I2C
from bmp180 import BMP180  # Biblioteca do BMP180
import time

# Configuração dos sensores
dht_sensor = dht.DHT11(Pin(4))  # DHT11 no pino 4
bmp_sensor = BMP180(I2C(scl=Pin(22), sda=Pin(21)))  # BMP180 usando I2C
ldr_pin = Pin(35, Pin.IN)  # Pin para o sensor LDR ou MH-RD

# Função para coletar os dados
def read_sensors():
    # Ler o DHT11
    dht_sensor.measure()
    temperature_dht = dht_sensor.temperature()
    humidity = dht_sensor.humidity()
    
    # Ler o BMP180
    temperature_bmp = bmp_sensor.temperature
    pressure = bmp_sensor.pressure
    
    # Ler o LDR (retorna 0 ou 1 dependendo da luminosidade)
    light_level = ldr_pin.value()
    
    return {
        "temperature_dht": temperature_dht,
        "humidity": humidity,
        "temperature_bmp": temperature_bmp,
        "pressure": pressure,
        "light_level": light_level
    }

# Enviar os dados para Django
def send_data_to_django(data):
    url = 'http://YOUR_SERVER_IP/api/sensordata/'
    headers = {'Content-Type': 'application/json'}
    try:
        response = urequests.post(url, json=data, headers=headers)
        print(response.text)
        response.close()
    except Exception as e:
        print("Failed to send data:", e)

# Loop para ler e enviar os dados
while True:
    sensor_data = read_sensors()
    send_data_to_django(sensor_data)
    time.sleep(60)  # Envia os dados a cada 60 segundos
