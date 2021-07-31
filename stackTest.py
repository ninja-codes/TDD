import unittest
from Stack import *

class stackTest(unittest.TestCase):
    stack = None
    def setUp(self):
        self.stack = Stack()
    def test_whenStackCreated_isEmpty(self):
        self.assertEqual(self.stack.isEmpty(), True, "Should be empty")
    def test_pop_whenEmptyShouldUnderflow(self):
        self.assertRaises(RuntimeError, self.stack.pop)
    def test_Onepush_Onepop_stackEmpty(self):
        self.stack.push(11)
        self.stack.pop()
        self.assertEqual(self.stack.isEmpty(), True, "When Push and then pop stack should be empty")
    def test_afterTwoPushesOnePop_StackWillNotBeEmpty(self):
        self.stack.push(22)
        self.stack.push(33)
        self.stack.pop()
        self.assertEqual(self.stack.isEmpty(), False, "After two pushes and one pop stack should not be empty")
    def test_onePush_StackNotEmpty(self):
        self.stack.push(44)
        self.assertNotEqual(self.stack.isEmpty(), True,"Should not be empty")
    def test_after_pushingX_willPopX(self):
        self.stack.push(55)
        self.assertEqual(self.stack.pop(), 55, "After pushing X should pop X")
        self.stack.push(66)
        self.assertEqual(self.stack.pop(), 66, "After pushing X should pop X")
    def test_after_pushing_xy_will_pop_y_then_x(self):
        self.stack.push(77)
        self.stack.push(88)
        self.assertEqual(self.stack.pop(), 88, "Push in order XY, pop in order YX")
        self.assertEqual(self.stack.pop(), 77, "Push in order XY, pop in order YX")


if __name__ == '__main__':
    unittest.main()