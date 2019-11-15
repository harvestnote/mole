import queue
import threading

q = queue.Queue()

con = threading.Condition()


def put_date(q):
        if con.acquire():
            for i in range(101):
                q.put(i)
                if q.qsize() == 10:
                    print("qsize :" + str(q.qsize()))


                    con.wait(1)
                    con.notify(1)



def show_data(q):
        con.acquire()
        if q.qsize() ==10:
            while not q.empty():
                print(q.get())
            print("qsize :" + str(q.qsize()))

            con.wait(1)
            con.notify(1)



if __name__ == "__main__":

    t1 = threading.Thread(target=put_date, args=(q,))
    t2=  threading.Thread(target=show_data,args=(q,))

    t1.start()
    t2.start()
