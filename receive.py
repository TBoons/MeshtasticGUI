from pubsub import pub
import datetime
from mesh import interface
import __main__

def onReceive(packet, interface): # called when a packet arrives
    sender = packet['fromId']
    #print(f"\nMessage from {interface.nodes[sender]['user']['longName']} ({interface.nodes[sender]['position']['latitude']}, {interface.nodes[sender]['position']['longitude']}) to {packet['toId']} at {datetime.datetime.fromtimestamp(packet['rxTime']).strftime('%Y-%m-%d %H:%M:%S')}:\n{packet['decoded']['text']}\n")
    triggerReceive({packet['decoded']['text']})

def triggerReceive(message):
    __main__.updateReceivedMessages(message)

def receiverThread():
    pub.subscribe(onReceive, "meshtastic.receive.text")