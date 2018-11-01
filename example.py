import google_scrape
from pynput.keyboard import Key, Listener
def on_press(key):
    if key == Key.space:
        print (google_scrape.getNumResults("Water mill"))

with Listener(on_press=on_press) as listener:
    listener.join()

