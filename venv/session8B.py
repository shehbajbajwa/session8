class Product:
    count = 0

    def __init__(self):
        Product.count = Product.count + 1

    def showNumberOfObject(self):
        print("the number of objects is:{}".format(Product.count))


p1 = Product()
p2 = Product()
p3 = Product()
p4 = p1
p5 = p3

p5.showNumberOfObject()

#total product object : ?