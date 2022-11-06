from collections import defaultdict


class ListNode:
    def __init__(self, key: int = 0, value: int = 0):
        self.key = key
        self.value = value
        self.freq = 1
        self.prev = None
        self.next = None


class DoubleyLinkedList:
    def __init__(self):
        self.size = 0
        self.dummy_head = ListNode()
        self.dummy_tail = ListNode()
        self.dummy_head.next = self.dummy_tail  # type: ignore
        self.dummy_tail.prev = self.dummy_head  # type: ignore

    def __len__(self):
        return self.size

    def remove(self, node: ListNode) -> None:
        self.size -= 1
        previous_node, next_node = node.prev, node.next
        next_node.prev = previous_node  # type: ignore
        previous_node.next = next_node  # type: ignore

    def remove_head(self) -> ListNode:
        head = self.dummy_head.next
        self.remove(head)  # type: ignore
        return head  # type: ignore

    def insert(self, node: ListNode) -> None:
        self.size += 1
        previous_node = self.dummy_tail.prev
        self.dummy_tail.prev = previous_node.next = node  # type: ignore
        node.prev, node.next = previous_node, self.dummy_tail  # type: ignore


class LFUCache:
    def __init__(self, capacity: int):
        self.cache = dict()
        self.freq_table = defaultdict(DoubleyLinkedList)
        self.capacity = capacity
        self.min_freq = 0

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        return self.update_cache(self.cache[key], key, self.cache[key].value)

    def put(self, key: int, value: int) -> None:
        if not self.capacity:
            return
        if key in self.cache:
            self.update_cache(self.cache[key], key, value)
        else:
            if len(self.cache) == self.capacity:
                prev_head = self.freq_table[self.min_freq].remove_head()
                del self.cache[prev_head.key]

            new_node = ListNode(key, value)
            self.freq_table[1].insert(new_node)
            self.cache[key] = new_node
            self.min_freq = 1

    def update_cache(self, node: ListNode, key: int, new_value: int) -> int:
        node = self.cache[key]
        node.value = new_value
        prev_freq = node.freq
        node.freq += 1
        self.freq_table[prev_freq].remove(node)
        self.freq_table[node.freq].insert(node)
        if prev_freq == self.min_freq and len(self.freq_table[prev_freq]) == 0:
            self.min_freq += 1

        return node.value
