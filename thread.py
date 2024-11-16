import threading
import time

def run(n):
    print('task: {} (thread name: {})'.format(n, threading.current_thread().name))
    time.sleep(1)
    print('2s')
    time.sleep(1)
    print('1s')
    time.sleep(1)
    print('0s')
    time.sleep(1)

t1 = threading.Thread(target=run, args=("t1",))
t2 = threading.Thread(target=run, args=("t2", ), name='Thread T2')
t1.start()
t2.start()
t1.join()
t2.join()

print(threading.current_thread().name)

# threading.Threadでスレッドを作成、start()で開始、join()で待機
