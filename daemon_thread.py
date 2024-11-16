import threading
import time

def run(n):
    print(f'task: {n}')
    time.sleep(1)
    print('3s')
    time.sleep(1)
    print('2s')
    time.sleep(1)
    print('1s')

for i in range(1, 4):
    t = threading.Thread(target=run, args=(f't{i}',))
    t.setDaemon(True)
    t.start()
    
time.sleep(1.5)
print(f"thread number: {threading.active_count()}")

# daemon threadはメインスレッドが終了したら終了する