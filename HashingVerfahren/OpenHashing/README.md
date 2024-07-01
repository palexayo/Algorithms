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

# Double Hashing

Double hashing is a collision resolution technique used in hash tables to efficiently handle collisions that occur when multiple keys hash to the same index. Unlike chaining or linear probing, double hashing employs two hash functions to determine the placement of keys in the hash table.

## How Double Hashing Works

### Hash Functions

- **First Hash Function (`hashFunction1`)**: Calculates the initial index for a key using the modulo operation (`hash(key) % self.size`). This function maps the key to a position within the hash table array.

- **Second Hash Function (`hashFunction2`)**: Determines the step size for probing. It computes a step size as `constant - (hash(key) % constant)`, where `constant` is typically a prime number close to the size of the hash table (`self.size`). This varying step size helps in avoiding clustering and efficiently finds an empty slot in the table.

### Collision Resolution

- **Insertion**: When inserting a key, if the calculated index is already occupied (`self.table[index] is not None`), double hashing is used to probe further in the table until an empty slot (`self.table[index] == None`) is found.

- **Deletion**: Instead of directly removing a key (which can complicate subsequent searches), the slot is marked as deleted (`self.table[index] = self.deleted`). This ensures that the slot is skipped during searches but maintains the integrity of the table.

- **Search**: To find a key, the same double hashing mechanism is employed. It calculates the initial index and probes through the table until either the key is found or an empty slot (`None`) is encountered.

## Implementation

The `DoubleHashing` class in Python initializes with a specified size and maintains a table (`self.table`) where keys are stored. It uses the `sympy.nextprime(size)` function to find a prime number close to the specified size for `hashFunction2`. The class provides methods for insertion (`insert`), deletion (`delete`), and searching (`search`) based on the principles of double hashing.

### Example Usage

```python
hash_table = DoubleHashing(10)  # Initialize with a size (e.g., 10)

# Insert some keys
hash_table.insert(5)
hash_table.insert(15)
hash_table.insert(25)

# Search for a key
print(hash_table.search(15))  # Output: Index where 15 is stored

# Delete a key
hash_table.delete(15)
print(hash_table.search(15))  # Output: None (key not found)
```
## Key Points

- **Efficiency**: Double hashing offers efficient performance for hash tables, particularly beneficial when dealing with a high load factor and frequent collisions. It helps minimize the number of collisions and ensures quick key retrieval operations.

- **Prime Number for `hashFunction2`**: Selecting a prime number close to the size of the hash table for `hashFunction2` is crucial. This choice reduces clustering of keys and promotes a more even distribution across the hash table, enhancing overall performance.

- **Deleted Marker**: Utilizing a designated marker (`self.deleted`) for deleted keys is essential in maintaining the integrity of the hash table during deletion operations. This marker ensures that the search process correctly identifies deleted slots and avoids unnecessary re-probing.

These key points highlight the advantages and considerations of using double hashing in hash table implementations, emphasizing its efficiency, distribution properties, and robust handling of deleted entries.
