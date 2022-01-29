class LRUCache:
    def __init__(self, capacity: int):
        self.max_capacity = capacity
        self.current_capacity = 0
        self.cache = {}
        self.deque = None
        self.last = None

    def get(self, key: int) -> int:
        if key not in self.cache:
            return None
        else:
            link = self.cache[key]
            self.update_position(link)
            return link.val

    def put(self, key: int, value: int) -> None:
        if key not in self.cache: # Init key val pair and link at front
            link = DLink(key, value, self.deque)
            self.cache[key] = link
            self.current_capacity += 1

            if self.current_capacity == 1: # Init last
                self.last = link
                self.deque = link
            else:
                self.deque.before, self.deque = link, link

            if self.current_capacity > self.max_capacity: # Remove last link
                key_to_remove = self.last.key
                self.last = self.last.before
                self.last.after = None
                self.cache.pop(key_to_remove)
                self.current_capacity -= 1
            
        else: # Key already exists, update val and move link to front
            link = self.cache[key]
            link.val = value
            self.update_position(link)

    def update_position(self, link): # Move given link to front
        if link.before is None: # Link is first already (or only link)
            return
        elif link.after is None: # Link is last
            self.last = link.before
            self.last.after = None
        else: # Link is in the middle somewhere
            before_link = link.before
            after_link = link.after
            before_link.after, after_link.before = after_link, before_link
        link.before = None
        link.after = self.deque
        self.deque.before, self.deque = link, link

    def __str__(self):
        current = self.deque
        print_lst = []
        while current is not None:
            print_lst.append((current.key, current.val))
            current = current.after
        return str(print_lst)

class DLink:
    def __init__(self, key, val, after) -> None:
        self.val = val
        self.key = key
        self.after = after
        self.before = None

def main():
    # Test 1
    cache = LRUCache(3)
    cache.put(3, 6)
    cache.put(5, 1)
    cache.put(2, 7)
    cache.put(8, 9)
    if cache.__str__() == "[(8, 9), (2, 7), (5, 1)]":
        print("Test 1 passed")
    else:
        print("Test 1 failed")
        print(cache)

    # Test 2
    cache = LRUCache(3)
    cache.put(3, 6)
    cache.put(5, 1)
    cache.put(2, 7)
    cache.get(3)
    cache.put(8, 9)
    if cache.__str__() == "[(8, 9), (3, 6), (2, 7)]":
        print("Test 2 passed")
    else:
        print("Test 2 failed")
        print(cache)

    # Test 2
    cache = LRUCache(3)
    cache.put(3, 6)
    cache.put(5, 1)
    cache.put(2, 7)
    cache.put(3, 345)
    cache.put(8, 9)
    if cache.__str__() == "[(8, 9), (3, 345), (2, 7)]":
        print("Test 2 passed")
    else:
        print("Test 2 failed")
        print(cache)

if __name__ == "__main__":
    main()