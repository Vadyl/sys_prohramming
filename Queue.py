class Queue:
    def __init__(self):
        self.elements = []

    def push(self, value):
        self.elements.append(value)

    def pop(self):
        if  len(self.elements) != 0:
            return self.elements.pop(0)
        else:
            return "no elements"

    def peek(self):
        if  len(self.elements) != 0:
            return self.elements[0]
        else:
            return "no elements"


def print_queue(input_arr):
    print(input_arr.elements)



example_array = Queue()

example_array.push(1)
example_array.push(3)
example_array.push(10)
example_array.push(20)
example_array.push(1000)

print_queue(example_array)

peeked_element = example_array.peek()
print("Peek:", peeked_element)

popped_element = example_array.pop()
print("Pop:", popped_element)

peeked_element = example_array.peek()
print("Peek:", peeked_element)

print_queue(example_array)
