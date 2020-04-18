import threading
import time


class TestClass(threading.Thread):
    def __init__(self):
        super(TestClass, self).__init__()
        self.x = False
        self.name = "asdf"
        self.lock = threading.Condition()

    def run(self):
        print('started')
        with self.lock:
            self.lock.wait()
        print('ok doing')

    def meth(self):
        print(f'{self.name} starting ride')
        time.sleep(2)
        print(f'{self.name} finished ride')


y = TestClass()
y.start()
time.sleep(5)
y.x = True
with y.lock:
    y.lock.notify()
print('done')
