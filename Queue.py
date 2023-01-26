from QueueEmptyException import QueueEmptyException
from QueueFullException import QueueFullException

class Queue:
    def __init__(self, max_size=5):
        '''Initialize the queue with a max size of 5
        '''
        self.head = -1
        self.tail = -1
        self.max_size = max_size
        self.queue_size = 0
        self.queue_items = [None] * self.max_size


    def is_empty(self):
        '''
        Returns True if the queue is empty, False otherwise
        '''
        return self.queue_size == 0

    def is_full(self):
        '''
        Returns True if the queue is full, False otherwise      
        '''
        return self.queue_size == self.max_size

    def enqueue(self, item):
        '''
        Adds an item to the queue
        Raises QueueFullException if the queue is full
        '''
        if self.is_full():
            raise QueueFullException("Queue is Full")
        else:
            self.tail = (self.tail + 1) % self.max_size
            self.queue_items[self.tail] = item
            self.queue_size += 1

    def dequeue(self):
        '''
        Removes an item from the queue
        Raises QueueEmptyException if the queue is empty
        '''
        item_str = ""
        if self.is_empty():
            raise QueueEmptyException("Queue is Empty")
        else:
            self.head = (self.head + 1) % self.max_size
            item_str = self.queue_items[self.head]
            self.queue_size -= 1
        return item_str
    
    def peek(self):
        '''
        Returns the item at the front of the queue
        Raises QueueEmptyException if the queue is empty
        '''
        item_str = ""
        if self.is_empty():
            raise QueueEmptyException("Queue is Empty")
        else:
            item_str = self.queue_items[(self.head + 1) % self.max_size]
        return item_str
    

    def size(self):
        '''
        Returns the number of items in the queue
        '''
        return self.queue_size

    def print_queue(self):
        '''
        returns a string representation of the queue
        '''
        queue_str = ""
        if self.is_empty():
            queue_str = "Queue is Empty"
        else:
            for i in range(self.tail, self.tail - self.queue_size, -1):
                item = self.queue_items[i % self.max_size]
                if item != None:
                    queue_str = str(item) + "\n" + queue_str
        return queue_str
    