from pythonds.basic.queue import Queue


q=Queue()

q.enqueue(5)
q.enqueue(7)

print q.size()

print q.dequeue()

print q.size()
