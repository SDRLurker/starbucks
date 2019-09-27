class MyQueue:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.add_stack = []
        self.del_stack = []
        
    def push(self, x):
        """
        Push element x to the back of queue.
        """
        while self.del_stack:
            self.add_stack.append(self.del_stack.pop())
        self.add_stack.append(x)
        
    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        """
        while self.add_stack:
            self.del_stack.append(self.add_stack.pop())
        if self.del_stack:
            return self.del_stack.pop()
        return None
        
    def peek(self):
        """
        Get the front element.
        """
        while self.add_stack:
            self.del_stack.append(self.add_stack.pop())
        if self.del_stack:
            return self.del_stack[-1]
        return None
        
    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.add_stack and not self.del_stack
        
# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()            

import unittest
class test_solution(unittest.TestCase):
    def test_all(self):
        obj = MyQueue()
        obj.push(1)
        obj.push(2)
        self.assertEqual(obj.peek(),1)
        self.assertEqual(obj.pop(),1)
        self.assertEqual(obj.empty(), False)

        obj = MyQueue()
        obj.push(1)
        obj.push(2)
        self.assertEqual(obj.peek(),1)
        obj.push(3)
        self.assertEqual(obj.peek(),1)

if __name__ == "__main__":
    unittest.main()
