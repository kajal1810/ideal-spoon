#create thread using threading module

import threading
import time

exitFlag = 0

class myThread (threading.Thread): #create subclass of Thread class
   def __init__(self, threadID, name, counter): #override init method to add other arguments
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter
   def run(self): #override run to implement what the thread should do when started
      print ("Starting " + self.name)
      print_time(self.name, self.counter, 5)
      print ("Exiting " + self.name)

def print_time(threadName, delay, counter):
   while counter:
      if exitFlag:
         threadName.exit()
      time.sleep(delay)
      print ("%s: %s" % (threadName, time.ctime(time.time()))) #display time
      counter -= 1

# Create new threads
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# Start new Threads
thread1.start()
thread2.start()
thread1.join()#waits to terminate thread
thread2.join()
print ("Exiting Main Thread")
