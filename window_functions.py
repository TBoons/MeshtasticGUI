import sys
import time
import __main__

def on_close():
    print('Closing...')
    __main__.runPro = False