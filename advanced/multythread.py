import os
import threading  # 스레드 import

def foo():
    print('thread id', threading.get_native_id())
    print('process id', os.getpid())

if __name__ == '__main__':
    print('process id', os.getpid())
    thread = threading.Thread(target=foo).start()

def foo():
    print('thread id', threading.get_native_id())
    print('process id', os.getpid())

if __name__ == '__main__':
    print('process id', os.getpid())
    thread1 = threading.Thread(target=foo).start()
    thread2 = threading.Thread(target=foo).start()
    thread3 = threading.Thread(target=foo).start()

def foo():
    print('This is foo')

def bar():
    print('This is bar')

def baz():
    print('This is baz')

if __name__ == '__main__':
    thread1 = threading.Thread(target=foo).start()
    thread2 = threading.Thread(target=bar).start()
    thread3 = threading.Thread(target=baz).start()