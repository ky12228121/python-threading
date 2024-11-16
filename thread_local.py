import threading
import time

def print_local_x():
    x = local.x
    print(f'{threading.current_thread().name}のx: {x}')

def set_thread_local_x(x):
    local.x = x
    print(f'{threading.current_thread().name}のxを設定しました')
    time.sleep(1)
    print_local_x()

local = threading.local()
t1 = threading.Thread(target=set_thread_local_x, args=(5,), name="Thread-A")
t2 = threading.Thread(target=set_thread_local_x, args=(8,), name="Thread-B")
t1.start()
t2.start()
t1.join()
t2.join()


# thread_localは、スレッド内のグローバル変数となる
# 他のスレッドからはアクセスできないためスレッドセーフで、かつスレッド内のどの関数からもアクセスできるグローバル性がある。