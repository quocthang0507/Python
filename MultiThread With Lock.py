# https://www.geeksforgeeks.org/multithreading-in-python-set-2-synchronization/
import threading

x = 0


def increment():
    global x
    x += 1


# no other thread can access the critical section (here, increment function) until the lock is released using lock.release() method.
def thread_task(lock):
    for _ in range(1000000):
        # When invoked with the blocking argument set to False, thread execution is not blocked
        lock.acquire()
        increment()
        # When the lock is locked, reset it to unlocked
        lock.release()


def main_task():
    global x
    x = 0

    # creating a lock
    lock = threading.Lock()

    # creating threads
    t1 = threading.Thread(target=thread_task, args=(lock,))
    t2 = threading.Thread(target=thread_task, args=(lock,))

    # starting threads
    t1.start()
    t2.start()

    # wait until threads finish their job
    t1.join()
    t2.join()


if __name__ == "__main__":
    for i in range(10):
        main_task()
        print('Iteration {0}: x = {1}'.format(i, x))
