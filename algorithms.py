from isSorted import is_sorted


class Algorithm:
    def step(self):
        pass
    name = "Algorithm"
    arr = []


class BogoSort(Algorithm):
    def __init__(self, arr2):
        self.arr = arr2
        self.name = "BogoSort"

    def step(self):
        if is_sorted(self.arr):
            return None, None
        # swap two random
        import random
        i = random.randint(0, len(self.arr)-1)
        j = random.randint(0, len(self.arr)-1)
        self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
        return i,j

class StalinSort(Algorithm):
    def __init__(self, arr2):
        self.arr = arr2
        self.name = "StalinSort"
        self.i = 0

    def step(self):
        if not is_sorted(self.arr) and self.i >= len(self.arr) - 1:
            self.i = 0
        if is_sorted(self.arr) or self.i >= len(self.arr) - 1:
            return None, None
        this = self.arr[self.i]
        next = self.arr[self.i + 1]
        if this > next:
            del self.arr[self.i]
        else:
            self.i += 1
        return None, None