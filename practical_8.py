class Stack:
    top = -1
    items = []

    def push(self, element):
        self.top += 1
        self.items.insert(self.top, element)
        print(f'Pushed: {element}')

    def pop(self):
        if self.top <= -1:
            return
        self.top -= 1
        print(f'Poped: {self.items[self.top+1]}')

    def traverse(self):
        if self.top <= -1:
            print('Stack Empty!')
            return
        print("Stack:", end=' ')
        for i in range(self.top+1):
            print(self.items[i], end=' ')
        print('')


s = Stack()

s.push(10)
s.push(20)
s.push(5)

s.traverse()

s.pop()
s.pop()

s.push(9)

s.traverse()
