# encoding-utf-8
import threading
import time

def loop(i, timeout):
    print(str(i)+' start')
    time.sleep(timeout)
    print(str(i)+' end')

def main():
    threads = []
    timeout = 10
    for i in range(0, 5):
        t = threading.Thread(target=loop, args=(i, timeout))
        threads.append(t)
    print(time.ctime())
    for i in range(0, 5):
        threads[i].start()
    print(time.ctime())
    # for i in range(0, 5):
    #     threads[i].join(timeout=5)
    #     print(time.ctime())
    for i in range(0, 5):
        print(threads[i].is_alive())
    print(time.ctime())


if __name__ == '__main__':
    main()
