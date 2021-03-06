'''

Implement the following operations of a queue using stacks.

push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.
Example:

MyQueue queue = new MyQueue();

queue.push(1);
queue.push(2);  
queue.peek();  // returns 1
queue.pop();   // returns 1
queue.empty(); // returns false
Notes:

You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.
You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).

'''


from collections import deque

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1 = deque()
        self.s2 = deque()
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.s1.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if len(self.s2) == 0:
            for i in range(len(self.s1)):
                temp = self.s1.pop()
                self.s2.append(temp)
            return self.s2.pop()
        else:
            return self.s2.pop()
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        if len(self.s2) == 0:
            for i in range(len(self.s1)):
                temp = self.s1.pop()
                self.s2.append(temp)
            return self.s2[-1]
        else:
            return self.s2[-1]       
        
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if len(self.s1) == 0 and len(self.s2) == 0:
            return True
        else:
            return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()



