#!/bin/python

from flask import Flask, render_template
import socket
import psutil
import datetime

application = Flask(__name__)

@application.route('/')
def cpu():
    usage=str("THE CPU USAGE IS {} %".format(psutil.cpu_percent())+"\n")
    now = datetime.datetime.now()
    tiempo = str(now.strftime("%Y-%m-%d %H:%M:%S"))
    ip=(socket.gethostbyname(socket.gethostname()))

    return render_template('index.html', title='MSD', time=tiempo, usage=usage, address=ip)


def main():
    application.run(host='0.0.0.0',
            port=5000,
            threaded=True,
            debug=True
            )


if __name__ == '__main__':
    main()
