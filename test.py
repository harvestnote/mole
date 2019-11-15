import queue
import threading
import time
import os
import _thread


arr = []
lock =threading.Lock()


def put_data(arr):
    lock.acquire()
    for i in range(101):
        arr.append(i)

        while len(arr) > 10:
             threading.Condition.wait()
    lock.release()







def show_data(arr):
    lock.acquire()
    for i in arr:
        print(i)
    arr.clear()
    lock.release()




if __name__ == "__main__":
    t1 = threading.Thread(target=put_data, args=(arr,))
    t2 = threading.Thread(target=show_data, args=(arr,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()


    print("end....")