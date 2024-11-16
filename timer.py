import threading

def hello():
    print('hello, world.')

t = threading.Timer(1, hello)
t.start()

# Timerを使うと時間でスレッドを制御できる