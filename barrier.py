import threading

num = 4

def start_game():
    print(f'{num}人になったためゲーム開始')
    
lock = threading.Lock()
barrier = threading.Barrier(num, action=start_game)

class Player(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def run(self):
        try:
            if not barrier.broken:
                print(f'{self.name}さんが参加しました')
                barrier.wait(2)
        except threading.BrokenBarrierError:
            print(f'ゲームを開始できないため、{self.name}が退出しました')

players = []
for i in range(10):
    p = Player(name=f'player{i}')
    players.append(p)

for p in players:
    p.start()

# 指定された数のスレッドがバリアを通ったらまとめて実行される
# waitを呼び出すと、指定数分のwaitが呼び出されるまで待機するようになる。
# 指定数分waitされると、actionが呼び出されてwaitしていたスレッドがwait状態から解放される
