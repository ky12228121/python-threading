import threading
import time

event = threading.Event()

def lighter():
    count = 0
    event.set()
    while True:
        if 5 < count <= 10:
            event.clear()
            print('赤信号...')
        elif count > 10:
            event.set()
            count = 0
        else:
            print('青信号...')
        
        time.sleep(1)
        count += 1

def car(name):
    while True:
        if event.is_set():
            print(f'[{name}] 前進する...')
            time.sleep(1)
        else:
            print(f'[{name}] 赤信号のため停止')
            event.wait()
            print(f'[{name}] 青信号のため前進開始...')

light = threading.Thread(target=lighter) 
light.start()

car = threading.Thread(target=car, args=('mini',))
car.start()

# ThreadのEventはメインスレッドが他のスレッドをコントロールするためのもの。
# setでflagをTrueに、clearでFalseにする。waitでTrueになるのをブロッキングで待つ