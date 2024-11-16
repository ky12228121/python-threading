import threading
import time

def run(n):
    print('task: {}'.format(n))
    time.sleep(0.5)

for i in range(1,4):
    t = threading.Thread(target=run, args=('t{}'.format(i),))
    t.start()
    
time.sleep(1)
print(threading.active_count())

# active_countで実行中のスレッド数を取得できる(メインスレッドもカウントされる)