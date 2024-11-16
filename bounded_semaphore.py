import threading
import time

def run(n):
    semaphore.acquire()
    time.sleep(1)
    print(f'current thread: {n}')
    semaphore.release()
    
semaphore = threading.BoundedSemaphore(5) # 5個のスレッドの同時処理を許可する

for i in range(22):
    t = threading.Thread(target=run, args=(f't-{i}',))
    t.start()
    
while threading.active_count() != 1:
    pass
else:
    print('All thread closed.')
    
# 一定数のスレッドの同時実行を許可する。一定数以上のスレッドは順番待ちをして、空き次第順次始まる。