# 使用生成器模拟生产者消费者
import time

message_que = [i for i in range(1000)]
def producer(*g):
    for msg in message_que:
        print("producing: {}".format(msg))
        for _g in g:
            c = _g.active(msg)
            print("producer: customer {}".format(c))


class Customer:
    def __init__(self, i, gen):
        self.id = i
        self.gen = gen
        self.active(None)

    def active(self, val):
        return self.gen.send(val)


def consume(i):
    while True:
        n = yield '{} ok'.format(i)
        print("customer {} :get {}".format(i, n))


start_time = time.time()
g = []
for i in range(1, 6):
    g.append(Customer(i, consume(i)))
producer(*g)
print("cost: {}s".format(time.time() - start_time))