class Stack():
    def __init__(self):
        self.items=[]

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items==[]

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def get_stack(self):
        return self.items


s1=Stack()
s1.push("S")
s1.push("h")
s1.push("r")
s1.push("i")
print(s1.get_stack())
s1.push("p")
print(s1.get_stack())
s1.pop()
print(s1.get_stack())