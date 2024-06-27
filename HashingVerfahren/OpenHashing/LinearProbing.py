class LinearProbingHasTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
        self.deleted = object() #Unique markierung für gelöschte Elemente

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key):
        index = self.hash_function(key)
        original_index = index
        i = 0

        while self.table[index] is not None:
            i += 1
            index = (original_index + i) % self.size #modulo self.size to start at the beginning of the table and not just from the index
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

# Example usage
hash_table = LinearProbingHasTable(10)
hash_table.insert(10)
hash_table.insert(20)
hash_table.insert(30)
hash_table.insert(40)
hash_table.insert(50)
hash_table.insert(25)
hash_table.display()

print("\nSearch for 20:", hash_table.search(20))
print("Search for 25:", hash_table.search(25))
print("Search for 35:", hash_table.search(35))

hash_table.delete(20)
hash_table.delete(25)
hash_table.display()