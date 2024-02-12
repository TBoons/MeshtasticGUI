import tkinter as tk
from tkinter import ttk
import mesh
import send
import receive
import window_functions

from pubsub import pub
import datetime

userShortName = mesh.myNodeInfo["user"]["shortName"]

#TODO - Fix outgoing message to send to correct tab
#TODO - make figuring our Channels and Index and utility
def send_message_to_mesh(self):
    text = entry.get()
    #sendChannelIndex = channelIndex.get()
    sendChannelIndex = mesh.theChans[channelSection.get()]
    #print("Sending text:", text)
    send.sendText(text,int(sendChannelIndex))
    print(f'Outgoing Messages: {text}')
    insert_message_text( formatMessage(f"{userShortName}: ", text), "left" )
    entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
#root.protocol("WM_DELETE_WINDOW", window_functions.on_close)
root.title("Meshtastic GUI")
root.geometry("600x400")  # Set window size to 400x200 pixels

# Create a label and text entry field for "Enter something"
label_enter = tk.Label(root, text="Send Message:")
label_enter.pack()

entry = tk.Entry(root, width=75)
entry.bind('<Return>', send_message_to_mesh)
entry.pack()

# Create a button
# button = tk.Button(root, text="Send", command=send_message_to_mesh)
# button.pack()

# Create a label and text entry field for "Incoming Messages"
label_incoming = tk.Label(root, text="Message Thread:")
label_incoming.pack()

# Create a text area for incoming messages
#text_area = tk.Text(root, height=5)
text_area = tk.Text(root, height=4, width=75, state=tk.DISABLED)
text_area.tag_configure("right", justify="right")
text_area.tag_configure("left", justify="left")
text_area.pack()

tabControl = ttk.Notebook(root)
channelTabs = {}
  
for channel in mesh.theChans:
    channelTabs[channel] = ttk.Frame(tabControl)
    tabControl.add(channelTabs[channel], text =channel)
    channelTabs[channel].text_area = tk.Text( channelTabs[channel], height=5 )
    #channelTabs[channel].text_area.insert(tk.END, f'This is the {channel} channel')
    channelTabs[channel].text_area.pack() 
tabControl.pack(expand = 1, fill ="both")

#USER and CHANNEL Info
label_nodeInfo = tk.Label(root, text="User:")
label_nodeInfo.pack(side = "left")
nodeInfo = tk.Text(root, height=1, width=10)
nodeInfo.insert(tk.END, userShortName)
nodeInfo.config(state=tk.DISABLED)
nodeInfo.pack(side = "left")

label_channelSection = tk.Label(root, text="Channel:")
label_channelSection.pack(side = "left")
channelNames=list(mesh.theChans.keys())
sel=tk.StringVar() # string variable for the Combobox
channelSection=ttk.Combobox(root,values=channelNames,width=15,
    textvariable=sel)
channelSection.current(0)
channelSection.pack(side = "left")

def insert_message_text(message, direction, incomingChannel):
    currentMessageChannel = ''
    #todo - put this out in the open for all things to use
    for chan in mesh.theChans:
         if mesh.theChans[chan] == incomingChannel:
            currentMessageChannel = chan
            break
    channelTabs[currentMessageChannel].text_area.config(state=tk.NORMAL)  # Set state to normal to allow editing
    channelTabs[currentMessageChannel].text_area.insert(tk.END, message, direction)  # Insert new item at the end
    channelTabs[currentMessageChannel].text_area.config(state=tk.DISABLED)  # Set state back to disabled to make it read-only
    channelTabs[currentMessageChannel].text_area.yview(tk.END)  # Auto-scroll to the end

def formatMessage(fromNode, message):
    return f'{fromNode}: {message}\n'

def updateReceivedMessages(message, fromNode,channel):
    receivedMessage = next(iter(message))
    insert_message_text( formatMessage(next(iter(fromNode)), receivedMessage), "right", channel )

def function_in_thread():
    receive.receiverThread()
    root.after(500, function_in_thread)

function_in_thread()
# Run the main event loop
root.mainloop()
