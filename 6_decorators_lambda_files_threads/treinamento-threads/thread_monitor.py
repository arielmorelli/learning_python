import thread_runner
import time


class ThreadMonitor(object):
    def __init__(self, number_of_threads):
        self.number_of_threads = number_of_threads
        self.threads_list = []

    def run(self):
        for i in range(self.number_of_threads):
            new_thread = thread_runner.ThreadRunner(i, i + 2)
            new_thread.start()
            self.threads_list.append(new_thread)
            time.sleep(0.7)
        self._wait_threads_to_finish()
        print "Finished"

    def _wait_threads_to_finish(self):
        for t in self.threads_list:
            t.join()


if __name__ == '__main__':
    monitor = ThreadMonitor(2)
    monitor.run()
