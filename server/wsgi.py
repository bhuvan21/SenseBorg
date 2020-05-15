from flask import Flask, jsonify, request
import time
import dataset

app = Flask(__name__)


db = dataset.connect('sqlite:///test.db')
db.create_table("table2")
table = db.load_table("table2")



@app.route('/', methods=["POST"])
def hello_world():
    content = request.args.get("main")
    for i in request.json["main"]:
        print(i)
    print(len(request.json["main"])/9)
    entries = []
    timegroup = request.json["main"][0]["t"]
    entry = []
    for n, sens in enumerate(request.json["main"]):
        
        if timegroup != sens["t"]:

            entries.append(dict(time=timegroup, accX=entry[0], accY=entry[1], accZ=entry[2], gyroX=entry[3], gyroY=entry[4], gyroZ=entry[5], magX=entry[6], magY=entry[7], magZ=entry[8]))
            timegroup = sens["t"]
            entry = [sens["v"]]
        else:
            entry.append(sens["v"])
         
    for entry in entries:
        print(entry)
        table.insert(entry)
    db.commit()
    print([a for a in table.find(time={'>=': time.time()-3})])
    return 'Hello, World!'
if __name__ == "__main__":

    app.run(host='0.0.0.0', ssl_context=("B:\etc\letsencrypt\live\senseborg.ddns.net\winfullchain.pem", "B:\etc\letsencrypt\live\senseborg.ddns.net\winprivkey.pem"))