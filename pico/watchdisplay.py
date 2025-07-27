#Data Page with messages and Clock
"""
How it is supposed to work:
    When it turns on, automatically, it is a watch and will tell time.
    Pressed a button (for a good second)
    Displays sensors information and messages at the same time!
    Press button (for a good second)
    Goes back to watch mode
    
PSEUDO CODE
    set up rtc
    set up dist sensor
    set up OLED
    
    set up get_distance function:
        return distance or None
    
    loop:
        Data Center!
            loop:
                CLEAR
                set variable of x coord of messages to the right (128)
                get distance
                set oled text (row1) to message
                set oled text (row2) to distance
                DISPLAY
                *see if button got clicked again:
                    Watch Screen is ON
                    break loop
                PAUSE
                CLEAR
                move x coord of messages to the left a little bit
                if the end of the message has halfway to leave the screen: REPEAT MESSAGE
                pause for a moment
                *see if button got clicked again:
                    Watch Screen is ON
                    break loop 
        button is clicked?
            Watch Mode is turned ON
            if button is clicked?
                got to Data Center Mode

"""

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
    #check button press
    #buttonCheck()
    
    # if button.value() == 0: #button got pressed
    #     time.sleep(1)  #prevent button lagging
    #     screenState = 1  #enter Watch Mode
    global xmes
    
    if screenState == 1:
        rtc = machine.RTC()
        timeTuple = rtc.datetime()

        Hour = timeTuple[4]-7
        Minute = timeTuple[5]
        Second = timeTuple[6]

        print(Hour,":",Minute,":",Second)
        
     
        # timeTuple = rtc.datetime()

        # Hour = timeTuple[4] + 5
        # Minute = timeTuple[5]
        # Second = timeTuple[6]

        # print(Hour,":",Minute,":",Second)

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
                
        if distance is not None:
            distance = round(distance,3)
            print("Distance: ", distance, "cm")
            distStr = str(distance)
            oled.text("Distance:",0,8)
            oled.text(distStr, 40, 8)
            #oled.show()
            #time.sleep(0.1)
            #oled.fill(0)
        else:
            print("no echo received")
            #oled.show()
            #time.sleep(0.1)
        tempStr = str(temperature)
        oled.text("Temp:",0,16)
        oled.text(tempStr, 40, 16)

        lightStr = str(light)
        oled.text("Light:",0,24)
        oled.text(lightStr, 40, 24)

        humidityStr = str(humidity)
        oled.text("Humidity:",0,32)
        oled.text(humidityStr, 40, 32)
            
        oled.text(message, xmes, 0)              
        xmes = xmes - 20
        if xmes < -len(message)*6:
            xmes = 128
            
        oled.show()
            
    
            
        