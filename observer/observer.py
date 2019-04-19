import threading
import time
import pdb

class Downloader(threading.Thread):

    def run(self):
        print("downloading")
        for i in range(1,5):
            self.i=i
            time.sleep(2)
        print("hi")
        return "hello world"

class Worker(threading.Thread):
    def run(self):
        for i in range(1,5):
            print("worker running: %i(%i)"%(i,t.i))
            time.sleep(1)
            t.join()
            print("done")

t=Downloader()
t.start()

time.sleep(1)

t1=Worker()
t1.start()

t2=Worker()
t2.start()

t3=Worker()
t3.start()



"""
Output:

downloading
worker running: 1(1)
worker running: 1(1)
worker running: 1(1)
hi
done
done
worker running: 2(4)
worker running: 2(4)
done
worker running: 2(4)
done
worker running: 3(4)
done
worker running: 3(4)
done
worker running: 3(4)
done
worker running: 4(4)
done
done
worker running: 4(4)
worker running: 4(4)
done
done
done
"""