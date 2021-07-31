import unittest
from Queue import *

class QueueTest(unittest.TestCase):
    queue = None
    def setUp(self):
        self.queue = Queue()
    def test_when_queue_created_should_be_empty(self):
        self.assertIs(self.queue.isEmpty(), True)
    def test_one_enqueue_should_not_be_empty(self): 
        self.queue.enqueue(5)
        self.assertIs(self.queue.isEmpty(), False)
    def test_one_enqueue_one_dequeue_queue_empty(self):
        self.queue.enqueue(77)
        self.queue.dequeue()
        self.assertIs(self.queue.isEmpty(), True)
    def test_dequeue_empty_queue_should_underflow(self):
        self.assertRaises(RuntimeError, self.queue.dequeue)
    def test_enqueueX_should_dequeueX(self):
        self.queue.enqueue(11)
        self.assertIs(self.queue.dequeue(), 11)
        self.queue.enqueue(22)
        self.assertIs(self.queue.dequeue(), 22)
    def test_two_enqueue_one_dequeue_queue_not_empty(self):
        self.queue.enqueue(33)
        self.queue.enqueue(44)
        self.queue.dequeue()
        self.assertIs(self.queue.isEmpty(), False)
    def test_enqueue_abcd_dequeue_abcd(self):
        self.queue.enqueue(33)
        self.queue.enqueue(44)
        self.queue.enqueue(55)
        self.queue.enqueue(66)
        self.assertIs(self.queue.dequeue(), 33)
        self.assertIs(self.queue.dequeue(), 44)        
        self.assertIs(self.queue.dequeue(), 55)
        self.assertIs(self.queue.dequeue(), 66)

if __name__ == '__main__':
    unittest.main()