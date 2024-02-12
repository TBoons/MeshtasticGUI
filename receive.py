from pubsub import pub
import datetime
from mesh import interface
import __main__

def onReceive(packet, interface): # called when a packet arrives
    sender = packet['fromId']
    if 'channel' in packet.keys():
        incomingChannel = packet['channel']
    else:
        incomingChannel = 0
    #print(f"\nMessage from {interface.nodes[sender]['user']['longName']} ({interface.nodes[sender]['position']['latitude']}, {interface.nodes[sender]['position']['longitude']}) to {packet['toId']} at {datetime.datetime.fromtimestamp(packet['rxTime']).strftime('%Y-%m-%d %H:%M:%S')}:\n{packet['decoded']['text']}\n")
    triggerReceive({packet['decoded']['text']},{interface.nodes[sender]['user']['longName']},incomingChannel)

def triggerReceive(message, fromNode,channel):
    __main__.updateReceivedMessages(message, fromNode, channel)
    print(f'Incoming Message: {message} from {fromNode}')

def receiverThread():
    pub.subscribe(onReceive, "meshtastic.receive.text")