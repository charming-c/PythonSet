import time
import threading


# 创建一个线程子类
class MyThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print("开始线程：" + self.name)
        moyu_time(self.name, self.counter, 2)
        print("结束线程：" + self.name)


def moyu_time(name, counter, delay):
    while counter:
        time.sleep(delay)
        print("%s 开始摸鱼 %s" % (name, time.strftime(
            "%Y-%m-%d %H:%M:%S", time.localtime())))
        counter -= 1


thread1 = MyThread(1, "xiaoming", 10)
thread2 = MyThread(2, "xiaohong", 10)

# 开启新线程
thread1.start()
thread2.start()

# 等待至线程终止
thread1.join()
thread2.join()

print("退出主线程")
