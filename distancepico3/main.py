from connections import connect_mqtt, connect_internet
from time import sleep
from machine import ADC, Pin
from distSens1 import get_distance

mqttServer = "ef4663ed2bc142868e6dadce87747bb0.s1.eu.hivemq.cloud"
mqttUser = "Team83"
mqttPass = "Team8$$$3"

internetUsername = "bruins" #CHANGE TO CORRECT WIFI OR WILL NOT WORK
internetPassword = "connect12"

client = None

def main():
    try:
        connect_internet(internetUsername,password=internetPassword) #ssid (wifi name), pass
        client = connect_mqtt(mqttServer, mqttUser, mqttPass) # url, user, pass

        while True:
            distance = str(get_distance())
            client.publish(b"ultrasonic", distance.encode())
            print(f"Distance: {distance} cm")
            sleep(0.5)

    except KeyboardInterrupt:
        print('keyboard interrupt')
        
        
if __name__ == "__main__":
    main()






