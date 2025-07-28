from connections import connect_mqtt, connect_internet
from time import sleep
from humledmain import read_sensor
from machine import ADC, Pin

mqttServer = "ef4663ed2bc142868e6dadce87747bb0.s1.eu.hivemq.cloud"
mqttUser = "Team82"
mqttPass = "Team8$$$2"

internetUsername = "bruins" #CHANGE TO CORRECT WIFI OR WILL NOT WORK
internetPassword = "connect12"

client = None

def getLight():
    photoresistor = machine.ADC(26)  # GP26 for photoresistor
    light_value = photoresistor.read_u16()  # Read the light value
    return ((1.8657e-5 * light_value) - 0.209)

def callback(topic, msg):

    if (topic == b"text"):
        print(msg.decode())

def main():
    try:
        connect_internet(internetUsername,password=internetPassword) #ssid (wifi name), pass
        client = connect_mqtt(mqttServer, mqttUser, mqttPass) # url, user, pass

        client.set_callback(callback)
        client.subscribe(b"text")
        

        while True:
            client.check_msg()
            sleep(0.3)
            temp, humidity = read_sensor()
            print(f"Temperature: {temp}, Humidity: {humidity}")
            client.publish(b"temp", str(temp).encode())
            client.publish(b"humidity", str(humidity).encode())
            client.publish(b"light", str(getLight()).encode())

    except KeyboardInterrupt:
        print('keyboard interrupt')
        
        
if __name__ == "__main__":
    main()






