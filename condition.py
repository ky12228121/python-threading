import threading
import time
from random import randint
from collections import deque

class Producer(threading.Thread):
    def run(self):
        global stocks
        while True:
            if lock_con.acquire():
                products = [randint(0,100) for _ in range(5)]
                stocks.extend(products)
                print(f'生産者{self.name}は{stocks}を生産した。')
                lock_con.notify()
                lock_con.release()
            time.sleep(3)

class Consumer(threading.Thread):
    def run(self):
        global stocks
        while True:
            lock_con.acquire()
            if len(stocks) == 0:
                lock_con.wait()
            print(f'お客様{self.name}は{stocks.popleft()}を買った。在庫: {stocks}')
            lock_con.release()
            time.sleep(0.5)
            
stocks = deque()
lock_con = threading.Condition()
p = Producer()
c = Consumer()
p.start()
c.start()

# Conditionを使うと条件判定でスレッド制御ができる。
# Lockと同様にLockを取得して使う。
# waitで通知されるまでスレッドをハングアップする。
# notifyでハングアップされたスレッドに通知する。