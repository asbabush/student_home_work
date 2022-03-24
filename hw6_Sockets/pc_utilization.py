import time

import psutil


class PCUtilization:
    """Class for collect PCU and Memory utilization every 5 second"""

    def __init__(self):
        self.cpu_util = None
        self.memory_util = None
        self.time = None
        self.stop = False

    def start_collect(self):
        with open("Local_log.txt", "w") as f:
            while True:
                if self.stop:
                    break
                f.write(self.get_current_state() + "\n")
                print(self.get_current_state())
                time.sleep(1)

    def get_current_state(self):
        self.cpu_util = psutil.cpu_percent(interval=1)
        self.memory_util = psutil.virtual_memory().percent
        self.time = time.strftime("%d %b %Y %H:%M", time.localtime())
        return (
            self.time
            + "  CPU utilization:"
            + str(self.cpu_util)
            + "%  Memory utilization:"
            + str(self.memory_util)
            + "%"
        )

    def cleanup(self):
        self.cpu_util = None
        self.memory_util = None
        self.time = None

    def stop_collect(self):
        self.stop = True
        self.cleanup()
