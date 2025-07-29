#Data Page with messages and Clock

from machine import Pin, I2C, ADC, PWM, time_pulse_us
from ssd1306 import SSD1306_I2C
import time
import machine
import network
from machine import RTC


#set up OLED
i2c = I2C(0, scl=Pin(9), sda=Pin(8))
oled = SSD1306_I2C(128, 64, i2c)
xmes = 128

#set up distance sensor
trigPin = Pin(2, Pin.OUT)
echoPin = Pin(3, Pin.IN)
# led = PWM(Pin(15, Pin.OUT))
soundSpeedm = 346 # m/s  --  speed of sound at 20Celsius is 343 m/s
soundSpeedin = soundSpeedm * 39.3700787 # in/s -- convert 343 m/s to inches:


#set up button
button = Pin(5, Pin.IN, Pin.PULL_UP)
screenState = 0


def oledActivate(screenState, distance, message, temperature, light, humidity):
    global xmes
    
    if screenState == 1:
        rtc = machine.RTC()
        timeTuple = rtc.datetime()

        Hour = timeTuple[4]-7
        Minute = timeTuple[5]
        Second = timeTuple[6]

        print(Hour,":",Minute,":",Second)
   
        oled.fill(0)
        oled.text("Time:",0,0)
        oled.text(str(Hour), 0 ,28)
        oled.text(":", 16,28)
        oled.text(str(Minute),24,28)
        oled.text(":", 40, 28)
        oled.text(str(Second), 48, 28)
        oled.show()
        
        
    
    #otherwise: default is Data Center Mode
    if screenState == 2:
        oled.fill(0)
            
        distStr = str(distance)
        oled.text("Distance:",0,8)
        oled.text(distStr, 80, 8)

        tempStr = str(temperature)
        oled.text("Temp:",0,16)
        oled.text(tempStr, 64, 16)

        lightStr = str(light)
        oled.text("Light:",0,24)
        oled.text(lightStr, 64, 24)

        humidityStr = str(humidity)
        oled.text("Humidity:",0,32)
        oled.text(humidityStr, 80, 32)
            
        oled.text(message, xmes, 0)              
        xmes = xmes - 20
        if xmes < -len(message)*6:
            xmes = 128
            
        oled.show()
            
    
            
        