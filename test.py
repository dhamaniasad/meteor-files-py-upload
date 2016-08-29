from MeteorClient import MeteorClient
from MeteorFiles import Uploader
import time

client = MeteorClient('ws://127.0.0.1:3000/websocket')
client.connect()

# upload example, work with Meteor-Files example: demo-simplest-upload
# server code: https://github.com/VeliovGroup/Meteor-Files/tree/master/demo-simplest-upload
client.subscribe('files.images.all');

uploader = Uploader(client, 'Images', transport='http', verbose=True)

uploader.upload("test.png")
while not uploader.finished:
    time.sleep(0.1)
