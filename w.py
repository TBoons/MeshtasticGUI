import tkinter as tk
from tkinter import ttk, Canvas, ALL, Scrollbar, VERTICAL, RIGHT, Y

theChans = {"Dagwood":0,"McMinnCo":1}
userShortName = "TB1"

def send_message_to_mesh(self):
    text = entry.get()
    #sendChannelIndex = channelIndex.get()
    #sendChannelIndex = mesh.theChans[channelSection.get()]
    #print("Sending text:", text)
    #send.sendText(text,int(sendChannelIndex))
    print(f'Outgoing Messages: {text}')
    insert_message_text( formatMessage(f"{userShortName}: ", text), "left", 0 )
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

for channel in theChans:
    channelTabs[channel] = ttk.Frame(tabControl)
    tabControl.add(channelTabs[channel], text =channel)
    channelTabs[channel].canvas_area = tk.Canvas(channelTabs[channel], bg="white",scrollregion=(0,0,500,500))
    #channelTabs[channel].text_area.insert(tk.END, f'This is the {channel} channel')
    channelTabs[channel].canvas_area.pack(expand=1)
    channelTabs[channel].messages = []
tabControl.pack(expand = 1, fill ="both")

class BotBubble:
    def __init__(self,master,message=""):
        self.master = master
        self.frame = tk.Frame(master,bg="light grey")
        self.i = self.master.create_window(90,160,window=self.frame)
        #tk.Label(self.frame,text=datetime.now().strftime("%Y-%m-%d %H:%m"),font=("Helvetica", 7),bg="light grey").grid(row=0,column=0,sticky="w",padx=5)
        tk.Label(self.frame, text=message,font=("Helvetica", 9),bg="light grey").grid(row=1, column=0,sticky="w",padx=5,pady=3)
        root.update_idletasks()

def send_message():
    if bubbles:
        canvas.move(ALL, 0, -65)
    a = BotBubble(canvas,message=entry.get())
    bubbles.append(a)


def insert_message_text(message, direction, incomingChannel):
    currentMessageChannel = ''
    #todo - put this out in the open for all things to use
    for chan in theChans:
         if theChans[chan] == incomingChannel:
            currentMessageChannel = chan
            break
    if channelTabs[currentMessageChannel].messages:
        print(channelTabs[currentMessageChannel].canvas_area)
        channelTabs[currentMessageChannel].canvas_area.move(ALL, 0,-65)
    a = BotBubble(channelTabs[currentMessageChannel].canvas_area,message=message)
    channelTabs[currentMessageChannel].messages.append(a)

    # channelTabs[currentMessageChannel].text_area.config(state=tk.NORMAL)  # Set state to normal to allow editing
    # channelTabs[currentMessageChannel].text_area.insert(tk.END, message, direction)  # Insert new item at the end
    # channelTabs[currentMessageChannel].text_area.config(state=tk.DISABLED)  # Set state back to disabled to make it read-only
    # channelTabs[currentMessageChannel].text_area.yview(tk.END)  # Auto-scroll to the end

def formatMessage(fromNode, message):
    return f'{fromNode}: {message}\n'

root.mainloop()