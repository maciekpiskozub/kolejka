from Queue import Queue

queue = Queue(10)


for i in range(10):
    number = int(input("Podaj liczbe:"))
    queue.add(number)

for i in range(10):
    print(queue.remove())

