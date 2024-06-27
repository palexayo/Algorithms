# Linear Probing Hash Table

## Overview

A linear probing hash table is a data structure used for associative arrays, implementing the hash table with a technique called linear probing to handle collisions. This README provides an explanation of the theory behind linear probing and describes an example implementation in Python.

### Key Concepts

- **Hash Function**: A function that maps keys to indices in the hash table array.
- **Collision Handling**: Linear probing resolves collisions by sequentially searching through the table for the next available slot.
- **Deletion Marking**: Deleted elements are marked rather than removed to maintain the integrity of the probing sequence.

## Example Implementation

### Python Code

```python
class LinearProbingHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
        self.deleted = object()  # Unique marker for deleted elements

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key):
        index = self.hash_function(key)
        original_index = index
        i = 0

        while self.table[index] is not None:
            i += 1
            index = (original_index + i) % self.size
            if index == original_index:
                raise Exception("Hash table is full")

        self.table[index] = key

    def search(self, key):
        index = self.hash_function(key)
        original_index = index
        i = 0

        while self.table[index] is not None:
            if self.table[index] == key:
                return index
            i += 1
            index = (original_index + i) % self.size
            if index == original_index:
                break

        return None

    def delete(self, key):
        index = self.search(key)
        if index is not None:
            self.table[index] = self.deleted
        else:
            print("Key not found")

    def display(self):
        for i, val in enumerate(self.table):
            if val is self.deleted:
                print(f"Index {i}: [Deleted]")
            else:
                print(f"Index {i}: {val}")
```
## Advantages

- **Space Efficiency**: Linear probing uses a single array for both keys and deleted markers, reducing space overhead compared to other collision resolution techniques like chaining.
- **Simple Implementation**: It is straightforward to implement compared to methods involving linked lists (chaining).
- **Cache Efficiency**: Linear probing can be more cache-friendly due to better locality of reference, as consecutive elements are stored adjacently in memory.

## Considerations

- **Clustering**: Sequential insertions and deletions can lead to clustering, where consecutive elements in the table are filled, potentially reducing performance as probes become longer.
- **Deleted Marking**: Properly marking deleted slots (`self.deleted`) is crucial to distinguish between actual deleted entries and empty slots, ensuring accurate search operations.

## Challenges

- **Handling Full Table**: When the hash table becomes full (all slots are occupied), resizing the table and rehashing existing keys is necessary for maintaining performance and avoiding collisions.
- **Performance Impact**: Clustering and longer probe sequences can degrade performance, especially under high load factors or uneven distribution of hash values.
- **Deletion Management**: Managing deletions, especially during resizing or rehashing operations, requires careful handling to maintain the correct state of the hash table.
