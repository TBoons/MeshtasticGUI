import meshtastic
import meshtastic.serial_interface

#lora.modem_preset

interface = meshtastic.serial_interface.SerialInterface()
print('Mesh Device Ready!')
myNodeInfo = interface.getMyNodeInfo()


# nodeInfo = interface.getNode(myNodeInfo['user']['id'])
nodeInfo = interface.getNode('^local')
#print(f'Our node preferences:{nodeInfo.localConfig.lora.modem_preset}')

#print(nodeInfo.channels)

channelNames = []
channelIndexes = []

for chan in nodeInfo.channels:
	psk = chan.settings.psk
	if len(psk) > 0:
		if len(chan.settings.name) == 0:
			thisChannelName = 'DefaultCh'
		else:
			thisChannelName = chan.settings.name
		channelNames.append(thisChannelName)
		channelIndexes.append(chan.index)
theChans = dict(zip(channelNames,channelIndexes))
