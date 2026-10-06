SIZE = 4
queue = [None] * SIZE
front = 0
rear = -1

def enqueue(value):
    global rear
    if rear == SIZE - 1:
        print("Overflow! (rear cannot move further, even if front has spaced)")
        return 
    rear = rear + 1
    queue[rear] = value
    print(queue, "front:", front, "rear:", rear)

def dequeue():
        global front
        queue[front] = None
        front = front + 1
        print(queue, "front:", front, "rear:", rear)

enqueue(46)
enqueue(56)
enqueue(66)
enqueue(76)
dequeue()
dequeue()
dequeue()