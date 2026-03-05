import random

class RandomizedSet:
    def __init__(self):
        self.len = 0
        self.mapping_idx_val = {}
        self.mapping_val_idx = {}

    def insert(self, val: int) -> bool:
        if val not in self.mapping_val_idx:
            self.mapping_idx_val[self.len] = val
            self.mapping_val_idx[val] = self.len
            self.len += 1
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.mapping_val_idx:
            self.len -= 1
            idx = self.mapping_val_idx[val]
            last_idx = self.len

            if idx != last_idx:
                last_val = self.mapping_idx_val[last_idx]

                # move last element to removed position
                self.mapping_idx_val[idx] = last_val
                self.mapping_val_idx[last_val] = idx

            # delete last element
            del self.mapping_idx_val[last_idx]
            del self.mapping_val_idx[val]

            return True
        return False

    def getRandom(self) -> int:
        idx = random.randint(0, self.len - 1)
        return self.mapping_idx_val[idx]