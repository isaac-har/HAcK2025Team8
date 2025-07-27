from connections import connect_mqtt, connect_internet
from time import sleep
from distSens1 import get_distance
from watchdisplay import oledActivate

mqttServer = "ef4663ed2bc142868e6dadce87747bb0.s1.eu.hivemq.cloud"
mqttUser = "Team8"
mqttPass = "Team8$$$"

internetUsername = "HAcK-Project-WiFi-1" #CHANGE TO CORRECT WIFI OR WILL NOT WORK
internetPassword = "UCLA.HAcK.2024.Summer"

client = None

currWatchMode = 1

def callback(topic, msg):
    global currWatchMode
    if (topic == b"text"):
        print(msg.decode())
    elif (topic == b"watchmode"):
        currWatchMode = int(msg.decode())
        print(f"Watch mode set to {currWatchMode}")

def main():
    try:
        connect_internet(internetUsername,password=internetPassword) #ssid (wifi name), pass
        client = connect_mqtt(mqttServer, mqttUser, mqttPass) # url, user, pass

        client.set_callback(callback)
        client.subscribe(b"text")
        client.subscribe(b"watchmode")
        

        while True:
            client.check_msg()
            sleep(0.8)
            distance = get_distance()
            client.publish(b"ultrasonic", str(distance).encode())
            oledActivate(currWatchMode, distance)

    except KeyboardInterrupt:
        print('keyboard interrupt')
        
        
if __name__ == "__main__":
    main()






