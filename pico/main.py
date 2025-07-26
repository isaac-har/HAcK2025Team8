from connections import connect_mqtt, connect_internet
from time import sleep

mqttServer = "ef4663ed2bc142868e6dadce87747bb0.s1.eu.hivemq.cloud"
mqttUser = "Team8"
mqttPass = "Team8$$$"

internetUsername = "HAcK-Project-WiFi-1" #CHANGE TO CORRECT WIFI OR WILL NOT WORK
internetPassword = "UCLA.HAcK.2024.Summer"

client = None

def callback(topic, msg):

    if (topic == b"text"):
        print(msg.decode())



def main():
    try:
        connect_internet(internetUsername,password=internetPassword) #ssid (wifi name), pass
        client = connect_mqtt(mqttServer, mqttUser, mqttPass) # url, user, pass

        client.set_callback(callback)
        client.subscribe("text")

        while True:
            client.check_msg()
            sleep(0.1)

    except KeyboardInterrupt:
        print('keyboard interrupt')
        
        
if __name__ == "__main__":
    main()






