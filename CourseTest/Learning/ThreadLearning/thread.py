import time
import threading
import concurrent.futures


def moyu_time(name, delay, counter):
    while counter:
        time.sleep(delay)
        print("%s charming %s" %
              (name, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
        counter -= 1


if __name__ == "__main__":
    pool = concurrent.futures.ThreadPoolExecutor(20)
    for i in range(1, 5):
        pool.submit(moyu_time("chamrming" + str(i), 1, 10))
