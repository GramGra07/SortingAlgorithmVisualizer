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

class BubbleSort(Algorithm):
    def __init__(self, arr2):
        self.arr = arr2
        self.name = "BubbleSort"
        self.n = len(self.arr)
        self.i = 0
        self.j = 0

    def step(self):
        if is_sorted(self.arr):
            return None, None
        if self.j >= self.n - self.i - 1:
            self.i += 1
            self.j = 0
        if self.i >= self.n - 1:
            return None, None
        if self.arr[self.j] > self.arr[self.j + 1]:
            self.arr[self.j], self.arr[self.j + 1] = self.arr[self.j + 1], self.arr[self.j]
            swap1, swap2 = self.j, self.j + 1
        else:
            swap1, swap2 = None, None
        self.j += 1
        return swap1, swap2

class QuickSort(Algorithm):
        def __init__(self, arr2):
            self.arr = arr2
            self.name = "QuickSort"
            self.stack = [(0, len(self.arr) - 1)]

        def step(self):
            if is_sorted(self.arr):
                return None, None
            if not self.stack:
                return None, None

            low, high = self.stack.pop()
            if low < high:
                pivot_index = self.partition(low, high)
                self.stack.append((low, pivot_index - 1))
                self.stack.append((pivot_index + 1, high))
            return None, None

        def partition(self, low, high):
            pivot = self.arr[high]
            i = low - 1
            for j in range(low, high):
                if self.arr[j] < pivot:
                    i += 1
                    self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
            self.arr[i + 1], self.arr[high] = self.arr[high], self.arr[i + 1]
            return i + 1

class MergeSort(Algorithm):
    def __init__(self, arr2):
        self.arr = arr2
        self.name = "MergeSort"
        self.temp_arr = [0] * len(self.arr)
        self.current_size = 1
        self.left_start = 0

    def step(self):
        if is_sorted(self.arr):
            return None, None
        if self.current_size >= len(self.arr):
            return None, None

        mid = min(self.left_start + self.current_size - 1, len(self.arr) - 1)
        right_end = min(self.left_start + 2 * self.current_size - 1, len(self.arr) - 1)
        self.merge(self.left_start, mid, right_end)

        self.left_start += 2 * self.current_size
        if self.left_start >= len(self.arr) - 1:
            self.left_start = 0
            self.current_size *= 2

        return None, None

    def merge(self, left, mid, right):
        for i in range(left, right + 1):
            self.temp_arr[i] = self.arr[i]

        i = left
        j = mid + 1
        k = left

        while i <= mid and j <= right:
            if self.temp_arr[i] <= self.temp_arr[j]:
                self.arr[k] = self.temp_arr[i]
                i += 1
            else:
                self.arr[k] = self.temp_arr[j]
                j += 1
            k += 1

        while i <= mid:
            self.arr[k] = self.temp_arr[i]
            i += 1
            k += 1

        while j <= right:
            self.arr[k] = self.temp_arr[j]
            j += 1
            k += 1
class InsertionSort(Algorithm):
    def __init__(self, arr2):
        self.arr = arr2
        self.name = "InsertionSort"
        self.i = 1
        self.j = 0

    def step(self):
        if is_sorted(self.arr):
            return None, None
        if self.i >= len(self.arr):
            return None, None

        key = self.arr[self.i]
        self.j = self.i - 1

        while self.j >= 0 and self.arr[self.j] > key:
            self.arr[self.j + 1] = self.arr[self.j]
            self.j -= 1

        self.arr[self.j + 1] = key
        self.i += 1

        return None, None

class HeapSort(Algorithm):
    def __init__(self, arr2):
        self.arr = arr2
        self.name = "HeapSort"
        self.n = len(self.arr)
        self.i = self.n // 2 - 1
        self.j = self.n - 1

    def step(self):
        if is_sorted(self.arr):
            return None, None
        if self.i >= 0:
            self.heapify(self.n, self.i)
            self.i -= 1
        elif self.j > 0:
            self.arr[0], self.arr[self.j] = self.arr[self.j], self.arr[0]
            self.heapify(self.j, 0)
            self.j -= 1
        return None, None

    def heapify(self, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and self.arr[i] < self.arr[left]:
            largest = left
        if right < n and self.arr[largest] < self.arr[right]:
            largest = right
        if largest != i:
            self.arr[i], self.arr[largest] = self.arr[largest], self.arr[i]
            self.heapify(n, largest)

class SelectionSort(Algorithm):
    def __init__(self, arr2):
        self.arr = arr2
        self.name = "SelectionSort"
        self.i = 0
        self.j = 0

    def step(self):
        if is_sorted(self.arr):
            return None, None
        if self.i < len(self.arr) - 1:
            min_idx = self.i
            for j in range(self.i + 1, len(self.arr)):
                if self.arr[j] < self.arr[min_idx]:
                    min_idx = j
            self.arr[self.i], self.arr[min_idx] = self.arr[min_idx], self.arr[self.i]
            self.i += 1
        return None, None
class TimSort(Algorithm):
    def __init__(self, arr2):
        self.arr = arr2
        self.name = "TimSort"
        self.min_run = 32
        self.n = len(self.arr)
        self.runs = []
        self.current_run = []

    def step(self):
        if is_sorted(self.arr):
            return None, None
        if not self.runs:
            self.create_runs()
        if len(self.runs) == 1:
            return None, None
        self.merge_runs()
        return None, None

    def create_runs(self):
        for i in range(0, self.n, self.min_run):
            run = self.arr[i:i + self.min_run]
            run.sort()
            self.runs.append(run)

    def merge_runs(self):
        if len(self.runs) <= 1:
            return
        new_runs = []
        for i in range(0, len(self.runs) - 1, 2):
            new_runs.append(self.merge(self.runs[i], self.runs[i + 1]))
        if len(self.runs) % 2 == 1:
            new_runs.append(self.runs[-1])
        self.runs = new_runs
        self.arr = [item for run in self.runs for item in run]

    def merge(self, left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result