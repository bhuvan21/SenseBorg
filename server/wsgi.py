from flask import Flask, jsonify, request
import time
import dataset
import threading
import queue

app = Flask(__name__)


q = queue.Queue()

def mainloop():
    db = dataset.connect('sqlite:///test.db')
    db.create_table("table2")
    table = db.load_table("table2")
    
    
    while 1:
        resps = []
        
        while 1:
            try:
                resp = None

                resp = q.get(block=False)

                resps.append(resp)
                
            except queue.Empty:
                if resps != []:
                    break

        print("RESPS", len(resps))
        s= time.time()
        rows = []
        for r in resps:
            for k, entry in r.items():
                e = dict(time=k, accX=entry["accX"], accY=entry["accY"], accZ=entry["accZ"], gyroX=entry["gyroX"], gyroY=entry["gyroY"], gyroZ=entry["gyroZ"], magX=entry["magX"], magY=entry["magY"], magZ=entry["magZ"])
                rows.append(e)
        table.insert_many(rows)
        
        db.commit()
        print(time.time()-s)
        try:
            print([a for a in table.find(time={'>=': time.time()-3})][-1])
        except IndexError:
            pass


@app.route('/', methods=["POST"])
def hello_world():
    content = request.args.get("main")
    print(len(request.json["main"])/9)
    entries = {}

    entry = []
    for n, sens in enumerate(request.json["main"]):
        if sens["t"] not in entries.keys():
            entries[sens["t"]] = {}
        entries[sens["t"]][sens["n"]] = sens["v"]
        
    '''
    for n, sens in enumerate(request.json["main"]):
        
        if timegroup != sens["t"]:

            entries.append(dict(time=timegroup, accX=entry[0], accY=entry[1], accZ=entry[2], gyroX=entry[3], gyroY=entry[4], gyroZ=entry[5], magX=entry[6], magY=entry[7], magZ=entry[8]))
            timegroup = sens["t"]
            entry = [sens["v"]]
        else:
            entry.append(sens["v"])
    '''

    q.put(entries, block=False)
    
    return 'Hello, World!'
if __name__ == "__main__":
    t = threading.Thread(target=mainloop)
    t.setDaemon(True)
    t.start()
    app.run(host='0.0.0.0', ssl_context=("B:\etc\letsencrypt\live\senseborg.ddns.net\winfullchain.pem", "B:\etc\letsencrypt\live\senseborg.ddns.net\winprivkey.pem"))
    