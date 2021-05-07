import numpy as np


class Histogram:
    def __init__(self, n):
        self.maxCount = n
        self.list = np.zeros(n)
        self.count = 0

    def addDataPoint(self, i):
        self.list[self.count] = i
        self.count += 1

    def sum(self):
        sum = 0
        for i in range(self.count):
            sum += self.list[i]
        return sum

    def mean(self):
        sum = 0
        for i in range(self.count):
            sum += self.list[i]

        average = sum / self.count
        return average

    def max(self):
        ans = 0
        for i in range(self.count):
            ans = max(ans, self.list[i])
        return ans

    def min(self):
        ans = 0
        for i in range(self.count):
            ans = min(ans, self.list[i])
        return ans

    def draw(self):
        for i in range(self.count):
            for j in range(int(self.list[i])):
                print("#", end="")
            print("")


if __name__ == "__main__":
    test = Histogram(100)

    for i in range(10):
        test.addDataPoint(i)

    print("count: " + str(test.sum()))
    print("average: " + str(test.mean()))
    print("max: " + str(test.max()))
    print("min: " + str(test.min()))
    test.draw()
