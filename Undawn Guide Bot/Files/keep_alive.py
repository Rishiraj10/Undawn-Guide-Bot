from flask import Flask
from threading import Thread 
app = Flask('') 
@app.route('/')
def main():
    return '<meta http-equiv="refresh" content="0; URL=https://mikeykunctx.blogspot.com/2022/10/lifeafter-map-guide.html"/>'
def run():
    app.run(host="0.0.0.0", port=8080)

def keep_alive():
    server = Thread(target=run)
    server.start()
