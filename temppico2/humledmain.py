import machine
import time
import dht

# Pin setup
sensor_pin = machine.Pin(6)  # GP2 for sensor

# Initialize DHT11 sensor
sensor = dht.DHT11(sensor_pin)

def read_sensor():
    """Read temperature and humidity from sensor"""
    try:
        sensor.measure()
        temp = (sensor.temperature() * 1.8) + 32  # Convert Celsius to Fahrenheit
        humidity = sensor.humidity()
        return temp, humidity
    except OSError as e:
        print(f"Sensor read error: {e}")
        return None, None

