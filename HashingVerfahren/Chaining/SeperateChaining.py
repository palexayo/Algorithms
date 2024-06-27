class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class Hashtable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)

        if self.table[index] is None:
            self.table[index] = Node(key, value)
        else:
            current = self.table[index]
            while current.next is not None:
                current = current.next
            current.next = Node(key, value)

    def search(self, key):
        index = self.hash_function(key)
        current = self.table[index]

        while current is not None:
            if current.key == key:
                return current.value
            current = current.next

        return None

    def remove(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        previous = None

        while current is not None:
            if current.key == key:
                if previous:
                    previous.nex = current.next
                else:
                    self.table[index] = current.next
                    return True
            previous = current
            current = current.next

        return False


# Beispiel zur Verwendung der Hash-Tabelle
hash_table = Hashtable(10)
hash_table.insert("key1", "value1")
hash_table.insert("key2", "value2")
hash_table.insert("key3", "value3")

print(hash_table.search("key2"))  # Ausgabe: value2

hash_table.remove("key2")
print(hash_table.search("key2"))  # Ausgabe: None, da "key2" entfernt wurde