'''

Design a max stack that supports push, pop, top, peekMax and popMax.

    push(x) -- Push element x onto stack.
    pop() -- Remove the element on top of the stack and return it.
    top() -- Get the element on the top.
    peekMax() -- Retrieve the maximum element in the stack.
    popMax() -- Retrieve the maximum element in the stack, and remove it. If you find more than one maximum elements, only remove the top-most one.

Example 1:

MaxStack stack = new MaxStack();
stack.push(5); 
stack.push(1);
stack.push(5);
stack.top(); -> 5
stack.popMax(); -> 5
stack.top(); -> 1
stack.peekMax(); -> 5
stack.pop(); -> 1
stack.top(); -> 5

Note:

    -1e7 <= x <= 1e7
    Number of operations won't exceed 10000.
    The last four operations won't be called when stack is empty.


'''

# approach 1

class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def peekMax(self) -> int:
        return max(self.stack)

    def popMax(self) -> int:
        item = max(self.stack)
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i] == item:
                index = i
                break
        return self.stack.pop(index)

# approach 2

class MaxStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.max = float('-inf')

    def push(self, x: int) -> None:
        self.max = max(x, self.stack[-1][1] if self.stack else x)
        self.stack.append((x, self.max))

    def pop(self) -> int:
        return self.stack.pop()[0]

    def top(self) -> int:
        return self.stack[-1][0]

    def peekMax(self) -> int:
        return self.stack[-1][1]

    def popMax(self) -> int:
        m = self.stack[-1][1]
        b = []
        while self.stack[-1][0] != m:
            b.append(self.stack.pop()[0])
        self.stack.pop()
        while b:
            item = b.pop()
            curr_m = max(item, self.stack[-1][1] if self.stack else item)
            self.stack.append((item, curr_m))
        return m

# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()



# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
    
