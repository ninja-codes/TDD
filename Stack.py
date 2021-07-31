class Stack():
    def __init__(self):
        self.size = 0
        self.elements = []
    def isEmpty(self):
        return self.size == 0
    def push(self, element):
        self.size = self.size + 1
        self.elements.insert(self.size-1, element)
    def pop(self):
        if self.isEmpty():
            raise RuntimeError
        else:
            self.size = self.size - 1
            retElm = self.elements[self.size]
            return retElm
