class Queue:
    def __init__(self):
        self.elements = []
        self.size = 0
        self.head = 0
    
    def isEmpty(self):
        return self.size == 0

    def enqueue(self, element):
        self.elements.insert(self.size+1, element)
        self.size = self.size + 1

    def dequeue(self):
        if self.isEmpty():
            raise RuntimeError
        self.size = self.size - 1
        elm = self.elements[self.head]
        self.head = self.head + 1  
        return elm