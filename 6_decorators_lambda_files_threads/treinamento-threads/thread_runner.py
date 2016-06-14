import threading
import time


class ThreadRunner(threading.Thread):

    def __init__(self, thread_id, divisor):
        self.thread_id = thread_id
        self.divisor = divisor
        threading.Thread.__init__(self)

    def run(self):
        for i in range(1, 100):
            if i % self.divisor == 0:
                print "=> Thread {}: {}".format(self.thread_id, i)
            time.sleep(0.2)
