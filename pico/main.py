from connections import connect_mqtt, connect_internet
import time
from watchdisplay import oledActivate
import ntptime

mqttServer = "ef4663ed2bc142868e6dadce87747bb0.s1.eu.hivemq.cloud"
mqttUser = "Team8"
mqttPass = "Team8$$$"

internetUsername = "bruins" #CHANGE TO CORRECT WIFI OR WILL NOT WORK
internetPassword = "connect12"

client = None

currWatchMode = 1
message = "Team HAPI is first in the universe!"  # Default message
temperature = "-9999"
light = "-9999"
humidity = "-9999"
distance = "-9999"

def callback(topic, msg):
    global currWatchMode
    global message
    global temperature
    global light
    global humidity
    global distance
    if (topic == b"text"):
        print(msg.decode())
    if (topic == b"watchmode"):
        if (msg.decode() == "1" or msg.decode() == "2"):
            currWatchMode = int(msg.decode())
            print(f"Watch mode set to {currWatchMode}")
        elif (msg.decode() == "none"):
            message = "Team HAPI is first in the universe!"
        else:
            message = msg.decode()
    if (topic == b"temp"):
        temperature = float(msg.decode())
    if (topic == b"humidity"):
        humidity = float(msg.decode())
    if (topic == b"light"):
        light = float(msg.decode())
    if (topic == b"ultrasonic"):
        distance = float(msg.decode())
        
            
    


def main():
    try:
        connect_internet(internetUsername,password=internetPassword) #ssid (wifi name), pass
        client = connect_mqtt(mqttServer, mqttUser, mqttPass) # url, user, pass

        time.sleep(5)

        ntptime.settime()

        client.set_callback(callback)
        client.subscribe(b"text")
        client.subscribe(b"watchmode")
        client.subscribe(b"temp")
        client.subscribe(b"humidity")
        client.subscribe(b"light")
        client.subscribe(b"ultrasonic")
        
        lastMqttCheck = 0
        lastOledUpdate = 0

        while True:
            currTime = time.ticks_ms()
            if currTime - lastMqttCheck > 100:
                client.check_msg()
                lastMqttCheck = currTime
            
            if currTime - lastOledUpdate > 1000:
                oledActivate(currWatchMode, distance, message, temperature, light, humidity)
                lastOledUpdate = currTime

    except KeyboardInterrupt:
        print('keyboard interrupt')
        
        
if __name__ == "__main__":
    main()






