from machine import Pin, ADC, PWM, time_pulse_us
import time
import ssd1306


trigPin = Pin(2, Pin.OUT)
echoPin = Pin(3, Pin.IN)
led = PWM(Pin(15, Pin.OUT))
button = Pin(5, Pin.IN, Pin.PULL_UP)

#testing for start of program
frequency = 1000
num = 500
led.freq(frequency)

led.duty_u16(num)
time.sleep(0.2)
led.duty_u16(0)
time.sleep(0.2)

led.duty_u16(num)
time.sleep(0.6)
led.duty_u16(0)
time.sleep(0.2)

print("begin!")

# speed of sound at 20Celsius is 343 m/s
soundSpeedm = 346 # m/s

# convert 343 m/s to inches: 
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
    

# while True:
#     dist = get_distance()
#     time.sleep(0.1)
    
#     if dist is not None:
#         print("Distance:", dist, "inches")
#     else:
#         print("no echo received")
#     time.sleep(0.1) #wait a moment


"""
while True:
    if button.value() == 0:  # button pressed
        led.value(1)  # turn on LED
        dist1 = get_distance()
        time.sleep(0.1)
        dist2 = get_distance()
        time.sleep(0.1)
        dist3 = get_distance()
        time.sleep(0.1)

        if dist1 is not None:
            print("Distance 1:", dist1, "inches")
        else:
            print("No echo received")
        time.sleep(0.1)  # wait

        if dist2 is not None:
            print("Distance 2:", dist2, "inches")
        else:
            print("No echo received")
        time.sleep(0.1)  # wait

        if dist3 is not None:
            print("Distance 3:", dist3, "inches")
        else:
            print("No echo received")
        time.sleep(0.1)  # wait

    else:
        led.value(0)  # turn off LED
    time.sleep(0.1)  # small delay to debounce button
    """






"""from machine import Pin, ADC, PWM, time_pulse_us
import time

trigPin = Pin(2, Pin.OUT)
echoPin = Pin(3, Pin.IN)
led = Pin(4, Pin.OUT)
button = Pin(5, Pin.IN, Pin.PULL_UP)

# speed of sound at 20Celsius is 343 m/s
soundSpeedm = 343 # m/s

# convert 343 m/s to inches: 
soundSpeedin = soundSpeedm * 39.3700787 # in/s


def get_distance():
    trigPin.value(0) # turn off trigger pin
    time.sleep_us(4)
    trigPin.value(1) # turn on trigger pin to send out pulse
    time.sleep_us(10)
    trigPin.value(0) # turn off trigger pin

    duration = 0
    duration = time_pulse_us(echoPin, 1, 30000) # wait for echo to return for 0.03s

    if duration < 0:
        return None

    # calculate distance in inches (remember duration is in microseconds)
    dist = duration * soundSpeedin / 2000000 # divide by 2 for round trip
    return dist

while True:
    if button.value() == 0:  # button pressed
        led.value(1)  # turn on LED
        dist1 = get_distance()
        time.sleep(0.1)
        dist2 = get_distance()
        time.sleep(0.1)
        dist3 = get_distance()
        time.sleep(0.1)

        if dist1 is not None:
            print("Distance 1:", dist1, "inches")
        else:
            print("No echo received")
        time.sleep(0.1)  # wait

        if dist2 is not None:
            print("Distance 2:", dist2, "inches")
        else:
            print("No echo received")
        time.sleep(0.1)  # wait

        if dist3 is not None:
            print("Distance 3:", dist3, "inches")
        else:
            print("No echo received")
        time.sleep(0.1)  # wait

    else:
        led.value(0)  # turn off LED
    time.sleep(0.1)  # small delay to debounce button
    """
