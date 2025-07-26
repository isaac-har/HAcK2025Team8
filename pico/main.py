from connections import connect_mqtt, connect_internet
from time import sleep
from distSens1 import get_distance

mqttServer = "ef4663ed2bc142868e6dadce87747bb0.s1.eu.hivemq.cloud"
mqttUser = "Team8"
mqttPass = "Team8$$$"

internetUsername = "HAcK-Project-WiFi-1" #CHANGE TO CORRECT WIFI OR WILL NOT WORK
internetPassword = "UCLA.HAcK.2024.Summer"

client = None

def callback(topic, msg):

    if (topic == b"text"):
        print(msg.decode())
def getTemperature():
    return -9999 #TODO: Implement temperature sensor reading

def getLight():
    return -9999 #TODO: Implement light sensor reading
    


def main():
    try:
        connect_internet(internetUsername,password=internetPassword) #ssid (wifi name), pass
        client = connect_mqtt(mqttServer, mqttUser, mqttPass) # url, user, pass

        client.set_callback(callback)
        client.subscribe(b"text")
        

        while True:
            client.check_msg()
            sleep(0.8)
            client.publish(b"ultrasonic", str(get_distance()).encode())
            client.publish(b"temp", str(getTemperature()).encode())
            client.publish(b"light", str(getLight()).encode())

    except KeyboardInterrupt:
        print('keyboard interrupt')
        
        
if __name__ == "__main__":
    main()






