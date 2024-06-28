class QuadraticProbingHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
        self.deleted = object()

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        j = 0

        #Quadratic Probing now
        while self.table[index] is not None:
            j += 1
            index = (index + j**2) % self.size

        self.table[index] = (key, value)

    def search(self, key):
        index = self.hash_function(key)
        j = 0

        #Quadratic Probing again
        while self.table[index] is not None:
            if self.table[index] != self.deleted and self.table[index][0] == key:
                return self.table[index][1]
            j += 1
            index = (self.hash_function(key) + j**2) % self.size

        return None

    def delete(self, key):
        index = self.hash_function(key)
        j = 0

        #Quadratic Probing
        while self.table[index] is not None:
            if self.table[index] != self.deleted and self.table[index][0] == key:
                self.table[index] = self.deleted
                return True
            j += 1
            index = (index + j**2) % self.size

        return False

    def __str__(self):
        return str([None if item == self.deleted else item for item in self.table])

# Beispielverwendung
hash_table = QuadraticProbingHashTable(11)  # 11 ist eine Primzahl der Form 4i + 3

# Einfügen von Elementen
hash_table.insert(10, "A")
hash_table.insert(21, "B")
hash_table.insert(32, "C")

# Suchen von Elementen
print("Suche 10:", hash_table.search(10))  # Ausgabe: A
print("Suche 21:", hash_table.search(21))  # Ausgabe: B
print("Suche 32:", hash_table.search(32))  # Ausgabe: C
print("Suche 43:", hash_table.search(43))  # Ausgabe: None

# Löschen von Elementen
hash_table.delete(21)
print("Nach dem Löschen von 21:", hash_table.search(21))  # Ausgabe: None

# Anzeige der Hash-Tabelle
print(hash_table)