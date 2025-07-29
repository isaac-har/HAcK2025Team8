from machine import Pin, ADC, PWM, time_pulse_us
import time
import ssd1306


trigPin = Pin(2, Pin.OUT)
echoPin = Pin(3, Pin.IN)
led = PWM(Pin(15, Pin.OUT))
button = Pin(5, Pin.IN, Pin.PULL_UP)

# speed of sound at 20Celsius is 343 m/s
soundSpeedm = 346 # m/s

# convert 343 m/s to cm/s: 
soundSpeedin = soundSpeedm * 100


def get_distance():
    trigPin.value(0) # turn off trigger pin
    time.sleep_us(4)
    trigPin.value(1) # turn on trigger pin to send out pulse
    time.sleep_us(10)
    trigPin.value(0) # turn off trigger pin

    duration = 0
    duration = time_pulse_us(echoPin, 1, 30000) # wait for echo to return for 0.03s

    if duration < 0:
        return -9999

    # calculate distance in inches (remember duration is in microseconds)
    dist = duration * soundSpeedin / 2000000 # divide by 2 for round trip
    if dist is None:
        return -9999
    else:
        return dist