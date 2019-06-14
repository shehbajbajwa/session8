class counter:
    ccount = 1

    def __init__(self):
        self.count = 1
        counter.ccount=1
    def incrementCount(self):
        self.count = self.count + 1
        counter.ccount = counter.ccount + 1

    def showCount(self):
        print("count is {}".format(self.count))
        print("count is {}and ccount is {}".format(self.count,counter.ccount))

c1 = counter()
c2 = counter()
c3 = c1

c1.incrementCount()
c2.incrementCount()
c3.incrementCount()

c1.incrementCount()
c2.incrementCount()
c3.incrementCount()

c4 = counter()


c1.showCount()
c2.showCount()
c3.showCount()
c4.showCount()
