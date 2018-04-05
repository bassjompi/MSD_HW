from flask import render_template
from app import app
import socket
import psutil
import datetime

@app.route('/index')
def cpu():
    usage=str("THE CPU USAGE IS {} %".format(psutil.cpu_percent())+"\n")
    now = datetime.datetime.now()
    tiempo = str(now.strftime("%Y-%m-%d %H:%M:%S"))
    ip=(socket.gethostbyname(socket.gethostname()))

    return render_template('index.html', title='MSD', time=tiempo, usage=usage, address=ip)

