class RingBuffer:
    # This class starts out empty (not full yet)
    def __init__(self, capacity):
        # Give the class a max size
        self.capacity = capacity
        self.data = []

    # Appends an element at the end of the buffer
    def append(self, item):
        self.data.append(item)
        # If the length reaches max...
        if len(self.data) == self.capacity:
            self.cur = 0
            # Change class from non-full to full
            self.__class__ = self.RingBufferFull

    # Returns a list of elements from oldest to newest
    def get(self):
        return self.data

    class RingBufferFull:
        def __init__(self, n):
            raise "string"

        # Appends an element overwriting the oldest one
        def append(self, item):
            self.data[self.cur] = item
            self.cur = (self.cur + 1) % self.capacity

        # Returns the list of elements in correct order
        def get(self):
            return self.data
            