import tkinter as tk
import mesh
import send
import receive
import threading

from pubsub import pub
import datetime

userShortName = mesh.myNodeInfo["user"]["shortName"]

def send_message_to_mesh(self):
    text = entry.get()
    sendChannelIndex = channelIndex.get()
    print(sendChannelIndex)
    print("Entered text:", text)
    send.sendText(text,int(sendChannelIndex))
    insert_message_text( formatMessage(f"{userShortName}: ", text), "left" )
    entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Meshtastic GUI")
root.geometry("600x400")  # Set window size to 400x200 pixels

# Create a label and text entry field for "Enter something"
label_enter = tk.Label(root, text="Message:")
label_enter.pack()

entry = tk.Entry(root, width=75)
entry.bind('<Return>', send_message_to_mesh)
entry.pack()

# Create a button
# button = tk.Button(root, text="Send", command=send_message_to_mesh)
# button.pack()

# Create a label and text entry field for "Incoming Messages"
label_incoming = tk.Label(root, text="Incoming Messages:")
label_incoming.pack()

# Create a text area for incoming messages
#text_area = tk.Text(root, height=5)
text_area = tk.Text(root, height=10, width=40, state=tk.DISABLED)
text_area.tag_configure("right", justify="right")
text_area.tag_configure("left", justify="left")
text_area.pack()


#USER and CHANNEL Info
label_nodeInfo = tk.Label(root, text="User:")
label_nodeInfo.pack(side = "left")
nodeInfo = tk.Text(root, height=1, width=10)
nodeInfo.insert(tk.END, userShortName)
nodeInfo.config(state=tk.DISABLED)
nodeInfo.pack(side = "left")

label_ChannelIndex = tk.Label(root, text="Channel Index:")
label_ChannelIndex.pack(side = "left")
channelIndex = tk.Entry(root, width=5)
channelIndex.insert(tk.END, '0')
channelIndex.pack(side = "left")

def insert_message_text(message, direction):
    text_area.config(state=tk.NORMAL)  # Set state to normal to allow editing
    text_area.insert(tk.END, message, direction)  # Insert new item at the end
    text_area.config(state=tk.DISABLED)  # Set state back to disabled to make it read-only
    text_area.yview(tk.END)  # Auto-scroll to the end

def formatMessage(fromNode, message):
    return f'{fromNode}: {message}\n'

def updateReceivedMessages(message, fromNode):
    receivedMessage = next(iter(message))
    insert_message_text( formatMessage(next(iter(fromNode)), receivedMessage), "right" )

def function_in_thread():
    while True:
        receive.receiverThread()

# Create a thread for the function
thread = threading.Thread(target=function_in_thread)

# Start the thread
thread.start()

# Run the main event loop
root.mainloop()