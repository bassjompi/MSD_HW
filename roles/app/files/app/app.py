from flask import Flask, render_template
import psutil
import time
import socket
import fcntl
import struct

application = Flask(__name__)

@application.route('/')
def systeminfo():

    usage=str("CPU USAGE  {}%".format(psutil.cpu_percent())+"\n")
    tiempo= time.strftime('%H:%M:%S %Z on %b %d, %Y')

    def get_ip_address(ifname):                                         ## function to obtain ip of a certain device
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        return socket.inet_ntoa(fcntl.ioctl(
            s.fileno(),
            0x8915,                                                      # SIOCGIFADDR
            struct.pack('256s', ifname[:15])
        )[20:24])

    ip= get_ip_address('eth1')
    numbers = list(ip)                                                  ##creates a list with the ip address

    odd = []
    even = []
    for i in numbers:                                                    ##check if numbers are odd or even
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