import meshtastic
import meshtastic.serial_interface

interface = meshtastic.serial_interface.SerialInterface()

myNodeInfo = interface.getMyNodeInfo()

print('Mesh Ready')
