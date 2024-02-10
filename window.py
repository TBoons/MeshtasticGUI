import tkinter as tk
import mesh
import send
import receive
import threading

from pubsub import pub
import datetime

print('here')

def on_button_click():
    text = entry.get()
    print("Entered text:", text)
    send.sendText(text)

# Create the main window
root = tk.Tk()
root.title("Meshtastic GUI")
root.geometry("400x200")  # Set window size to 400x200 pixels

# Create a label and text entry field for "Enter something"
label_enter = tk.Label(root, text="Enter something:")
label_enter.pack()

entry = tk.Entry(root)
entry.pack()

# Create a label and text entry field for "Incoming Messages"
label_incoming = tk.Label(root, text="Incoming Messages:")
label_incoming.pack()

# Create a text area for incoming messages
text_area = tk.Text(root, height=5)
text_area.pack()

# Create a button
button = tk.Button(root, text="Submit", command=on_button_click)
button.pack()

def updateReceivedMessages(message):
    print(next(iter(message)))
    text_area.insert(tk.END, next(iter(message)))


def function_in_thread():
    while True:
        receive.receiverThread()

# Create a thread for the function
thread = threading.Thread(target=function_in_thread)

# Start the thread
thread.start()

# Run the main event loop
root.mainloop()

