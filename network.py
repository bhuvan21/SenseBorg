import threading
import requests
import queue
import time

class Sender:
    def __init__(self):
        self.thread = threading.Thread(target=self.mainloop)

        self.queue = queue.Queue()

        self.to_send = []

        self.thread.setDaemon(True)
        self.thread.start()
        self.last_sent = 0

    def mainloop(self):
        while True:
            recents = []
            recent = None
            while True:
                try:
                    recent = self.queue.get(block=False)
                    recents.append(recent)
                except queue.Empty:
                    if recent is not None:
                        break
            
            for recent in recents:
                son = {"main": self.to_send}
                names = ["accX", "accY", "accZ", "gyroX", "gyroY", "gyroZ", "magX", "magY", "magZ"]
                units = ["ms^-2"]*3 + ["degs^-2"]*3 + ["T"]*3
                for i in range(9):
                    packet = {"n":names[i], "u":units[i], "t":recent[-1], "v":recent[i]}
                    son["main"].append(packet)

            
            if time.time() - self.last_sent > 10:
                try:
                    pre_empt = time.time()
                    resp = requests.post("https://senseborg.ddns.net", json=son)
                    if resp.status_code == 200:
                        self.to_send = []
                        self.last_sent = pre_empt
                        
                except requests.exceptions.ConnectionError as e:
                    print(e)
                    self.to_send = son["main"]
            else:
                self.to_send = son["main"]
