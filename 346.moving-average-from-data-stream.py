""" Solution 1 """
# import queue

# class MovingAverage:

#     def __init__(self, size: int):
#         self.queue = queue.Queue(size)
#         self.size = 0
#         self.summation = 0.0

#     def next(self, val: int) -> float:
#         if self.queue.full():
#             _val = self.queue.get()
#             self.size -= 1
#             self.summation -= _val
#         self.queue.put(val)
#         self.size += 1
#         self.summation += val

#         return self.summation / self.size

""" Solution 2: circular queue """

class MovingAverage:
    def __init__(self, size: int) -> None:
        self.size = size
        self.head = 0
        self.windows_sum = 0
        self.queue = [0] * size
        self.counter = 0
    def next(self, val: int) -> float:
        self.counter += 1
        tail = (self.head + 1) % self.size
        self.windows_sum = self.windows_sum - self.queue[tail] + val
        self.head = (self.head + 1) % self.size
        self.queue[self.head] = val
        return self.windows_sum/min(self.size, self.counter)