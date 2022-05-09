import time
import threading

run = True
def thread_run():
    if run:
        print('Hello, world')
        threading.Timer(1, thread_run).start()


thread_run()
print('This is main')
time.sleep(10)
print('10 sec ended')
run = False
time.sleep(10)
print('another 10 sec ended')


############################Canel()#########################################
# def hello():
#     print("hello, world")
#
# t = threading.Timer(10.0, hello)
# t.start()  # after 10 seconds, "hello, world" will be printed
# time.sleep(5)
# print('5 sec ended')
# t.cancel()
