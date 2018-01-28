import thread
import time

def Threadfun(string, sleeptime, lock, *args):
    while(True):
        lock.acquire()
        print 'Enter_{0}\r\n'.format(string)
        time.sleep(sleeptime)
        print 'Leave_{0}\r\n'.format(string)
        lock.release()

if __name__ == "__main__":
    lock = thread.allocate_lock() 
    thread.start_new_thread(Threadfun, ("ThreadFun1", 2, lock))
    thread.start_new_thread(Threadfun, ("ThreadFun2", 2, lock))

    while (True):
        pass