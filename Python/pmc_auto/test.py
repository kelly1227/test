# def outer_func():
#     loc_list = []
#     def inner_func(name):
#         loc_list.append(len(loc_list) + 1)
#         print('%s loc_list = %s' %(name, loc_list))
#     return inner_func
#
# clo_func_0 = outer_func()
# clo_func_0('clo_func_0')
# clo_func_0('clo_func_0')
# clo_func_0('clo_func_0')
#
# clo_func_1 = outer_func()
# clo_func_1('clo_func_1')
# clo_func_0('clo_func_0')
# clo_func_1('clo_func_1')



# def my_func(*args):
#     fs = []
#     for i in range(3):
#         func = lambda _i = i : _i * _i
#         fs.append(func)
#         print("index=",i,len(fs))
#     return fs
# fs1, fs2, fs3 = my_func()
# print(fs1())
# print(fs2())
# print(fs3())

# def func_dec(func):
#     def wrapper(*args):
#         print(args)
#         if len(args) >= 2:
#             func(*args)
#         else:
#             print('Error! Arguments = %s'%list(args))
#     return wrapper
#
# @func_dec
# def add_sum(*args):
#     print(sum(args))
#
# # add_sum = func_dec(add_sum)
# args = range(1,6)
# add_sum(*args)
# import functools
#
#
# def counter(cls):
#     obj_list = []
#     @functools.wraps(cls)
#     def wrapper(*args, **kwargs):
#         new_obj = cls(*args, **kwargs)
#         obj_list.append(new_obj)
#         print("class:%s'object number is %d" % (cls.__name__, len(obj_list)))
#         return new_obj
#     return wrapper
#
# @counter
# class my_cls(object):
#     STATIC_MEM = 'This is a static member of my_cls'
#     def __init__(self, *args, **kwargs):
#         print(self, args, kwargs)
#         print(my_cls)
#         print(my_cls.STATIC_MEM)
#
# args = range(1,6)
# kwargs = range(1,3)
# my_cls(args,kwargs)
# def outer_func():
#     loc_var = "local variable"
#     def inner_func():
#         return loc_var
#     return inner_func
#
# import dis
#
# dis.dis(outer_func)
# clo_func = outer_func()
# print(clo_func())
# dis.dis(clo_func)

#进程  VS 线程 Thread  Threading

import threading
import time

# def tstart(arg):
#     time.sleep(0.5)
#     print("%s running...."%arg)
#
# if __name__ == '__main__':
#     t1 = threading.Thread(target=tstart("123"),name="A123")
#     t2 = threading.Thread()
#     t1.start()
#     t2.start()
#     print("this is main funcation",t1.name)

# class MyThread(threading.Thread):
#     def __init__(self,thread_name):
#         # call base __init__
#         super(MyThread,self).__init__(name=thread_name)
#         self._thread_name = thread_name
#     def run(self):
#         time.sleep(0.5)
#         print("This is running %s " % self._thread_name)
#
# if __name__ == '__main__':
#     mythread = MyThread("")
#     mythread.start()
#     print(mythread.name)
#进程 创建
# from multiprocessing import Process
# import os,time
#
# class MyProcess(Process):
#     def __init__(self,p_name,target=None):
#         super(MyProcess,self).__init__(name=p_name,target=target,args=(p_name,))
#
#     def run(self):
#         print("MyProcess name %s,pid: %s"%(self.name,os.getpid()))
#
# def pstart(name):
#     time.sleep(0.5)
#     print("进程开始了。名称为 %s pid:%s"%(name,os.getpid()))
#
# if __name__ == '__main__':
#     subpro = MyProcess(p_name="ABC",target=pstart)
#     # subpro = Process(target=pstart,args=('subprocess',))
#     subpro.start()
#     subpro.join()
#     print("subprocess pid:%s"%subpro.pid)
#     print("current process pid:%s"% os.getpid())

# import subprocess
#
# if __name__ == '__main__':
#
#     res = subprocess.Popen(["ping","www.baidu.com"],stdout=subprocess.PIPE)
#     # print(res)
#
#     lines = res.stdout.readlines()
#     # print(lines)
#
#     [print(line.decode('gbk')) for line in lines]




# def tstart(arg):
#     var = 0
#     for i in range(100000000):
#         var += 1
#
# if __name__ == '__main__':
#     t1 = threading.Thread(target=tstart, args=('This is thread 1',))
#     t2 = threading.Thread(target=tstart, args=('This is thread 2',))
#     start_time = time.time()
#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()
#     print("Two thread cost time: %s" % (time.time() - start_time))
#     start_time = time.time()
#     tstart("This is thread 0")
#     print("Main thread cost time: %s" % (time.time() - start_time))

# from multiprocessing import Process
# def pstart(arg):
#     var = 0
#     for i in range(100000000):
#         var += 1
#
# if __name__ == '__main__':
#     p1 = Process(target = pstart, args = ("1", ))
#     p2 = Process(target = pstart, args = ("2", ))
#     start_time = time.time()
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()
#     print("Two process cost time: %s" % (time.time() - start_time))
#     start_time = time.time()
#     pstart("0")
#     print("Current process cost time: %s" % (time.time() - start_time))

# share_data = 0
# res = []
# lock = threading.Lock()
# def tstart(arg):
#     time.sleep(0.1)
#     global share_data
#     # if lock.acquire():  # step 2: 获取互斥锁，否则阻塞当前线程
#     #     share_data += 1
#     # lock.release()  # step 3: 释放互斥锁
#     if lock.acquire():
#         for i in range(200000):
#             res.append((arg, share_data))
#             share_data += 1
#     lock.release()
#
# if __name__ == '__main__':
#     t1 = threading.Thread(target = tstart, args = ('1',))
#     t2 = threading.Thread(target = tstart, args = ('2',))
#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()
#     print(res, len(res))
#     print('share_data result:', share_data)
#     # tlst = list()
#     # for i in range(10):
#     #     t = threading.Thread(target=tstart, args=('',))
#     #     tlst.append(t)
#     # for t in tlst:
#     #     t.start()
#     # tlst[2].join()
#     # print("This is main function at：%s" % time.time())
#     # print('share_data result:', share_data)


# import threading
# import time
# rlock = threading.RLock()     # step 1: 创建重入锁
# share_data = 0
#
# def check_data():
#     global share_datashare_data
#     if rlock.acquire():
#         if share_data > 10:
#             share_data = 0
#     rlock.release()
#
# def tstart(arg):
#     time.sleep(0.1)
#     global share_data
#     if rlock.acquire():       # step 2: 获取重入锁，否则阻塞当前线程
#         check_data()
#         share_data += 1
#     rlock.release()          # step 3: 释放重入锁
#
# if __name__ == '__main__':
#     t1 = threading.Thread(target = tstart, args = ('',))
#     t1.start()
#     t1.join()
#     print("This is main function at：%s" % time.time())
#     print('share_data result:', share_data)
#
# import random
# def get_wait_time():
#     return random.random()/5.0
#
# # 资源数0
# S = threading.Semaphore(0)
# def consumer(name):
#     S.acquire()
#     time.sleep(get_wait_time())
#     print(name)
#
# def producer(name):
#     # time.sleep(0.1)
#     time.sleep(get_wait_time())
#     print(name)
#     S.release()
#
# if __name__ == "__main__":
#     print(S)
#     for i in range(5, 10):
#         c = threading.Thread(target=consumer, args=("consumer:%s"%i, ))
#         c.start()
#     for i in range(5):
#         p = threading.Thread(target=producer, args=("producer:%s"%i, ))
#         p.start()
#     time.sleep(2)

# share_data, max_len = '#', 6
# cond = threading.Condition()
#
# def get_time():
#     return time.strftime("%Y-%m-%d %H:%M:%S")
#
# def show_start_info(tname):
#     print('%s start at: %s' %(tname, get_time()))
#
# def show_acquire_info(tname):
#     print('%s acquire at: %s' % (tname, time.time()))
#
# def show_add_once_res(tname):
#     print('%s add: %s at: %s' % (tname, share_data, time.time()))
#
# def show_end_info(tname):
#     print('End %s with: %s at: %s' % (tname, share_data, time.time()))
#
# def show_wait_info(tname):
#     print('%s wait at: %s' % (tname, time.time()))
#
#
# def addA(tname):
#     show_start_info(tname)
#     cond.acquire()
#     time.sleep(1)
#     show_acquire_info(tname)
#     global share_data
#     while len(share_data) <= max_len:
#         if share_data[-1] != 'A':
#             share_data += 'A'
#             time.sleep(1)
#             cond.notify()
#             show_add_once_res(tname)
#         else:
#             # show_wait_info(tname)
#             cond.wait()
#     cond.release()
#     show_end_info(tname)
#
# def addB(tname):
#     show_start_info(tname)
#     cond.acquire()
#     time.sleep(1)
#     show_acquire_info(tname)
#     global share_data
#     while len(share_data) <= max_len:
#         if share_data[-1] != 'B':
#             share_data += 'B'
#             time.sleep(1)
#             cond.notify()
#             show_add_once_res(tname)
#         else:
#             # show_wait_info(tname)
#             cond.wait()
#     cond.release()
#     show_end_info(tname)
#
# if __name__ == "__main__":
#     t1 = threading.Thread(target=addA, args=("Thread 1", ))
#     t2 = threading.Thread(target=addB, args=("Thread 2", ))
#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()
#     print("share_data:", share_data)
# import random
# import operator
# import filecmp
# E = threading.Event()
# E.clear()
# res1, res2, cnt, lst = 0, 0, 3, ("player2", 'both', 'player1')
#
# def show_round_res():
#     if operator.eq(res1,res2):
#         print ("Stop! judging...  win!", lst[1])
#     elif operator.lt(res1,res2):
#         print("Stop! judging...  win!", lst[0])
#     else:
#         print("Stop! judging...  win!", lst[2])
#
# def judge():
#     global cnt
#     while cnt > 0:
#         print('start game!')
#         E.set()
#         time.sleep(1)
#         E.clear()
#         show_round_res()
#         time.sleep(1)
#         cnt -= 1
#     print("game over by judge!")
#
# def player1():
#     global res1
#     while cnt > 0:
#         if E.is_set():
#             res1 = random.randint(1, 6)
#             print("player1 get %d" % res1)
#             time.sleep(1.5)
#             E.wait()
#     print("player1 quit!")
#
# def player2():
#     global res2
#     while cnt > 0:
#         if E.is_set():
#             res2 = random.randint(1, 6)
#             print("player2 get %d" % res2)
#             time.sleep(1.5)
#             E.wait()
#     print("player2 quit!")
#
#
# if __name__ == "__main__":
#     t1 = threading.Thread(target=judge, args=( ))
#     t2 = threading.Thread(target=player1, args=( ))
#     t3 = threading.Thread(target=player2, args=( ))
#     t1.start()
#     t2.start()
#     t3.start()
#     t1.join()
#     E.set()

# from multiprocessing import Process,Pipe
#
# def pstart(pname,conn):
#     conn.send("Data@subprocess")
#     print("pstart",conn.recv())  # Data@parentprocess
#
# if __name__ == '__main__':
#     conn1, conn2 = Pipe(True)
#     sub_proc = Process(target=pstart, args=('subprocess', conn2,))
#     sub_proc.start()
#     print("main :",conn1.recv())
#     conn1.send("Data@parentprocess")
#     sub_proc.join()

# from multiprocessing import Process, Queue
# import time
#
# def producer(que):
#     for product in ('Orange', 'Apple', 'Pear',''):
#         print('put product: %s to queue' % product)
#         que.put(product)
#         time.sleep(0.5)
#         res = que.get()
#         print('consumer result: %s' % res)
#
# def consumer(que):
#     while True:
#         product = que.get()
#         print(type(product))
#         print('get product:%s from queue' % product)
#         que.put('suc!')
#         time.sleep(0.5)
#         if not product:
#             break
#
# if __name__ == '__main__':
#     que = Queue(1)
#     p = Process(target=producer, args=(que,))
#     c = Process(target=consumer, args=(que,))
#     p.start()
#     c.start()
#     p.join()
#     c.join()

from multiprocessing import Process
import mmap
import contextlib
import time

def writer():
    with contextlib.closing(mmap.mmap(-1, 1024, tagname='cnblogs', access=mmap.ACCESS_WRITE)) as mem:
        for share_data in ("Hello", "Alpha_Panda"):
            mem.seek(0)
            print('Write data:== %s == to share memory!' % share_data)
            mem.write(str.encode(share_data))
            mem.flush()
            time.sleep(0.5)

def reader():
    while True:
        invalid_byte, empty_byte = str.encode('\x00'), str.encode('')
        with contextlib.closing(mmap.mmap(-1, 1024, tagname='cnblogs', access=mmap.ACCESS_READ)) as mem:
            share_data = mem.read(1024).replace(invalid_byte, empty_byte)
            if not share_data:
                """ 当共享内存没有有效数据时结束reader """
                break
            print("Get data:== %s == from share memory!" % share_data.decode())
        time.sleep(0.5)


if __name__ == '__main__':
    p_reader = Process(target=reader, args=())
    p_writer = Process(target=writer, args=())
    p_writer.start()
    p_reader.start()
    p_writer.join()
    p_reader.join()