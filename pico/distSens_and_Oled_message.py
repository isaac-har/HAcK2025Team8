#get OLED to display distance of the dist sensor

"""
PSEUDO CODE
initialize the OLED and clear everything
look for a button being pressed:
    if pressed, then begin distance sensing.
        send out a pulse from the trigger
        collect duration in microseconds
        if measurement is not received in 0.03 seconds then it failed and send out new pulse
        take the duration measured and calculate distance using speed of sound in current temperature (24-25 Cel)
        send distance data to OLED to begin printing. (ROUND to 3 decimals)
            //print on the second row. First row is for talking
            get dist and put it on (0,8)
    if button is pressed again, then stop distance sensing.
    
    
    **Simultaneously print out messages**
    
    make a function called printMessage(string):
        declare variable xcoord starts all the way to the right
        loop:
            clear the rectance of the first row
            print message
            pause
            move starting x coord a bit to the left
            if the xcoord is less than the negative of the total amount of pixels of the message:
                BREAK
    
    while loop:
        printMessage(message)
        
"""
from machine import Pin, I2C, PWM, time_pulse_us
from ssd1306 import SSD1306_I2C
import time

#distance sensor set up
trigPin = Pin(2, Pin.OUT)
echoPin = Pin(3, Pin.IN)
led = PWM(Pin(15, Pin.OUT))
button = Pin(5, Pin.IN, Pin.PULL_UP)

#OLED set up
i2c = I2C(0, scl=Pin(9), sda=Pin(8))
oled = SSD1306_I2C(128,64,i2c)

#message to communicate in OLED
message = "HAPI first in the universe!!"

#normal watch duty
#def watchDuty():
    

#make function for printing messages
def printMessage(message):
    xmes = 128  #start from very right
    while True:
        #oled.fill_rect(0, 8, 128, 8, 0)  #clear first row
        oled.fill(0)
        oled.text(message, xmes, 0)
        oled.show()
        time.sleep(0.02)
        xmes = xmes - 2
        pxLenMes = len(message)*8  #number of char in message times 8 px per char
        if xmes < -1*pxLenMes:
            break
      
      
      
      
# speed of sound at 20Celsius is 343 m/s
soundSpeedm = 346 # m/s

# convert 343 m/s to inches: 
soundSpeedin = soundSpeedm * 39.3700787 # in/s

#make function to get distance value
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





runCode = 0  #set up some variable
while True:
    if button.value() == 0:  #means button got pressed: turn on distance sensor and run it
        runCode = 1
        if runCode == 1:   #starting distance sensor sequence
            print("distance sensing starting")
            time.sleep(2)
            while True:
                distance = get_distance()
                time.sleep(0.1)
                
                if distance is not None:
                    distance = round(distance,3)
                    print("Distance: ", distance, "in")
                    distStr = str(distance)
                    oled.text(distStr, 0, 8)
                    oled.show()
                    time.sleep(0.1)
                    oled.fill(0)
                else:
                    print("no echo received")
                    oled.text("no echo received",0, 8)
                    oled.show()
                    time.sleep(0.1)               
                
                
                if button.value() == 0:    #button got pressed again. switching to messages page
                    runCode = 2
                    break       
        if runCode == 2:     #starting message printing
            print("message page go now")
            while True:
                printMessage(message)
                if button.value() == 0:
                    runCode = 0
                    print("done with messages")
                    time.sleep(2)
                    break
                




    






