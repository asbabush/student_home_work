import socket
import threading
import time

import keyboard
from pc_utilization import PCUtilization


def connection_server():
    pc_util = PCUtilization()
    print("Connected")
    while True:
        print(pc_util.get_current_state())
        sock.send(pc_util.get_current_state().encode("utf-8"))
        time.sleep(5)


if __name__ == "__main__":
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(("localhost", 9999))
        thread_connection_server = threading.Thread(target=connection_server)
        thread_connection_server.daemon = True
        thread_connection_server.start()

        while True:
            if keyboard.is_pressed("q"):
                print('Stop send and teardown client, because you pushed "q"')
                break
        sock.close()
        print("Disconnected")
    except Exception as e:
        print(e)
