import sympy


class DoubleHashing:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
        self.deleted = object()

    def hashFunction1(self, key):
        #Normal first hashfunction as we know it
        return hash(key) % self.size

    def hashFunction2(self, key):
        constant = self.findPrim(self.size)
        return constant - (hash(key) % constant)

    def findPrim(self, size):
        return sympy.nextprime(size)
    def insert(self, key):
        initial_index = self.hashFunction1(key)
        index = initial_index
        step_size = self.hashFunction2(key)
        i = 1
        while self.table[index] is not None:
            index = (initial_index + i * step_size) % self.size
            i += 1

        self.table[index] = key

    def delete(self, key):
        initial_index = self.hashFunction1(key)
        index = initial_index
        step_size = self.hashFunction2(key)
        i = 1
        while self.table[index] is not None:
            if self.table[index] == key:
                self.table[index] = self.deleted  # Mark as deleted
                return True
            index = (initial_index + i * step_size) % self.size
            i += 1
        return False

    def search(self, key):
        initial_index = self.hashFunction1(key)
        index = initial_index
        step_size = self.hashFunction2(key)
        i = 1
        while self.table[index] is not None:
            if self.table[index] == key:
                return index
            index = (initial_index + i * step_size) % self.size
            i += 1
        return None

# Example usage:
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