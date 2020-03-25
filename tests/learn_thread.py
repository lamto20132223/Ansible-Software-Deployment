import logging
import threading
import time

def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: finishing", name)
    return 3

if __name__ == "__main__":

    a =[4,6,7,8,8]
    b=[]
    for i , nb in enumerate(a):
        print(i,nb)
        b.append(nb+i)

    print(b)

    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    logging.info("Main    : before creating thread")
    x = threading.Thread(target=thread_function, args=(1,))
    x.setDaemon(True) #dieu nay lam cho thread bi kill khi ham main cham den end code
    logging.info("Main    : before running thread")
    x.start()
    logging.info("Main    : wait for the thread to finish")
    x.join()  # su dung join de giu cho tien trinh ben duoi doi den khi thread duoc hoan thanh  cu the ket qua se chay
    # thread finishing truoc khi chay all done
    logging.info("Main    : all done")

    #time.sleep(3)
    logging.info("Done sleep")
    print(x)