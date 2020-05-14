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
        self.last_sent = time.time()

    def mainloop(self):
        recent = None
        while True:
            try:
                recent = self.queue.get(block=False)
            except queue.Empty:
                if recent is not None:
                    break
        
        json = {"main": self.to_send}
        names = ["accX", "accY", "accZ", "gyroX", "gyroY", "gyroZ", "magX", "magY", "magZ"]
        units = ["ms^-2"*3] + ["degs^-2"*3] + ["T"*3]
        for i in range(9):
            json["main"].append({"n":names[i], "u":units[i], "t":recent[-1], "v":recent[i]})
        
        self.to_send.append(json["main"])

        if time.time() - self.last_sent > 3:
            resp = requests.post("http://senseborg.ddns.net", json)
            if resp.status_code == 200:
                self.to_send = []
                self.last_sent = time.time()