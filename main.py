import time

from timeloop import Timeloop
from datetime import timedelta
import threading

class MyThread(threading.Thread):
    pass


def fibonacci(n):
    # First Fibonacci number is 0
    if n == 1:
        return 0
    # Second Fibonacci number is 1
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)


def wait_until():
    tl = Timeloop()

    thread = MyThread()

    @tl.job(interval=timedelta(seconds=0))
    def sample_job_every_2s():
        fibonacci(20)
        if True:
            print
            "2s job current time : {}".format(time.ctime())

    @tl.job(interval=timedelta(seconds=0))
    def sample_job_every_5s():
        fibonacci(1)
        print
        "5s job current time : {}".format(time.ctime())

    @tl.job(interval=timedelta(seconds=0))
    def sample_job_every_10s():
        fibonacci(20)
        print
        "10s job current time : {}".format(time.ctime())

    tl.start()
    while thread.is_alive():
        print('+++do something')
    tl.stop()
    return True