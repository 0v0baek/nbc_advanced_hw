import os
from multiprocessing import Process  #프로세스 import


# 프로세스 만들기
print('hello os')
print(f'my pid is {os.getpid()}')

def foo():
    print(f'child process : {os.getpid()}')
    print(f'my parent is : {os.getppid()}')

# 처음부터 실행되는 듯 !
if __name__ == '__main__':
    print(f'parent process : {os.getpid()}')
    child = Process(target=foo).start()

def foo():
    print('hello, os')
 
if __name__ == '__main__':
    child1 = Process(target=foo).start()
    child2 = Process(target=foo).start()
    child3 = Process(target=foo).start()

def foo():
    print('This is foo')

def bar():
    print('This is bar')

def baz():
    print('This is baz')
  
if __name__ == '__main__':
    child1 = Process(target=foo).start()
    child2 = Process(target=bar).start()
    child3 = Process(target=baz).start()