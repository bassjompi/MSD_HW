from flask import Flask, render_template
import psutil
import datetime
import netifaces as ni


application = Flask(__name__)

@application.route('/')
def systeminfo():
    usage=str("THE CPU USAGE IS {}%".format(psutil.cpu_percent())+"\n")
    now = datetime.datetime.now()
    tiempo = str(now.strftime("%Y-%m-%d %H:%M:%S"))
    ni.ifaddresses('eth1')
    ip = ni.ifaddresses('eth1')[ni.AF_INET][0]['addr']

    numbers = list(ip)
    odd = []
    even = []
    for i in numbers:
        if i != '.':
            cifra = int(i)
            if cifra % 2 == 0:
                even.append(i)
            else:
                odd.append(i)

    return render_template('index.html', title='MSD_JUAN_PABLO', time=tiempo, usage=usage, address=ip, even=even, odd=odd)


def main():
    app.run(host='0.0.0.0',
            port=80,
            threaded=True,
            debug=True
            )


if __name__ == '__main__':
    main()
