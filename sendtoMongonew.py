#Written by Jafir Kluis, 0973013
from time import sleep
import random
import paho.mqtt.client as mqtt
import pymongo
from sense_hat import SenseHat
import datetime


client = pymongo.MongoClient(
    "")
db = client.KluisDB

broker = ''
client = mqtt.Client()
client.connect(broker,1883,60)

sense = SenseHat()
sense.clear()



def send_to_desktop():
    client.publish("topic/*", f'{temp} ');

    
def insert_temp_in_Mongo():
    

    # create 1 document
    db.KluisValues4.insert_one({"sensor_name": "temperature", "value": temp, "time": time})
    # create multiple documents

    print(time, temp)
    
    
while True:
    temp = round(sense.get_temperature())
    now = datetime.datetime.now()
    time = now.strftime("%d/%m/%Y %H:%M:%S")
    send_to_desktop()
    insert_temp_in_Mongo()
    sleep(5)
