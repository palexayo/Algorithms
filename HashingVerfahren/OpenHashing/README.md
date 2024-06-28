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


# Quadratic Probing in Hash Tables

Quadratic probing is a collision resolution technique used in hash tables to address the issue of multiple keys hashing to the same index. This README provides an overview of quadratic probing, its advantages, disadvantages, and the rationale behind its use.

## Overview

A hash table is a data structure that maps keys to values using a hash function to compute an index into an array of buckets or slots. Collisions occur when multiple keys hash to the same index. Quadratic probing is one approach to resolving collisions in open addressing schemes.

### How Quadratic Probing Works

1. **Hash Function**: Compute the initial index using a hash function.
   
2. **Collision Handling**: If the computed slot is already occupied:
   - Use a quadratic sequence (\( j^2 \)) to probe subsequent slots until an empty slot is found.
   - Insert the key-value pair into the empty slot.

3. **Searching and Deleting**: When searching or deleting:
   - Use the same quadratic sequence to find the key or mark the slot as deleted (without physically removing it).

## Advantages

- **Simplicity**: Quadratic probing is relatively simple to implement compared to chaining.
- **Space Efficiency**: It does not require additional memory for pointers or linked lists.
- **Performance**: Effective under certain conditions (e.g., low load factors) due to reduced clustering compared to linear probing.

## Disadvantages

- **Clustering**: Can suffer from primary and secondary clustering, impacting performance under high load factors.
- **Probing Sequence Dependence**: Effectiveness relies on the choice of quadratic sequence, which can affect clustering behavior.
- **Performance Degradation**: Efficiency can degrade as the hash table becomes more full, increasing average search times.

## Rationale Behind Using Quadratic Probing

- **Avoiding Primary Clustering**: Reduces consecutive collisions at the same initial position compared to linear probing.
- **Memory Efficiency**: Compact representation without additional storage overhead.
- **Suitability for Open Addressing**: Well-suited for scenarios where every slot in the hash table needs to store key-value pairs or deletion markers.

## Conclusion

Quadratic probing offers a balance between simplicity, space efficiency, and performance in certain hash table implementations. Understanding its advantages, disadvantages, and the conditions under which it performs well is crucial for choosing an appropriate collision resolution strategy based on specific application requirements.

