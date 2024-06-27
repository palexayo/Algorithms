# Hashtable Implementation with Chaining

This Python code implements a basic hash table using chaining to handle collisions. It includes methods for insertion, search, and removal of key-value pairs.

## Node Class

The `Node` class represents an element in a linked list used for chaining in the hash table.

### Attributes:
- `key`: Stores the key used for hashing and retrieval.
- `value`: Stores the corresponding value associated with the key.
- `next`: Points to the next `Node` object in the linked list. Initialized to `None` indicating no next node initially.

## Hashtable Class

The `Hashtable` class implements the hash table with chaining using an array of linked lists.

### Attributes:
- `size`: Specifies the size of the hash table.
- `table`: An array (`list` in Python) of size `size`, initialized with `None`. Each element in this array potentially holds a linked list of `Node` objects.

### Methods:

#### `__init__(self, size)`
- Initializes the hash table with the specified size and initializes each bucket in the `table` with `None`.

#### `hash_function(self, key)`
- Computes the hash index for a given key using Python's built-in `hash()` function and modulo operation.

#### `insert(self, key, value)`
- Inserts a key-value pair into the hash table. Handles collisions using chaining.
  
#### `search(self, key)`
- Searches for a key in the hash table and returns its corresponding value if found, otherwise returns `None`.

#### `remove(self, key)`
- Removes a key-value pair from the hash table. Returns `True` if removal was successful, otherwise returns `False`.

### Example Usage:

```python
# Example usage of the Hashtable class

# Initialize a hash table with size 10
hash_table = Hashtable(10)

# Insert key-value pairs
hash_table.insert("key1", "value1")
hash_table.insert("key2", "value2")
hash_table.insert("key3", "value3")

# Search for a key
print(hash_table.search("key2"))  # Output: value2

# Remove a key
hash_table.remove("key2")

# Search again after removal
print(hash_table.search("key2"))  # Output: None, key2 was removed
