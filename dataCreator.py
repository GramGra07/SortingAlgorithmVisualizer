import random

class DataCreator:
    def __init__(self, n):
        self.n = n
        self.data = [i for i in range(1, n+1)]
        random.shuffle(self.data)
        print(self.data)

    def getData(self):
        return self.data

    def resetData(self):
        self.data = [i for i in range(1, self.n+1)]
        random.shuffle(self.data)
