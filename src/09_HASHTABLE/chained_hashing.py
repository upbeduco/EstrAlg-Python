# An implementation of the Chaining Symbol Table in Python


class ChainingST:

    def __init__(self, M):
        self.M = M  # Size of the hash table
        self.st = [[] for _ in range(M)]  # Initialize a list of empty lists for chaining

    def hash(self, key):
        return hash(key) % self.M  # Hash function to map keys to indices

    def put(self, key, value):
        index = self.hash(key)
        for i, (k, v) in enumerate(self.st[index]):
            if k == key:
                self.st[index][i] = (key, value)  # Update existing key
                return
        self.st[index].append((key, value))  # Add new key-value pair

    def get(self, key):
        index = self.hash(key)
        for k, v in self.st[index]:
            if k == key:
                return v  # Return value if key is found
        return None  # Return None if key is not found

    def delete(self, key):
        index = self.hash(key)
        for i, (k, v) in enumerate(self.st[index]):
            if k == key:
                del self.st[index][i]  # Remove the key-value pair
                return    
            
    def rehash(self, new_size):
        old_st = self.st
        self.M = new_size
        self.st = [[] for _ in range(new_size)]
        for bucket in old_st:
            for key, value in bucket:
                self.put(key, value)
        old_st = self.st

    def __str__(self):
        """Returns a string representation of the hash table.
        Only list per line.
        """
        return '\n'.join([f"{i}: {bucket}" for i, bucket in enumerate(self.st) if bucket])

    def __len__(self):
        """Returns the number of key-value pairs in the hash table."""
        return sum(len(bucket) for bucket in self.st)
    
    def __contains__(self, key):
        """Checks if a key is in the hash table."""
        index = self.hash(key)
        for k, v in self.st[index]:
            if k == key:
                return True
        return False
    
    def keys(self):
        """Returns a list of all keys in the hash table."""
        return [k for bucket in self.st for k, v in bucket]
    
    def clear(self):
        """Clears the hash table."""
        self.st = [[] for _ in range(self.M)]
