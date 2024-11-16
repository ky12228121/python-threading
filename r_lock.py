import threading

balance = 0

def add_it(n):
    lock.acquire()
    global balance
    balance = balance + n
    return balance

def sub_it(n):
    lock.acquire()
    global balance
    balance = balance - n
    return balance

def change_it(n):
    lock.acquire()
    global balance
    balance = add_it(n)
    balance = sub_it(n)
    lock.release()
    
def run_thread(n):
    for i in range(1_000):
        change_it(n)
        
lock = threading.RLock()

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)

# RLockを使うと、再帰的にロックを解放できる