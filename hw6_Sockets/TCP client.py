import socket
import time

from hw6_Sockets.PCUtilization import PCUtilization

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("localhost", 9999))
while True:
    PCUtil = PCUtilization()
    print(PCUtil.get_current_state())
    sock.send(PCUtil.get_current_state().encode("utf-8"))
    time.sleep(5)
sock.close()
